from abc import ABC, abstractmethod
import requests
import json
from openai import OpenAI


class Communicator(ABC):

    @abstractmethod
    def request(self, text: str):
        pass
