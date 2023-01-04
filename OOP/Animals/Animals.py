import os
from Dog import *

def main():

    os.system('cls')
    print()
    print('This code is about ANIMALS!')
    
    # young Alik
    Alik = MyCuteDog('Alík','Voříšek', 1)
    Alik.show_dog()
    Alik.make_noice(5)
    Alik.how_old()
    Alik.be_cute()

    # adult Azor
    Azor = MyAngryDog('Azor','Vlčák', 10)
    Azor.show_dog()
    Azor.make_noice(2)
    Azor.how_old()
    Azor.be_angry(3)

    # retired Prcek
    Prcek = MyDog('Prcek','Čivava', 12)
    Prcek.show_dog()
    Prcek.make_noice(1)
    Prcek.how_old()



if __name__ == '__main__':
    main()