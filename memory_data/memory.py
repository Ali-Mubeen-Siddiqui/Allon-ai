import os
from datetime import datetime

class Memory:
    def __init__(self) -> None:
        self.BASE_URL = os.getcwd()
        self.short_term_path = os.path.join(self.BASE_URL,"memory_data/shortTerm.txt")
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(self.short_term_path), exist_ok=True)
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.clear_short()
        # Create file if it doesn't exist
        if not os.path.exists(self.short_term_path):
            with open(self.short_term_path, "w", encoding="utf-8") as f:
                f.write("")
        
    def load_short(self):
        try:
            with open(self.short_term_path, "r", encoding="utf-8") as short_mem:
                short_txt = short_mem.read()
                return short_txt if short_txt else "No previous conversations."
        except FileNotFoundError:
            # Create the file if it doesn't exist
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
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.short_term_path, "w", encoding="utf-8") as short_mem:
                short_mem.write("")
        except Exception as e:
            print(f"Error adding to short term memory: {e}")
        