import speech_recognition as sr

class Listener_Engine:
    def __init__(self) -> None:
        self.rcg = sr.Recognizer()
        self.rcg.pause_threshold = 0.8
        self.rcg.non_speaking_duration = 0.15
        self.rcg.dynamic_energy_threshold = False
        self.rcg.dynamic_energy_adjustment_damping = 0.15
        self.rcg.dynamic_energy_ratio = 1.5
        self.rcg.dynamic_energy_adjustment_ratio = 1.5

    def take_command(self):
        with sr.Microphone() as source:
            self.rcg.adjust_for_ambient_noise()
            print("Listening.......")
            self.audio = self.rcg.listen(source)
            return self.recognise()

    def recognise(self):
        try:
            self.query = sr.recognize_google(self.audio,language="en-in")
            print(f"[YOU]: {self.query}")
            return self.query
        except Exception as e:
            return "[Allon]: Sorry an error occured"