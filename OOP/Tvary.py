import math

def main():

    print('\nTento soubor je o tvarech!')

    strana_ctverec = float(input('\nZadej stranu čtverce: '))
    
    # ctverec1
    Ctverec1 = Ctverec(strana_ctverec)
    Ctverec1.obvod()
    Ctverec1.obsah()


    strana_obdelnik_a = float(input('\nZadej stranu obdélníka a: '))
    strana_obdelnik_b = float(input('\nZadej stranu obdélníka b: '))

    # obdelnik1
    Obdelnik1 = Obdelnik(strana_obdelnik_a, strana_obdelnik_b)
    Obdelnik1.obvod()
    Obdelnik1.obsah()

    polomer_r = float(input('\nZadej poloměr kruhu: '))

    # kruh1
    Kruh1 = Kruh(polomer_r)
    Kruh1.obvod()
    Kruh1.obsah()


# třída čtverec
class Ctverec:
    
    def __init__(self, strana_a):
        self.strana_a = strana_a

    def obvod(self):
        obvod = 4 * self.strana_a
        print('Obvod čtverce o straně', self.strana_a, 'je', obvod)

    def obsah(self):
        obsah = math.pow(self.strana_a, 2)
        print('Obsah čtverce o straně', self.strana_a, 'je', obsah)

# třída obdélník
class Obdelnik:
    
    def __init__(self, strana_a, strana_b):
        self.strana_a = strana_a
        self.strana_b = strana_b

    def obvod(self):
        obvod = 2 * (self.strana_a + self.strana_b)
        print('Obvod obdelníka o straně', self.strana_b, 'je', obvod)

    def obsah(self):
        obsah = self.strana_a * self.strana_b
        print('Obsah obdelníka o straně', self.strana_a, 'je', obsah)

# třída kruh
class Kruh:
    
    def __init__(self, polomer):
        self.polomer = polomer

    def obvod(self):
        obvod = 2 * math.pi * self.polomer
        print('Obvod kruhu o poloměru', self.polomer, 'je', round(obvod, 3))

    def obsah(self):
        obsah = math.pi * math.pow(self.polomer, 2)
        print('Obsah kruhu o poloměru', self.polomer, 'je', round(obsah, 3))


if __name__ == '__main__':
    main()