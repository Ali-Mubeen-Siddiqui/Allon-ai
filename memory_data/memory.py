import os
from datetime import datetime, timedelta
import json


class Memory:
    def __init__(self) -> None:
        # Initialize the base URL and paths for short-term and long-term memory files
        self.BASE_URL = os.getcwd()
        self.short_term_path = os.path.join(self.BASE_URL, "memory_data/shortTerm.txt")
        self.long_term_path = os.path.join(self.BASE_URL, "memory_data/longTerm.txt")
        self.config = os.path.join(self.BASE_URL, "memory_data/mem_config.json")
        # Set the duration for refresh time
        duration = 5

        # Ensure the directory for short-term memory exists
        os.makedirs(os.path.dirname(self.short_term_path), exist_ok=True)

        # Record the start time
        self.start_time = datetime.now()
        

        # Check if the short-term memory file exists, if not, create it
        if not os.path.exists(self.short_term_path):
            with open(self.short_term_path, "w", encoding="utf-8") as f:
                f.write("")

        # Ensure the configuration file exists
        self.ensure_config_exists()
        
        # Validate and add refresh time if necessary
        if self.validate_reftime():
            self.add_refresh_time(timedelta(minutes=duration))
            

    def ensure_config_exists(self):
        # Check if the configuration file exists, if not, create it with default data
        if not os.path.exists(self.config):
            config_data = {"short_term": {"refresh_time": ""}}
            with open(self.config, "w", encoding="utf-8") as config_file:
                json.dump(config_data, config_file)

    def load_short(self):
        # Load the content of the short-term memory file
        try:
            with open(self.short_term_path, "r", encoding="utf-8") as short_mem:
                short_txt = short_mem.read()
                return short_txt if short_txt else "No previous conversations."
        except FileNotFoundError:
            # If the file is not found, create it and return a default message
            with open(self.short_term_path, "w", encoding="utf-8") as f:
                f.write("")
            return "No previous conversations."
        except Exception as e:
            # Handle any other exceptions and return a default message
            print(f"Error loading short term memory: {e}")
            return "No previous conversations."
        

    def load_long(self):
        # Load the content of the long-term memory file
        try:
            with open(self.long_term_path, "r", encoding="utf-8") as long_mem:
                long_txt = long_mem.read()
                return long_txt if long_txt else "No previous conversations."
        except FileNotFoundError:
            # If the file is not found, create the short-term memory file and return a default message
            with open(self.short_term_path, "w", encoding="utf-8") as f:
                f.write("")
            return "No previous conversations."
        except Exception as e:
            # Handle any other exceptions and return a default message
            print(f"Error loading short term memory: {e}")
            return "No previous conversations."

    def add_short(self, data):
        # Add data to the short-term memory file
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.short_term_path, "a", encoding="utf-8") as short_mem:
                short_mem.write(f"\n{timestamp}\n{data}")
        except Exception as e:
            # Handle any exceptions during data addition
            print(f"Error adding to short term memory: {e}")

    def clear_short(self):
        # Clear the content of the short-term memory file
        try:
            with open(self.short_term_path, "w", encoding="utf-8") as short_mem:
                short_mem.write("")
        except Exception as e:
            # Handle any exceptions during clearing
            print(f"Error clearing short term memory: {e}")

    def add_refresh_time(self, duration: timedelta):
        # Add or update the refresh time in the configuration file
        try:
            with open(self.config, "r", encoding="utf-8") as config_file:
                config_data = json.load(config_file)

            refresh_time = (self.start_time + duration).strftime("%Y-%m-%d %H:%M:%S")
            config_data["short_term"]["refresh_time"] = refresh_time

            with open(self.config, "w", encoding="utf-8") as config_file:
                json.dump(config_data, config_file, indent=4)

            return config_data

        except FileNotFoundError:
            # Handle the case where the configuration file is not found
            print("Configuration file not found.")
            return {}
        except json.JSONDecodeError as e:
            # Handle JSON decoding errors
            print(f"Error decoding JSON from configuration file: {e}")
            return {}
        except Exception as e:
            # Handle any other exceptions
            print(f"Error reading configuration file: {e}")
            return {}

    def validate_reftime(self):
        # Validate the refresh time and clear short-term memory if necessary
        try:
            with open(self.config, "r", encoding="utf-8") as config_file:
                config_data = json.load(config_file)

            ref_time_prev = config_data["short_term"]["refresh_time"]
            ref_time_obj = datetime.strptime(ref_time_prev, "%Y-%m-%d %H:%M:%S")

            if self.start_time > ref_time_obj:
                self.clear_short()
                return True
                
            

        except FileNotFoundError:
            # Handle the case where the configuration file is not found
            print("Configuration file not found.")
            return False
        except json.JSONDecodeError as e:
            # Handle JSON decoding errors
            print(f"Error decoding JSON from configuration file: {e}")
            return False
        except Exception as e:
            # Handle any other exceptions
            print(f"Error reading configuration file: {e}")
            return False
        
    def add_long(self,data):
        # Add data to the long-term memory file
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.long_term_path, "a", encoding="utf-8") as long_mem:
                long_mem.write(f"\n{timestamp}\n{data}")
        except Exception as e:
            # Handle any exceptions during data addition
            print(f"Error adding to long term memory: {e}")
