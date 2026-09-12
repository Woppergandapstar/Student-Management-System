class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name} ,Age : {self.age}") 

class Student(Person):
        School_name = "ABC School"

        def __init__(self, name, age,class_name,roll,marks = 0):
            super().__init__(name, age)

            self.class_name = class_name
            self.roll = roll
            self.__marks = 0
            self.set_marks(marks)

        #setter method    
        def set_marks(self,marks):

            if 0 <= marks <= 100:
                 self.__marks = marks
            else:
                 print('Invalid marks! Marks must be between 0 to 100')

        #getter method
        def get_marks(self):
             return self.__marks 

        def grade(self):

            if 80 <= self.__marks <= 100:
                return "A+"

            elif 70 <= self.__marks <= 79:
                return "A"

            elif 65 <= self.__marks <= 69:
                return "A-"

            elif 60 <= self.__marks <= 64:
                return "B+"

            elif 55 <= self.__marks <= 59:
                return "B"

            elif 50 <= self.__marks <= 54:
                return "C+"

            elif 40 <= self.__marks <= 49:
                return "C"

            else:
                return "Fail"
def show_info(self):
            super().show_info() 
            print(f"Class: {self.class_name}")   
            print(f"Roll: {self.roll}")  
            print(f"Marks: {self.__marks}")  
            print(f"Grade: {self.grade()}")

class Teacher(Person):

    def __init__(self ,name,age,subject):
        super().__init__(name, age)

        self.subject = subject

    def show_info(self):

        super().show_info()

        print(f"Subject: {self.subject}")




class Admin(Teacher):
    def add_student(self,student_list, student):
        student_list.append(student)
        print(f"(student.name) added succesfully")

    def remove_student(self,student_list,roll):
        for s in student_list:
            if s.roll == roll:
                student_list.remove(s)
                print("uh miss stopped")
        

    def update_marks(self,student_list,roll,new_marks):
        for s in student_list:
            if s.roll == roll:
                s.set_marks(new_marks)
                print("Marks updated successfully")
                break
            else:
                print("Student not found")


Students = []

admin1 = Admin('Paris',50,'algorithm')

while True:
    print('\n --Student Management--')
    print("1. Add Student")
    print("2. Show All Students")
    print("3.Update Student Marks")
    print("4.Remove Student")
    print("5.Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Student Name: ")
        age = int(input("Student Age:"))
        class_name = input("Class: ")
        roll = int(input("Student Roll"))
        marks = int(input("Student Marks"))


        st = Student(name,age,class_name,roll,marks)
        admin1.add_student(Students,st)

    elif choice == '2':
        if len(Students) == 0:
            print("No student found")
        else:
            for s in Students:
                print("\n --Student Info--")
                s.show_info()

    elif choice == "3":
        roll = int(input("Enter Rolls:"))
        new_marks = int(input("Enter new marks:"))

        admin1.update_marks()

    elif choice == '4':
        roll = int(input("Enter Roll to remove:"))

    elif choice == '5':
        print("system closed")
        break
    
    else:
        print("Invalid choice")



