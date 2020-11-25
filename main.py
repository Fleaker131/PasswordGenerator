import generator as gr


class pwdgod:

    def creategod(self):
        desing = """
        *********************
           Password Creator
        *********************
        """
        print(desing)
        while True:
            try:
                length = int(input("Password Length : "))
                while not length:
                    length = int(input("Password Length : "))
                number = int(input("Password Number : "))
                while not number:
                    number = int(input("Password Number : "))
                gr.creator(length=length, number=number)
            except ValueError:
                print("Error : Please enter a value ")
                input("Press The Any Key")


if __name__ == '__main__':
    startgod = pwdgod()
    startgod.creategod()
