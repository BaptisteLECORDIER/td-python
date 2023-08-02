# Models/teacher.py
from .user import User

class Teacher(User):
    def __init__(self, first_name: str, last_name: str) -> None:
        super().__init__(first_name, last_name)
        self.lst_lessons = []

    def connect(self) -> None:
        input_username = input("Entrez votre nom d'utilisateur : ")
        input_password = input("Entrez votre mot de passe : ")

        if input_username == self.username and input_password == self.password:
            print("Connecté")
        else:
            print("Incorrects")
