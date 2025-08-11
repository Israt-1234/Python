
import json

class Person:
    def __init__(self, name:str, age:int, address:str):
        self.name = name
        self.age = age
        self.address = address
    def display_person_info(self):
        print(f"Name: {self.name}, age: {self.age}, address: {self.address}")

class Student(Person):
    def __init__(self, name:str, age:int, address:str, student_id:int):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject:str, grade:str):
        self.grades[subject] = grade

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def display_student_info(self):
        super().display_person_info()
        print(f"Student ID: {self.student_id}, Grades: {self.grades}, Courses: {self.courses}")

        
class Course():
    def __init__(self, course_name:str, course_code:str, instructor:str):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []
    def add_student(self, student: Student):
        if student not in self.students:
            self.students.append(student)
    def display_course_info(self):
        print(f"Course Name: {self.course_name}, Course Code: {self.course_code}, Instructor: {self.instructor}")
        print("Enrolled Students:")
        for student in self.students:
            student.display_student_info()



students = {}
courses = {}


def save_data():
    data = {
        "students":{
            student_id:{
                "name": student.name,
                "age": student.age,
                "address": student.address,
                "grades": student.grades,
                "courses": student.courses
            }
            for student_id, student in students.items()
        },
        "courses":{
            course_code:{
                "course_name": course.course_name,
                "course_code": course.course_code,
                "instructor": course.instructor,
                "students": [student.student_id for student in course.students]
            }
            for course_code, course in courses.items()
        }

    }
    with open('data.json', 'w')as file:
        json.dump(data, file, indent=4)
    print("all students and courses data saved successfully")


def load_data():
    global students, courses
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return data

    except Exception as e:
        print("not found file")






def menu():

    while True:
        print("\nStudent Management System")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student details")
        print("6. Display Course details")
        print("7. Save data to file")
        print("8. load data from file")
        print("9. Exit")

        choice = input("select an option: ")

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            address = input("Enter student address: ")
            student_id = int(input("Enter student ID: "))
            if student_id not in students:
                students[student_id] = Student(name, age, address, student_id)
                print(f"Student {name} (Id: {student_id}) added successfully.")
            else:
                print(f"Student with ID {student_id} already exists.")
        elif choice == '2':
            Course_name = input("Enter course name: ")
            Course_code = input("Enter course code: ")
            instructor = input("Enter instructor name: ")
            if Course_code not in courses:
                courses[Course_code] = Course(Course_name, Course_code, instructor)
                print(f"Course {Course_name} (Code: {Course_code}) Created with instructor {instructor}.")
            else:
                print(f"Course with code {Course_code} already exists.")
        elif choice == '3':
            student_id  = int(input("Enter student ID to enroll: "))
            course_code = input("Enter course code to enroll in: ")
            if student_id in students and course_code in courses:
                students[student_id].enroll_course(courses[course_code].course_name)
                courses[course_code].add_student(students[student_id])
                print(f"Student {students[student_id].name} enrolled in course {courses[course_code].course_name}.")
            else:
                print("Invalid student ID or course code.")
        elif choice == '4':
            student_id = int(input("Enter student ID to add grade: "))
            course_code = input("Enter course code: ")
            grade = input("Enter grade: ")
            if student_id in students and course_code in courses:
                students[student_id].add_grade(course_code, grade)
                print(f"Grade {grade} added for student {students[student_id].name} in course {course_code}.")
            else:
                print("Invalid student ID or course code.")
        elif choice == '5':
            student_id = int(input("Enter student ID to display details: "))
            if student_id in students:
                students[student_id].display_student_info()
            else:
                print("Invalid student ID.")
        elif choice == '6':
            course_code = input("Enter course code to display details: ")
            if course_code in courses:
                courses[course_code].display_course_info()
            else:
                print("Invalid course code.")
        elif choice == '7':
            save_data()
        elif choice == '8':
            print(load_data())
            print("Data loaded successfully.")
        else:
            print("exit")
            break

if __name__ == "__main__":
    menu()
