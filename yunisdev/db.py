import json
from tabulate import tabulate

data = None
dataFile = 'db.json'

def load_data():
    with open(dataFile,'rt') as source:
        return json.load(source)

def save_data(data):
    with open(dataFile,'wt') as source:
        json.dump(data, source)

def show_data(auth):
    pass

def get_last_id():
    data = load_data()
    last_student = data["students"][-1]
    return last_student["id"]

def add_student_to_db(d):
    data = load_data()
    data["students"].append(d)
    save_data(data)
    print('Successfully added user to db')

def remove_student_from_db(_id):
    data = load_data()
    data["students"] = [st for st in data["students"] if not st["id"]==int(_id)]
    save_data(data)
    print('Successfully deleted user')

if __name__ == "__main__":
    print('This is module file and cannot run.')