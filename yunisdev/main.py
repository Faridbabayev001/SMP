import methods
from auth import logged_in

if __name__ == "__main__":
    while True:
        if not logged_in():
            methods.login()
        else:
            while True:
                cmd = input('Enter command: ')
                if cmd == 'create':
                    methods.create()
                elif cmd == 'remove':
                    methods.remove()
                elif cmd == 'show':
                    methods.show()
                elif cmd == 'showall':
                    methods.showall()
                elif cmd == 'update':
                    methods.update()
                elif cmd == 'exit':
                    exit()
                else:
                    print('Command not found.')
            break