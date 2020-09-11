from tarlansoltanov.db import *
from tarlansoltanov.validations import valid_input, checkexit
import tarlansoltanov.validations as valid
from tarlansoltanov.system import System


def login():
    print("--------Login--------")
    user = getUserData()
    if user != None:
        system(*user)


def getUserData():
    userInfo = None
    print("Please type exit for exit login.\n")
    email = valid_input("email", validations=[valid.empty])
    while email != "exit":
        for student in students:
            if student['email'] == email:
                userInfo = student
                role = 'student'
                break
        for admin in admins:
            if admin['email'] == email:
                userInfo = admin
                role = 'admin'
                break
        if userInfo != None:
            break
        print("This email is not in system.\nPlease type correct email!\n")
        email = valid_input("email", validations=[valid.empty])
    if checkexit(email, "exit") == -1:
        return None
    password = valid_input("password", validations=[valid.empty])
    while password != "exit":
        if userInfo['password'] == password:
            return [userInfo, role]
            break
        print("This password is not in correct.\nPlease type correct password!\n")
        password = valid_input("password", validations=[
                               valid.empty, valid.password])
    if checkexit(password, "exit") == -1:
        return None
