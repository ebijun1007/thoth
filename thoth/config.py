"""Configuration class to store the state of bools for different scripts access."""
import os

from colorama import Fore
from dotenv import load_dotenv

from thoth.singleton import Singleton

load_dotenv(verbose=True)


class Config(metaclass=Singleton):
    """
    Configuration class to store the state of bools for different scripts access.
    """

    def __init__(self) -> None:
        """Initialize the Config class"""
        self.speak_mode = False
        self.shelf_file = os.getenv("SHELF_FILE", "shelf.yaml")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.book = ""

    def set_speak_mode(self, value: bool) -> None:
        """Set the speak mode value."""
        self.speak_mode = value

    def set_mode(self, value: str) -> None:
        """Set the mode value."""
        self.mode = value

    def set_book(self, value: str) -> None:
        """Set the book value."""
        self.book = value

    def set_openai_api_key(self, value: str) -> None:
        """Set the OpenAI API key value."""
        self.openai_api_key = value

def check_openai_api_key() -> None:
    """Check if the OpenAI API key is set in config.py or as an environment variable."""
    cfg = Config()
    if not cfg.openai_api_key:
        print(
            Fore.RED
            + "Please set your OpenAI API key in .env or as an environment variable."
        )
        print("You can get your key from https://platform.openai.com/account/api-keys")
        exit(1)

def create_config(
    speak: bool,
    mode: str,
    book: str,
) -> None:
    cfg = Config()
    cfg.set_speak_mode(speak)
    cfg.set_mode(mode)
    cfg.set_book(book)
