"""write a python program for the addtion of odd elements of a square matrix whose i and j values are same"""
'''i=0;
j=0;
s=1;
l=[[1,2,3],[2,6,4],[3,4,5]]
for i in range(len (l)):
    for j in range(len (l)):
        if l[i][j]%2!=0:
            if(i==j):
                s=s+l[i][j];  
print(s)            
            
'''

class Student:
    def __init__(self, name, age, gmail):
        self.name = name
        self.age = age
        self.gmail = gmail

def add_student(student_list):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    gmail = input("Enter student Gmail address: ")

    student = Student(name, age, gmail)
    student_list.append(student)
    print("Student added successfully!")

def display_students(student_list):
    print("\nStudent Details:")
    for index, student in enumerate(student_list, start=1):
        print(f"Student {index}:")
        print("Name:", student.name)
        print("Age:", student.age)
        print("Gmail:", student.gmail)
        print()

def main():
    students = []

    while True:
        print("\nOptions:")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()

    




