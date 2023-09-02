import math

def main():

    print('\nTento soubor je o tvarech!')

    strana_ctverec = float(input("Zadej stranu čtverce: "))
    
    # ctverec1
    Ctverec1 = Ctverec(strana_ctverec)
    Ctverec1.obvod()
    Ctverec1.obsah()


    strana_obdelnik_a = float(input("Zadej stranu obdélníka a: "))
    strana_obdelnik_b = float(input("Zadej stranu obdélníka b: "))

    # obdelnik1
    Obdelnik1 = Obdelnik(strana_obdelnik_a, strana_obdelnik_b)
    Obdelnik1.obvod()
    Obdelnik1.obsah()

    polomer_r = float(input("Zadej polomer kruhu: "))

    # kruh1
    Kruh1 = Kruh(polomer_r)
    Kruh1.obvod()
    Kruh1.obsah()


# třída čtverec
class Ctverec:
    """ 
    Třída pro vytvoření a získání vlastností čtverce

    Metody počítají obvod, obsah.

    Výsledky se vypisují jako text.
    """
    
    def __init__(self, strana_a):
        """
        Konstruktor čtverce - parametrem je strana a
        """
        self.strana_a = strana_a

    def obvod(self):
        """
        Metoda pro výpočet obvodu čtverce

        Vypíše text

        Obvod čtverce: o = 4*a
        """
        obvod = 4 * self.strana_a
        print('Obvod čtverce o straně', self.strana_a, 'je', obvod)

    def obsah(self):
        """
        Metoda pro výpočet obsahu čtverce

        Vypíše text

        Obsah čtverce: S = a^2
        """
        obsah = math.pow(self.strana_a, 2)
        print('Obsah čtverce o straně', self.strana_a, 'je', obsah)

# třída obdélník
class Obdelnik:
    """ 
    Třída pro vytvoření a získání vlastností obdélníka

    Metody počítají obvod, obsah.

    Výsledky se vypisují jako text.
    """
    
    def __init__(self, strana_a, strana_b):
        """
        Konstruktor obdélníka - parametry jsou strana a, strana b
        """
        self.strana_a = strana_a
        self.strana_b = strana_b

    def obvod(self):
        """
        Metoda pro výpočet obvodu obdélníka

        Vypíše text

        Obvod obdélníka: o = 2*(a+b)
        """
        obvod = 2 * (self.strana_a + self.strana_b)
        print('Obvod obdelníka o stranách', self.strana_a, 'a' ,self.strana_b, 'je', obvod)

    def obsah(self):
        """
        Metoda pro výpočet obsahu obdélníka

        Vypíše text
        
        Obsah obdélníka: o = a*b
        """
        obsah = self.strana_a * self.strana_b
        print('Obsah obdelníka o stranách', self.strana_a, 'a' ,self.strana_b, 'je', obsah)

# třída kruh
class Kruh:
    """ 
    Třída pro vytvoření a získání vlastností kruhu

    Metody počítají obvod, obsah.

    Výsledky se vypisují jako text.
    """
    
    def __init__(self, polomer):
        """
        Konstruktor kruhu - parametrem je poloměr r
        """
        self.polomer = polomer

    def obvod(self):
        """
        Metoda pro výpočet obvodu kruhu

        Obvod kruhu: o = 2*PI*r
        """
        obvod = 2 * math.pi * self.polomer
        print('Obvod kruhu o poloměru', self.polomer, 'je', round(obvod, 3))

    def obsah(self):
        """
        Metoda pro výpočet obsahu kruhu

        Obsah kruhu: S = PI*r^2
        """
        obsah = math.pi * math.pow(self.polomer, 2)
        print('Obsah kruhu o poloměru', self.polomer, 'je', round(obsah, 3))


if __name__ == '__main__':
    main()