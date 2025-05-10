import os
from datetime import datetime, timedelta
import json


class Memory:
    def __init__(self) -> None:
       
        self.BASE_URL = os.getcwd()
        self.short_term_path = os.path.join(self.BASE_URL, "memory_data/shortTerm.txt")
        self.config = os.path.join(self.BASE_URL, "memory_data/mem_config.json")
        duration = 5

        os.makedirs(os.path.dirname(self.short_term_path), exist_ok=True)

        self.start_time = datetime.now()
        

        if not os.path.exists(self.short_term_path):
            with open(self.short_term_path, "w", encoding="utf-8") as f:
                f.write("")

        self.ensure_config_exists()
        
        if self.validate_reftime():
            self.add_refresh_time(timedelta(minutes=duration))
            

    def ensure_config_exists(self):
        if not os.path.exists(self.config):
            config_data = {"short_term": {"refresh_time": ""}}
            with open(self.config, "w", encoding="utf-8") as config_file:
                json.dump(config_data, config_file)

    def load_short(self):
        try:
            with open(self.short_term_path, "r", encoding="utf-8") as short_mem:
                short_txt = short_mem.read()
                return short_txt if short_txt else "No previous conversations."
        except FileNotFoundError:
            with open(self.short_term_path, "w", encoding="utf-8") as f:
                f.write("")
            return "No previous conversations."
        except Exception as e:
            print(f"Error loading short term memory: {e}")
            return "No previous conversations."

    def add_short(self, data):
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.short_term_path, "a", encoding="utf-8") as short_mem:
                short_mem.write(f"\n{timestamp}\n{data}")
        except Exception as e:
            print(f"Error adding to short term memory: {e}")

    def clear_short(self):
        try:
            with open(self.short_term_path, "w", encoding="utf-8") as short_mem:
                short_mem.write("")
        except Exception as e:
            print(f"Error clearing short term memory: {e}")

    def add_refresh_time(self, duration: timedelta):
        try:
            with open(self.config, "r", encoding="utf-8") as config_file:
                config_data = json.load(config_file)

            refresh_time = (self.start_time + duration).strftime("%Y-%m-%d %H:%M:%S")
            config_data["short_term"]["refresh_time"] = refresh_time

            with open(self.config, "w", encoding="utf-8") as config_file:
                json.dump(config_data, config_file, indent=4)

            return config_data

        except FileNotFoundError:
            print("Configuration file not found.")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from configuration file: {e}")
            return {}
        except Exception as e:
            print(f"Error reading configuration file: {e}")
            return {}

    def validate_reftime(self):
        try:
            with open(self.config, "r", encoding="utf-8") as config_file:
                config_data = json.load(config_file)

            ref_time_prev = config_data["short_term"]["refresh_time"]
            ref_time_obj = datetime.strptime(ref_time_prev, "%Y-%m-%d %H:%M:%S")

            if self.start_time > ref_time_obj:
                self.clear_short()
                return True
                
            

        except FileNotFoundError:
            print("Configuration file not found.")
            return False
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from configuration file: {e}")
            return False
        except Exception as e:
            print(f"Error reading configuration file: {e}")
            return False