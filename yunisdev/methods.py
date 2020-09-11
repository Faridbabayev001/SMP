import auth
import student
import db
from tabulate import tabulate

def getInput(*datas, asDict=True):
    if asDict:
        return {data: input(f'Enter {data}: ') for data in datas}
    else:
        return [input(f'Enter {data}: ') for data in datas]


def login():
    credentials = getInput('email', 'password')
    if auth.login(credentials):
        print('Login successfull')
    else:
        print('Try again')


def create(authRole):
    if authRole == "admin":
        data = getInput('name', 'surname', 'email', 'password',asDict=False)
        student.create_student(data)
    else:
        print('You do not have permission to do this operation')


def remove(authRole):
    if authRole == "admin":
        data = getInput('id')
        student.remove_student(data["id"])
    else:
        print('You do not have permission to do this operation')

def show():
    data = getInput('id')
    student.get_student(data["id"])


def showall():
    student.get_all()


def update(authRole):
    if authRole == "admin":
        data = getInput('id')
        st = student.get_student_data(data["id"])
        changeData = getInput("id","name","surname","email","password")
        student.update_student(st)
    else:
        print('You do not have permission to do this operation')

def print_as_table(tabledata,head=["ID","Name","Surname","Email","Password"]):
    print(tabulate(tabledata, headers=head))