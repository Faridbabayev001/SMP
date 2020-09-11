import auth

def login():
    credentials = {data:input(f'Enter {data}: ') for data in ['email','password']}
    if auth.login(credentials):
        print('Login successfull')
    else:
        print('Try again')

def 