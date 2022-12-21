import math
import os

def main():

    os.system('cls')

    print('\nTento soubor je o porovnání obdélníků!')

    # obdelnik1
    strana_a_obd1 = float(input('Zadej stranu a prvního obdélníka:'))
    strana_b_obd1 = float(input('Zadej stranu b prvního obdélníka:'))
    Obd1 = Obdelnik(strana_a_obd1, strana_b_obd1)
    # Obd1.obvod()
    # Obd1.obsah()

    # obdelnik2
    strana_a_obd2 = float(input('Zadej stranu a druhého obdélníka:'))
    strana_b_obd2 = float(input('Zadej stranu b druhého obdélníka:'))
    Obd2 = Obdelnik(strana_a_obd2, strana_b_obd2)
    # Obd2.obvod()
    # Obd2.obsah()



    # porovnání obsahu obdélníků
    Obd1.porovnejObsah(Obd2)

    # porovnání obsahu obdélníků v obráceném pořadí
    Obd2.porovnejObsah(Obd1)

    # porovnání obvodu obdélníků
    Obd1.porovnejObvod(Obd2)

    # porovnání obvodu obdélníků v obráceném pořadí
    Obd2.porovnejObvod(Obd1)
    


# třída obdélník
class Obdelnik:
    
    def __init__(self, strana_a, strana_b):
        self.strana_a = strana_a
        self.strana_b = strana_b

    def obvod(self):
        obvod = 2 * (self.strana_a + self.strana_b)
        print('\nObvod obdelníka o stranách', self.strana_a, 'a' ,self.strana_b, 'je', obvod)
        return obvod

    def obsah(self):
        obsah = self.strana_a * self.strana_b
        print("\nObsah obdelníka o stranách", self.strana_a, 'a' ,self.strana_b, 'je', obsah)
        return obsah
    
    def porovnejObsah(self, obd2):

        obsah1 = self.obsah()
        obsah2 = obd2.obsah()

        if (obsah1 > obsah2):
            print("\nObsah obdelníka o stranách", self.strana_a, "a" ,self.strana_b) 
            print("je větší než obsah druhého obdélníka o stranách", obd2.strana_a, "a" , obd2.strana_b) 

        elif (obsah1 == obsah2):
            print("\nOba obdélníky mají stejný obsah")

        else:
            print("\nObsah obdelníka o stranách", self.strana_a, "a" ,self.strana_b) 
            print("je menší než obsah druhého obdélníka o stranách", obd2.strana_a, "a" , obd2.strana_b) 

    
    def porovnejObvod(self, obd2):

        obvod1 = self.obvod()
        obvod2 = obd2.obvod()

        if (obvod1 > obvod2):
            print("\nObvod obdelníka o stranách", self.strana_a, "a" ,self.strana_b) 
            print("je větší než obvod druhého obdélníka o stranách", obd2.strana_a, "a" , obd2.strana_b) 

        elif (obvod1 == obvod2):
            print("\nOba obdélníky mají stejný obvod")

        else:
            print("\nObvod obdelníka o stranách", self.strana_a, "a" ,self.strana_b) 
            print("je menší než obvod druhého obdélníka o stranách", obd2.strana_a, "a" , obd2.strana_b) 


if __name__ == '__main__':
    main()