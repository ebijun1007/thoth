import os

from colorama import Fore
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.completion.filesystem import PathCompleter

from thoth.enums.mode import Mode
from thoth.utils.logs import Logger

logger = Logger()

class BooksCompleter(Completer):
    def __init__(self, directory):
        self.directory = directory

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        for filename in os.listdir(self.directory):
            if filename.startswith(text):
                yield Completion(filename, start_position=-len(text))

def clean_input(message: str, completer: Completer = None):
    try:
        return prompt(message, completer=completer)
    except KeyboardInterrupt:
        print("Quitting...")
        exit(0)

def input_mode():
    completer = WordCompleter([e.value for e in Mode])
    logger.typewriter_log(
        "Choose a mode 'Focus' or 'Explore'.", Fore.GREEN
    )
    logger.typewriter_log(
        "    Focus: Deeply engage with one book.", Fore.YELLOW
    )
    logger.typewriter_log(
        "    Explore: Find insights from past reads", Fore.YELLOW
    )
    mode = clean_input(f"{'/'.join([e.value for e in Mode])}: ", completer=completer)
    return mode

def input_book():
    completer = BooksCompleter("books")
    logger.typewriter_log(
        "Select a book to read", Fore.GREEN
    )
    book = clean_input('book: ', completer=completer)
    return book

