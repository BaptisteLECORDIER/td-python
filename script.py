from Models.student import Student
from Models.teacher import Teacher
import json

with open("data/students.json", "r") as file:
    students_data = json.load(file)

students = []
for student_data in students_data:
    student = Student(student_data["first_name"], student_data["last_name"])
    student.rates = student_data["rates"]
    student.average_student = student_data["average_student"]
    student.username = student_data["username"]
    student.password = student_data["password"]
    students.append(student)

with open("data/teachers.json", "r") as file:
    teachers_data = json.load(file)

teachers = []

for teacher_data in teachers_data:
    teacher = Teacher(teacher_data["first_name"], teacher_data["last_name"])
    teacher.lst_lessons = teacher_data["lst_lessons"]
    teacher.username = teacher_data["username"]
    teacher.password = teacher_data["password"]
    teachers.append(teacher)

persons = students + teachers

for person in persons:
    print(f"{person.first_name} {person.last_name} : ", end="")
    
    input_username = input("Entrez votre nom d'utilisateur : ")
    input_password = input("Entrez votre mot de passe : ")
    
    if input_username == person.username and input_password == person.password:
        person.connect()

        if isinstance(person, Student):
            print("Connecté en tant qu'élève")
            
            new_rates = []
            for i in range(5):
                while True:
                    try:
                        rate = int(input(f"Entrez la note {i + 1} sur 20 : "))
                        if 0 <= rate <= 20:
                            new_rates.append(rate)
                            break
                        else:
                            print("La note doit être comprise entre 0 et 20.")
                    except ValueError:
                        print("Veuillez entrer un nombre valide.")
            
            person.rates = new_rates
            person.average_student = sum(new_rates) / len(new_rates)
            print(f"Moyenne des notes : {person.average_student:.2f}")

        elif isinstance(person, Teacher):
            print("Connecté en tant qu'enseignant")

            person.lst_lessons = [] 

            while True:
                lesson = input("Entrez une matière enseignée (ou 'stop' pour terminer) : ")
                if lesson.lower() == "stop":
                    break
                person.lst_lessons.append(lesson)

            print("Matières mises à jour :", person.lst_lessons)

        person.disconnect()
    else:
        print("Identifiants incorrects")

updated_students_data = []
for student in students:
    student_data = {
        "first_name": student.first_name,
        "last_name": student.last_name,
        "rates": student.rates,
        "average_student": student.average_student,
        "username": student.username,
        "password": student.password,
    }
    updated_students_data.append(student_data)

with open("data/students.json", "w") as file:
    json.dump(updated_students_data, file, indent=4)

updated_teachers_data = []
for teacher in teachers:
    teacher_data = {
        "first_name": teacher.first_name,
        "last_name": teacher.last_name,
        "lst_lessons": teacher.lst_lessons,
        "username": teacher.username,
        "password": teacher.password,
    }
    updated_teachers_data.append(teacher_data)

with open("data/teachers.json", "w") as file:
    json.dump(updated_teachers_data, file, indent=4)

