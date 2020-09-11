import auth
import student
import db

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


def create():
    data = getInput('name', 'surname', 'email', 'password',asDict=False)
    student.create_student(data)


def remove():
    data = getInput('id')
    student.remove_student(data["id"])

def show():
    pass


def showall():
    pass


def update():
    pass
