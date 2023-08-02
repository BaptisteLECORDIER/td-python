# Models/student.py
from .user import User

class Student(User):
    def __init__(self, first_name: str, last_name: str) -> None:
        super().__init__(first_name, last_name)
        self.rates = []
        self.average_student = 0

    def connect(self) -> None:
        input_username = input("Nom d'utilisateur : ")
        input_password = input("Mot de passe : ")

        if input_username == self.username and input_password == self.password:
            print("Étudiant connecté")
        else:
            print("Identifiants incorrects")


