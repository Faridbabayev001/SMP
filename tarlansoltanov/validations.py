from tarlansoltanov.db import *
import re


def empty(txt):
    if txt:
        return True
    print("This field can't be empty!\n")
    return False


def alphabetic(txt):
    if txt.isalpha():
        return True
    print("Please use only alphabetical characters\n")
    return False


def numeric(txt):
    if txt.isdigit():
        return True
    print("Please use only numerical characters\n")
    return False


def email(email):
    x = re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
    if x == None:
        print("Please enter valid email!\n")
        return False
    for student in students:
        if student['email'] == email:
            print("This email exists. Please try again.\n")
            return False
    for admin in admins:
        if admin['email'] == email:
            print("This email exists. Please try again.\n")
            return False
    return True


def password(password):
    check = re.fullmatch('[A-Za-z0-9@#$%^&+=]{8,}', password)
    if check == None:
        print("Please enter valid password!\n")
        return False
    return True


def valid(txt, args):
    for elem in args:
        if(elem(txt) == False):
            return False
    return True


def valid_input(out, validations=[]):
    txt = input(f'{out.capitalize()} : ')
    if txt == 'exit':
        return 'exit'
    while valid(txt, validations) == False:
        txt = input(f'{out.capitalize()} : ')
    return txt


def checkexit(txt, x):
    if txt == x:
        print("----Going Back----")
        return -1
