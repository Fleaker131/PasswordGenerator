import random

lowercases = "abcdefghijklmnopqrstuvwxyz"
uppercases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]?;,*/(){}%#$£@!_=-"


def creator(length, number):
    try:
        print("***** Passwords Generated *****")
        for a in range(1, number):
            allcreator = lowercases + uppercases + numbers + symbols
            password = "".join(random.sample(allcreator, length))
            print("({0})".format(int(a)), "{0}".format(password))
    except ValueError:
        print("Error !")
    finally:
        quit()