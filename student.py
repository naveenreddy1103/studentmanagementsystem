class Student:
    def __init__(self, name, roll_no, age, phone_no, class_name):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.phone_no = phone_no
        self.class_name = class_name

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print(f"Student with roll no {roll_no} removed successfully")
                return
        print(f"Student with roll no {roll_no} not found in classroom")

    def get_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print(f"Student found - Name: {student.name}, Roll No: {student.roll_no}, Age: {student.age}, Phone No: {student.phone_no}, Class: {student.class_name}")
                return
        print(f"Student with roll no {roll_no} not found in classroom")

    def get_all_students(self):
        for student in self.students:
            print(f"Name: {student.name}, Roll No: {student.roll_no}, Age: {student.age}, Phone No: {student.phone_no}, Class: {student.class_name}")

    def update_student(self, roll_no, name=None, age=None, phone_no=None, class_name=None):
        for student in self.students:
            if student.roll_no == roll_no:
                if name is not None:
                    student.name = name
                if age is not None:
                    student.age = age
                if phone_no is not None:
                    student.phone_no = phone_no
                if class_name is not None:
                    student.class_name = class_name
                print(f"Student with roll no {roll_no} updated successfully")
                return
        print(f"Student with roll no {roll_no} not found in classroom")

classroom = Classroom()

while True:
    print("\nChoose an option:")
    print("\t1) to add a student")
    print("\t2) to remove a student")
    print("\t3) to get a student's details")
    print("\t4) to get all students' details")
    print("\t5) to update a student's details")
    print("\t6) to exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter student roll no: ")
        age = input("Enter student age: ")
        phone_no = input("Enter student phone number: ")
        class_name = input("Enter student class(1 to 10): ")
        student = Student(name, roll_no, age, phone_no, class_name)
        classroom.add_student(student)

    elif choice == "2":
        roll_no = input("Enter student roll no to remove: ")
        classroom.remove_student(roll_no)

    elif choice == "3":
        roll_no = input("Enter student roll no to get details: ")
        classroom.get_student(roll_no)

    elif choice == "4":
        classroom.get_all_students()

    elif choice == "5":
        roll_no = input("Enter student roll no to update details: ")
        name = input("Enter new name (press enter to keep existing value): ")
        age = input("Enter new age (press enter to keep existing value): ")
        phone_no = input("Enter new phone number (press enter to keep existing value):")
        class_name = input("Enter new class(press enter to keep existing value):")
        classroom.update_student(roll_no, name=name, age=age, phone_no=phone_no, class_name=class_name)

    elif choice == "6":
        break

    else:
        print("Invalid choice")
