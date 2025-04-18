from voice_engine import VoiceEngine


def main():
    engineSP = VoiceEngine()
    
    engineSP.speak("hello i am allon ")
    

if __name__ == "__main__":
    run = True
    while run:
        main()  