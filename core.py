from openai import OpenAI  # Import OpenAI class for interacting with the OpenAI API
import os  # Import os module for file operations and environment variables
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from .env file
from memory_data.memory import Memory  # Import Memory class for managing memory
import re #import regex
import json

from functions import functions,funcs_table
# Load environment variables from .env file
load_dotenv()

class Core:
    def __init__(self, training_data, model="meta-llama/llama-3.3-70b-instruct:free", save_mem=True):
        # Initialize the Core class with training data, model, and save_mem option
        # Get API key from environment variables
        self.model = model  # Set the model to use for the AI
        api_key = os.getenv("API_KEY")  # Retrieve API key from environment variables
        if not api_key:
            raise ValueError("API_KEY not found in environment variables")  # Raise error if API key is not found
        try:
            self.client = OpenAI(
                base_url="https://openrouter.ai/api/v1",  # Base URL for the OpenAI API
                api_key=api_key,  # Use the retrieved API key
                )
            
        except Exception as e:
            print(f"error creating the core of ai:\n {e}")  # Print error message if an exception occurs
            exit(0)  # Exit the program if an error occurs during initialization
        # Load training data
        self.training_data = self.load_training_data(training_data)  # Load training data from the specified path
        if save_mem:
            self.mem = Memory()  # Initialize memory if save_mem is True
        else:
            self.mem = None  # Set memory to None if save_mem is False

        self.short,self.long = self.load_memory()

    def get_response(self, user_message):
        # Method to get a response from the AI based on user_message and training_data
        completion = self.client.chat.completions.create(
            model=self.model,  # Use the model set during initialization
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"{self.training_data}\n at the starting of every response you will <long>true or false</long> ,this will tell that does this need to be saved in long memory or not."  # Include training data in the system message
                        f"This is your short term memory\n{self.short}"
                        f"This is your long term memory\n{self.long}"
                        f"whenever there is a need to perform a task like opening something or something that you cant do without using external functions just <function>true or false</function> to let program know that is there a need to call a function "
                        f"this is the list of funcs you need to remember \n{functions}\n whenever you have to call a function just give the JSON object with string keys like '0', '1', etc. containing 'function_name' and 'arguments' to be executed in <execute></execute> tags "
                    ),
                    
                        
                   
                },
                {
                    "role": "user",
                    "content": user_message  # Include user_message in the user role
                }
            ],
            max_tokens=1500,  # Maximum tokens in the response
            temperature=0.7,  # Temperature for the response
            top_p=1.0,  # Top p value for the response
            frequency_penalty=0.0,  # Frequency penalty for the response
            presence_penalty=0.0,  # Presence penalty for the response
        )
        

        full_response = completion.choices[0].message.content  # preserve original
        long_content = re.findall(r'<long>(.*?)</long>', full_response, flags=re.DOTALL)
        response = re.sub(r'<long>.*?</long>', '', full_response, flags=re.DOTALL)
        
        self.add_to_short(f"\n[USER]: {user_message}\n[ALLON]: {response}")
        if self.validate_long_or_short(long_content):
            self.add_to_long(f"\n[USER]: {user_message}\n[ALLON]: {response}")

        if self.validate_func(full_response):  # use full_response
            output = self.functions_main(full_response)  # pass full_response
            response += f"\n{output}"

        # Now clean tags after extracting
        response = re.sub(r'<function>.*?</function>', '', response, flags=re.DOTALL)
        response = re.sub(r'<execute>.*?</execute>', '', response, flags=re.DOTALL)
        
        return response
        
    def load_training_data(self, path):
        # Method to load training data from a file
        if not os.path.exists(path):
            raise FileNotFoundError(f"Training data file not found: {path}")  # Raise error if file does not exist
        try:
            with open(path, "r", encoding="utf-8") as trainD:
                data = trainD.read()  # Read the file content
            return data  # Return the read data
        except Exception as e:
            raise IOError(f"Error reading training data: {e}")  # Raise error if an exception occurs during file reading


    def load_memory(self):
        if self.mem is not None:
            short_mem = self.mem.load_short()
            long_mem = self.mem.load_long()
            
            return short_mem,long_mem
       
        return None
    def add_to_short(self,data):
        if self.mem is not None:
            short_mem = self.mem.add_short(data)
            
            self.short += f"\n{data}"
            
       
        return None

    def add_to_long(self,data):
        if self.mem is not None:
            long_mem = self.mem.add_long(data)
            self.long += f"\n {data}"

        return None
    
    def validate_long_or_short(self,choice : list):
        try:
            if choice[0].strip().lower() == "true":
                return True
            return False
        except IndexError:
            return True
        return False
    
    def validate_func(self,response):
        vres = re.findall(r'<function>.*?</function>',  response, flags=re.DOTALL)
        
        if vres:
            content = vres[0].replace('<function>', '').replace('</function>', '').strip().lower()
            if content == "true":
                return True
            else:
                return False
        return False
    
    def get_funcs_to_exec(self, response):
        func_json = re.findall(r'<execute>(.*?)</execute>', response, flags=re.DOTALL)
        if func_json:
            try:
                return {int(k): v for k, v in json.loads(func_json[0]).items()}

            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
        return []

        
    def execute_funcs(self,func_list):
        results = []
        
        for i in sorted(func_list.keys(),key=int):
            
            func = func_list[i]
            func_name = func["function_name"]
            if func_name not in funcs_table:
                results.append("cannot perform function")
                continue
            arg = func["arguments"]
            
            function = funcs_table[func_name]
            result = function(**arg)
            results.append(result)

        return results

    def functions_main(self,response):
        
        func_list = self.get_funcs_to_exec(response)
        results = self.execute_funcs(func_list)
        return results
