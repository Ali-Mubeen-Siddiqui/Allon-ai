from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Core:
    def __init__(self,training_data, model="deepseek/deepseek-r1:free"):
        # Get API key from environment variables
        self.model = model
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY not found in environment variables")
        try:
            self.client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=api_key,
                )
            
        except Exception as e:
            print(f"error creating the core of ai:\n {e}")
            exit(0)

        self.training_data = self.load_training_data(training_data)

    def get_response(self, user_message):
        completion = self.client.chat.completions.create(
            model = self.model,
            messages = [
                {
                    "role": "system",
                    "content": (
                        f"{self.training_data}"
                    )
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            max_tokens=512,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        return completion.choices[0].message.content
        
    def load_training_data(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Training data file not found: {path}")
        try:
            with open(path, "r", encoding="utf-8") as trainD:
                data = trainD.read()
            return data
        except Exception as e:
            raise IOError(f"Error reading training data: {e}")

