from db import get_last_id


class StudentSchema:
    def __init__(self, _name, _surname, _email, _password,):
        self.id = get_last_id() + 1
        self.name = _name
        self.surname = _surname,
        self.email = _email
        self.password = _password
    def __dict__(self):
        return {
            "id":self.id,
            "name":self.name,
            "surname":self.surname,
            "email":self.email,
            "password":self.password
        }

def create_student(inputs):
    st = StudentSchema()

if __name__ == "__main__":
    print('This is module file and cannot run.')
