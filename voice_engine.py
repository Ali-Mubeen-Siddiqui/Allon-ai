import pyttsx3
from typing import Optional
import re

class VoiceEngine:
    def __init__(self, volume: float = 1.0, rate: int = 200) -> None:
        """
        Initialize the voice engine with configuration settings.
        
        Args:
            volume (float): Voice volume between 0.0 and 1.0
            rate (int): Words per minute
        """
        self.engine = pyttsx3.init()
        self.set_volume(volume)
        self.set_rate(rate)

    def set_volume(self, volume: float) -> None:
        """Set the voice volume."""
        if not 0.0 <= volume <= 1.0:
            raise ValueError("Volume must be between 0.0 and 1.0")
        self.engine.setProperty('volume', volume)

    def set_rate(self, rate: int) -> None:
        """Set the speech rate in words per minute."""
        if rate < 0:
            raise ValueError("Rate must be a positive number")
        self.engine.setProperty('rate', rate)

    def speak(self, text: str) -> None:
        """
        Speak the given text and print it.
        
        Args:
            text (str): The text to be spoken
        """
        try:
            text = self.filter_response(text)
            self.engine.say(text)
            print(f"[ALLON]: {text}")
            self.engine.runAndWait()
        except Exception as e:
            print(f"An error occurred while speaking: {e}")

    def get_volume(self) -> float:
        """Get the current volume setting."""
        return self.engine.getProperty('volume')

    def get_rate(self) -> int:
        """Get the current speech rate."""
        return self.engine.getProperty('rate')
    

    def filter_response(self, text):
        # Remove any text between <thinking> and </thinking> tags
        filtered_text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
        return filtered_text.strip()