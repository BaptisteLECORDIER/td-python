
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

        
        self.username: str = ""
        self.password: str = ""

    @abstractmethod
    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        print("Déconnexion")
