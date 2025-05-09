from openai import OpenAI  # Import OpenAI class for interacting with the OpenAI API
import os  # Import os module for file operations and environment variables
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from .env file
from memory_data.memory import Memory  # Import Memory class for managing memory

# Load environment variables from .env file
load_dotenv()

class Core:
    def __init__(self, training_data, model="deepseek/deepseek-r1:free", save_mem=True):
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

        self.short = self.load_short_term_memory()

    def get_response(self, user_message):
        # Method to get a response from the AI based on user_message and training_data
        completion = self.client.chat.completions.create(
            model=self.model,  # Use the model set during initialization
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"{self.training_data}"  # Include training data in the system message
                        f"This is your short term memory\n{self.short}"
                    ),
                    
                        
                   
                },
                {
                    "role": "user",
                    "content": user_message  # Include user_message in the user role
                }
            ],
            max_tokens=512,  # Maximum tokens in the response
            temperature=0.7,  # Temperature for the response
            top_p=1.0,  # Top p value for the response
            frequency_penalty=0.0,  # Frequency penalty for the response
            presence_penalty=0.0,  # Presence penalty for the response
        )
        response = completion.choices[0].message.content  # Return the content of the first choice
        self.add_to_short(f"\n[USER]: {user_message}\n[YOU]: {response}")
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


    def load_short_term_memory(self):
        if self.mem is not None:
            short_mem = self.mem.load_short()
            
            return short_mem
       
        return None
    def add_to_short(self,data):
        if self.mem is not None:
            short_mem = self.mem.add_short(data)
            
            self.short += f"\n{data}"
            
       
        return None
