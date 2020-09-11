import json

db = {}
with open("db.json") as d:
    db = json.load(d)

students = db['students']
admins = db['admins']


def addToDb(db):
    with open("db.json", "w") as f:
        json.dump(db, f)
    students = db['students']
    admins = db['admins']


class User:
    def __init__(self, name, surname,  email, password, role='student'):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.role = role

    def dictToDb(self):
        myDict = dict()
        myDict['name'] = self.name
        myDict['surname'] = self.surname
        myDict['email'] = self.email
        myDict['password'] = self.password
        if self.role == 'student':
            myDict['id'] = students[len(students)-1]['id']+1
            students.append(myDict)
        else:
            myDict['id'] = admins[len(admins)-1]['id']+1
            admins.append(myDict)
        addToDb(db)
