#Initialize empty list and dictionary
student_list = []
student_dict = {}

# Addin student information
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
grade = input("Enter student's grade: ")

student_list.append(name)
student_dict[name] = {'age': age, 'grade': grade}
print("Student information added successfully!")

# To display all student information
print("Student's detail: ")
for name, info in student_dict.items():
        print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")

# to search for a student
student_search = input("Enter the name of student to search or simply enter  to skip: ")    
if name in student_dict:
    info = student_dict[name]
    print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
else:
    print("Student not found.")

# to remove a student
student_remove = input("Enter the name of student to remove or simply enter to skip: ")
if name in student_dict:
    student_list.remove(name)
    del student_dict[name]
    print("Student removed successfully.")
else:
    print("Student not found.")