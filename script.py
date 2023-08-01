# Importation des modules Students, Teachers et json

from Models.student import Student
from Models.teacher import Teacher
import json


# Ouverture du fichier json student

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
    print(f"{person.first_name} {person.last_name} ", end="")
    person.connect()
    person.disconnect()

