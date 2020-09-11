import json.encoder
import auth
import methods

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

def get_student_from_db(_id):
    tableData = []
    data = load_data()["students"]
    for i in data:
        if i["id"]==int(_id):
            if auth.auth["role"]=="admin":
                tableData.append([i["id"],i["name"],i["surname"],i["email"],i["password"]])
            elif auth.auth["id"]==i["id"]:
                tableData.append([i["id"],i["name"],i["surname"],i["email"],i["password"]])
            else:
                tableData.append([i["id"],i["name"],i["surname"],i["email"],"<hidden>"])
    methods.print_as_table(tableData)
    
def get_students_from_db():
    tableData = []
    data = load_data()["students"]
    for i in data:
        if auth.auth["role"]=="admin":
            tableData.append([i["id"],i["name"],i["surname"],i["email"],i["password"]])
        elif auth.auth["id"]==i["id"]:
            tableData.append([i["id"],i["name"],i["surname"],i["email"],i["password"]])
        else:
            tableData.append([i["id"],i["name"],i["surname"],i["email"],"<hidden>"])
    methods.print_as_table(tableData)

def get_student_data_from_db(_id):
    data = load_data()["students"]
    for i in data:
        if i["id"]==int(_id):
            return i

def update_student_on_db(st):
    data = load_data()
    for i in range(len(data["students"])):
        if data["students"][i]["id"]==st["id"]:
            data["students"][i] = st
    save_data(data)
    print('Updated student')

if __name__ == "__main__":
    print('This is module file and cannot run.')