from db import get_last_id, add_student_to_db, remove_student_from_db


class StudentSchema:
    def __init__(self, _name, _surname, _email, _password,):
        self.id = get_last_id() + 1
        self.name = _name
        self.surname = _surname
        self.email = _email
        self.password = _password
    def getDict(self):
        return {
            "id":self.id,
            "name":self.name,
            "surname":self.surname,
            "email":self.email,
            "password":self.password
        }

def create_student(inputs):
    st = StudentSchema(*inputs)
    add_student_to_db(st.getDict())

def remove_student(_id):
    remove_student_from_db(_id)

if __name__ == "__main__":
    print('This is module file and cannot run.')
