from tarlansoltanov.db import *
from tarlansoltanov.validations import valid_input
import tarlansoltanov.validations as valid
from tarlansoltanov.register import *


def showInfo(user, me=0):
    print("-------------------------------")
    print(
        f'ID : {user["id"]}\nName : {user["name"]}\nSurname : {user["surname"]}\nEmail : {user["email"]}')
    if me == 1:
        print(f'Password : {user["password"]}\n')


def showAllStudents():
    for student in students:
        showInfo(student)


def showStudentWithId():
    userInfo = None
    print("Please type exit for go back.\n")
    id = valid_input("id", validations=[valid.empty])
    while id != "exit":
        for i in range(len(students)):
            student = students[i]
            if str(student['id']) == id:
                userInfo = i
                break
        if userInfo != None:
            break
        print("This id is not in system.\nPlease type correct id!\n")
        id = valid_input("id", validations=[valid.empty])
    if id == "exit":
        print("----Going Back----")
        return None
    showInfo(students[userInfo])
    return userInfo


def showStudentWithEmail():
    userInfo = None
    print("Please type exit for go back.\n")
    email = valid_input("email", validations=[valid.empty])
    while email != "exit":
        for i in range(len(students)):
            student = students[i]
            if student['email'] == email:
                userInfo = i
                break
        if userInfo != None:
            break
        print("This email is not in system.\nPlease type correct email!\n")
        email = valid_input("email", validations=[valid.empty])
    if email == "exit":
        print("----Going Back----")
        return None
    showInfo(students[userInfo])
    return userInfo


def changeUser():
    info = """
    0. Exit system
    1. Change student with ID
    2. Change student with email
    """
    print(info)
    student = None
    operation = input("Please enter operation number : ")
    while operation != "0":
        if operation == "1":
            i = showStudentWithId()
        elif operation == "2":
            i = showStudentWithEmail()
        else:
            print("Operation number is incorrect!")
        if i!= None:
            userData = getUserData()
            students[i]['name'] = userData[0]
            students[i]['surname'] = userData[1]
            students[i]['email'] = userData[2]
            students[i]['password'] = userData[3]
            break
        print(info)
        operation = input("Please enter operation number : ")
    print("User Data Changed Successfully!")
    addToDb(db)


def deleteUser():
    info = """
    0. Exit system
    1. Delete student with ID
    2. Delete student with email
    """
    print(info)
    student = None
    operation = input("Please enter operation number : ")
    while operation != "0":
        if operation == "1":
            i = showStudentWithId()
        elif operation == "2":
            i = showStudentWithId()
        else:
            print("Operation number is incorrect!")
        if i!= None:
            del students[i]
            break
        print(info)
        operation = input("Please enter operation number : ")
    print("User Deleted Successfully!")
    addToDb(db)
