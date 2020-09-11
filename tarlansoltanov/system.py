from tarlansoltanov.func import *
from tarlansoltanov.register import *


def system(user, role):
    if role == 'student':
        studentSystem(user)
    elif role == 'admin':
        adminSystem(user)


def studentSystem(user):
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
            showStudent('id')
        elif oper == "4":
            showStudent('email')
        else:
            print("Please type correct operation!")
        print(systemInfo)
        oper = input("Please select operation : ")

    print("Logging out......")


def adminSystem(user):
    print("\nYou Logged In as Admin.")
    systemInfo = """
    0. Log out
    1. Show your account info
    2. Show all students
    3. Show student info with id
    4. Show student info with email
    5. Add student or admin
    6. Change student
    7. Delete student\n"""
    print(systemInfo)
    oper = input("Please select operation : ")
    while oper != "0":
        if oper == "1":
            showInfo(user, me=1)
        elif oper == "2":
            showAllStudents()
        elif oper == "3":
            showStudent('id')
        elif oper == "4":
            showStudent('email')
        elif oper == "5":
            register()
        elif oper == "6":
            changeUser()
        elif oper == "7":
            deleteUser()
        else:
            print("Please type correct operation!")
        print(systemInfo)
        oper = input("Please select operation : ")

    print("Logging out......")
