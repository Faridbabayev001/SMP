from tarlansoltanov.db import *
from tarlansoltanov.login import *
from tarlansoltanov.validations import valid_input, checkexit
import tarlansoltanov.validations as valid


def register():
    log = getUserType()
    if log != -1:
        print("User registered succesfully!")


def getUserData():
    print("Please type exit for go back.\n")
    name = valid_input("name", validations=[valid.empty, valid.alphabetic])
    if checkexit(name, "exit") == -1:
        return None
    surname = valid_input("surname", validations=[
                          valid.empty, valid.alphabetic])
    if checkexit(surname, "exit") == -1:
        return None
    email = valid_input("email", validations=[valid.empty, valid.email])
    if checkexit(email, "exit") == -1:
        return None
    password = valid_input("password", validations=[
                           valid.empty, valid.password])
    if checkexit(password, "exit") == -1:
        return None
    password_confirm = valid_input(
        "confirm password", validations=[valid.empty, valid.password])
    if checkexit(password_confirm, "exit") == -1:
        return None
    while password != password_confirm:
        print("Password and confirm password must be same!\n")
        password = valid_input("password", validations=[
                               valid.empty, valid.password])
        if checkexit(password, "exit") == -1:
            return None
        password_confirm = valid_input(
            "confirm password", [valid.empty, valid.password])
        if checkexit(password_confirm, "exit") == -1:
            return None
    return [name, surname, email, password]


def getUserType():
    print("--------Register--------")
    typeInfo = """
    0. Go back
    1. Student
    2. Admin\n"""
    print(typeInfo)
    type = input("Please select user type : ")
    while type != "0":
        if type == "1" or type == "2":
            userInfo = getUserData()
            if userInfo == None:
                break
            elif type == "2":
                userInfo.append('admin')
            User(*userInfo).dictToDb()
            print("User added to system succesfully!\n")
            break
        else:
            print("Please type valid user type number!")
        print(typeInfo)
        type = input("Please select user type : ")
    if checkexit(type, "0") == -1:
        return -1
    if checkexit(userInfo, None) == -1:
        return -1
