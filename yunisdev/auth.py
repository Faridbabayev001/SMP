from db import load_data
auth = {
    "id": "",
    "role": "",
    "loggedIn": False
}


def login(credentials):
    data= load_data()
    for i in data["students"]:
        if i["email"]==credentials['email'] and i['password']==credentials['password']:
            auth['id']=i["id"]
            auth["role"] = 'student'
            auth['loggedIn'] = True
            return True
    for i in data["admins"]:
        if i["email"]==credentials['email'] and i['password']==credentials['password']:
            auth['id']=i["id"]
            auth["role"] = 'admin'
            auth['loggedIn'] = True
            return True
    return False
    


def logged_in():
    return auth["loggedIn"]


if __name__ == "__main__":
    print('This is module file and cannot run.')
