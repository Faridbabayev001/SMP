import auth

def getInput(*datas):
    return {data:input(f'Enter {data}: ') for data in datas}

def login():
    credentials = getInput('email','password')
    if auth.login(credentials):
        print('Login successfull')
    else:
        print('Try again')

def create():
    pass

def remove():
    pass

def show():
    pass

def showall():
    pass

def update():
    pass
