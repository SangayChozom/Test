class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number
    
    def walk(self):
        print(f"{self.name} is walking.")
    
    def talk(self):
        print(f"{self.name} is talking.")
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")
    
    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")
    
    def grade_students(self):
        print(f"{self.name} is grading students.")

class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.marks = []
    
    def study(self):
        print(f"{self.name} is studying.")
    
    def attend_class(self):
        print(f"{self.name} is attending class.")
    
    def write_exam(self):
        print(f"{self.name} is writing an exam.")
    
    def calculate_gpa(self):
        if not self.marks:
            return "No marks available"
        total_marks = sum(self.marks)
        num_subjects = len(self.marks)
        return total_marks / num_subjects

# Creating objects
teacher1 = Teacher("Pema", 35, "123456", "Math", 45000, "ECE Department", "HOD")
student1 = Student("Sherab", 20, "789012", "S12345", "CSF", 2)

# Accessing specific behaviors and attributes
teacher1.teach()
teacher1.grade_students()
teacher1.attend_meeting()

student1.study()
student1.attend_class()
student1.write_exam()

# Accessing common behaviors
teacher1.walk()
teacher1.talk()
teacher1.eat()
teacher1.sleep()

student1.walk()
student1.talk()
student1.eat()
student1.sleep()