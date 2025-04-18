from voice_engine import VoiceEngine
from listener import Listener_Engine


def main():
    engineSP = VoiceEngine()
    
    engineSP.speak("hello i am allon ")
    command = Listener_Engine()
    query = command.take_command()
    if query.lower() == "exit":
        engineSP.speak("bye")
        exit(0)
    engineSP.speak(query)
    

if __name__ == "__main__":
    run = True
    while run:
        main()  