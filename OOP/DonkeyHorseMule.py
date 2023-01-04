import os

def main():
    os.system('cls')
    print('----------------------------------------------------')
    print('This code is about ANIMALS - horse, donkey and mule!')
    print('----------------------------------------------------')

    Jerry = Donkey()
    Alice = Horse()
    Baby = Mule()

    Jerry.who_am_I()
    Alice.who_am_I()
    Baby.who_am_I()

class Horse:

    def __init__(self):
        pass

    def who_am_I(self):
        print()
        print("I am HORSE")

class Donkey:

    def __init__(self):
        pass

    def who_am_I(self):
        print()
        print("I am DONKEY")

class Mule(Donkey, Horse):
    
    def who_am_I(self):
        super().who_am_I()
        Horse.who_am_I(self)


if __name__ == '__main__':
    main()

