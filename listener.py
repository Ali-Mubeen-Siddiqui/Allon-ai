import speech_recognition as sr
from typing import Optional

class Listener_Engine:
    def __init__(self) -> None:
        self.rcg = sr.Recognizer()
        self.source = None
        # Configure recognizer settings
        self.rcg.pause_threshold = 0.8
        self.rcg.non_speaking_duration = 0.15
        self.rcg.dynamic_energy_threshold = False
        self.rcg.dynamic_energy_adjustment_damping = 0.15
        self.rcg.dynamic_energy_ratio = 1.5
        self.rcg.dynamic_energy_adjustment_ratio = 1.5
        self.setup_microphone()

    def setup_microphone(self) -> None:
        """Set up the microphone and adjust for ambient noise."""
        try:
            self.source = sr.Microphone()
            with self.source as source:
                self.rcg.adjust_for_ambient_noise(source, duration=1)
        except Exception as e:
            print(f"Error setting up microphone: {e}")
            raise

    def take_command(self) -> Optional[str]:
        """Listen for and process voice command."""
        try:
            if self.source is None:
                self.setup_microphone()

            with self.source as source:
                print("Listening.......")
                audio = self.rcg.listen(source)
                return self.recognise(audio)
        except sr.WaitTimeoutError:
            print("No speech detected")
            return None
        except Exception as e:
            print(f"Error in take_command: {e}")
            return None

    def recognise(self, audio) -> Optional[str]:
        """Recognize the audio input."""
        try:
            query = self.rcg.recognize_google(audio, language="en-in")
            print(f"[YOU]: {query}")
            return query
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None
        except Exception as e:
            print(f"Error in recognition: {e}")
            return None
