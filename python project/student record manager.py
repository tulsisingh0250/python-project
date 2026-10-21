import json
File="student.txt"
def load_student():
    try:
        with open("File","r")as file:
            student=json.load(file)
            return student
    except FileNotFoundError:
        return[]
def write_student(students):
    with open("File","w")as file:
        json.dump(students,file,indent=3)

students=load_student()
while True:
    print("student record")
    print("1. Add a student")
    print("2. view a student")
    print("3. Exit")
    choice=input("enter your choice:(1/2/3): ")
    if choice=="1":
        name=input("enter your name:")
        age=int(input("enter your age: "))
        marks=int(input("enter your marks:"))
        student={
            "Name":name,
            "Age":age,
            "Marks":marks
        }
        students.append(student)
        write_student(students)
        print("student record completed successfully")
    elif choice=="2":
        if len(students)==0:
            print("not record found")
        else:
            print("/n----All student record-----")
            for student in students:
                print("Name:",student["Name"])
                print("Age:",student["Age"])
                print("Marks:",student["Marks"])
                print("------------------")
    elif choice=="3":
        print("Exit")
        break
    else:
        print("invalid choice")
            




