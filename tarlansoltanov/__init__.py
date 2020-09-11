from tarlansoltanov.login import login


def run():
    print("""Welcome Student Management Program!\n Please Login for using Student Management!""")
    info = """
    0. Exit system
    1. Login
    """
    print(info)
    operation = input("Please enter operation number : ")
    while operation != "0":
        if operation == "1":
            login()
        else:
            print("Operation number is incorrect!")
        print(info)
        operation = input("Please enter operation number : ")
    print("Thank you for using our system!")
