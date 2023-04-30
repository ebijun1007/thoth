from colorama import Fore, Style

from thoth.config import Config
from thoth.utils.spinner import Spinner

from langchain.memory import ChatMessageHistory
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

class Agent:
    def __init__(
        self,
    ):
        cfg = Config()

    def start_interaction_loop(self):
        # Interaction Loop
        cfg = Config()

        while True:
            # Send message to AI, get response
            with Spinner("Thinking... "):
                pass