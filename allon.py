from listener import ListenerEngine
from voice_engine import VoiceEngine
# importing main ai core logic 
from core import Core
import os



class Allon:
    def __init__(self) -> None:
        self.run = True
        self.voice = VoiceEngine()
        self.listener = ListenerEngine()
        self.voice.speak("Hey ,I am Allon how may i assist you today.")

        # loading data files
        self.train_dir = self.load_data_folder()
        self.main_train_data = os.path.join(self.train_dir,"main.txt")
        try:
            self.ai_main = Core(self.main_train_data)
        except Exception as e:
            print(e)

    def mainloop(self):
        while self.run:
            anomaly = self.cycle()
            if anomaly is None:
                continue

            if anomaly == "exit":
                self.run = False
    
    def cycle(self):
        query = self.listener.take_command()
        if query is None:
            return None
        if query.lower() == "exit":
            return "exit"
        
        response = self.ai_main.get_response(query)

        self.voice.speak(response)


    def load_data_folder(self):
        try:
            BASE_URL = os.getcwd()
            folder_dir = os.path.join(BASE_URL,"training_data")
            return folder_dir
        except Exception as e:
            print(e)
            exit(0)
            

            

