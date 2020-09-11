from tarlansoltanov.func import *
from tarlansoltanov.register import *


def System(user, role):
    if role == 'student':
        StudentSystem(user)
    elif role == 'admin':
        AdminSystem(user)


def StudentSystem(user):
    print("\nYou Logged In as Student.")
    systemInfo = """
    0. Log out
    1. Show your account info
    2. Show all students
    3. Show student info with id
    4. Show student info with email\n"""
    print(systemInfo)
    oper = input("Please select operation : ")
    while oper != "0":
        if oper == "1":
            showInfo(user, me=1)
        elif oper == "2":
            showAllStudents()
        elif oper == "3":
            showStudentWithId()
        elif oper == "4":
            showStudentWithEmail()
        else:
            print("Please type correct operation!")
        print(systemInfo)
        oper = input("Please select operation : ")

    print("Logging out......")


def AdminSystem(user):
    print("\nYou Logged In as Admin.")
    systemInfo = """
    0. Log out
    1. Show your account info
    2. Show all students
    3. Show student info with id
    4. Show student info with email
    5. Add student
    6. Change student
    7. Delete student\n"""
    print(systemInfo)
    oper = input("Please select operation : ")
    while oper != "0":
        if oper == "1":
            showInfo(user)
        elif oper == "2":
            showAllStudents()
        elif oper == "3":
            showStudentWithId()
        elif oper == "4":
            showStudentWithEmail()
        elif oper == "5":
            Register()
        elif oper == "6":
            changeUser()
        elif oper == "7":
            deleteUser()
        else:
            print("Please type correct operation!")
        print(systemInfo)
        oper = input("Please select operation : ")

    print("Logging out......")
