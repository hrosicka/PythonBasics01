import math

def main():

    print('\nTento soubor je o porovnání čtverců!')

    # ctverec1
    strana_ctverec1 = float(input('\nZadej stranu prvního čtverce: '))
    Ctverec1 = Ctverec(strana_ctverec1)
    Ctverec1.obvod()
    Ctverec1.obsah()

    # ctverec2
    strana_ctverec2 = float(input('\nZadej stranu druhého čtverce: '))
    Ctverec2 = Ctverec(strana_ctverec2)
    Ctverec2.obvod()
    Ctverec2.obsah()

    # porovnání čtverců
    Ctverec1.porovnej(Ctverec2)

    # porovnání čtverců v obráceném pořadí
    Ctverec2.porovnej(Ctverec1)
    


# třída čtverec
class Ctverec:
    """ 
    Třída pro vytvoření a získání vlastností čtverce

    Metody počítají obvod, obsah a porovnávají 2 čtverce

    Výsledkem je výpis do konzole
    """
    
    def __init__(self, strana_a):
        """
        Konstruktor čtverce - parametrem je strana a v centimetrech
        """
        self.strana_a = strana_a

    def obvod(self):
        """
        Metoda pro výpočet obvodu čtverce v centimetrech

        Obvod čtverce: o = 4*a
        """
        obvod = 4 * self.strana_a
        print('Obvod čtverce o straně', self.strana_a, 'je', obvod)

    def obsah(self):
        """
        Metoda pro výpočet obsahu čtverce v centimetrech

        Obsah čtverce: S = a^2
        """
        obsah = math.pow(self.strana_a, 2)
        print('Obsah čtverce o straně', self.strana_a, 'je', obsah)
    
    def porovnej(self, ctverec2):
        """
        Metoda pro porovnání 2 čtverců

        Parametrem je druhý čtverec
        """

        if (self.strana_a > ctverec2.strana_a):
            print('\nČtverec o straně', self.strana_a, 'je větší než čtverec o straně', ctverec2.strana_a)

        elif (self.strana_a == ctverec2.strana_a):
            print('\nOba čtverce jsou stejné a mají stranu', self.strana_a)

        else:
            print('\nČtverec o straně', self.strana_a, 'je menší než čtverec o straně', ctverec2.strana_a)


if __name__ == '__main__':
    main()