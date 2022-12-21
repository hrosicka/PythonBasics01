def main():
    print('Tento soubor je o psech!')
    
    # stenatko Alik
    Alik = MyDog('Alík','Voříšek', 1)
    Alik.show_dog()
    Alik.zastekej()
    Alik.stari()

    # Azor je pes v plné síle
    Azor = MyDog('Azor','Vlčák', 10)
    Azor.show_dog()
    Azor.zastekej()
    Azor.stari()

    # Prcek je čivava v důchodu
    Prcek = MyDog('Prcek','Čivava', 12)
    Prcek.show_dog()
    Prcek.zastekej()
    Prcek.stari()


class MyDog:
    zvuk = "Haf Haf"

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

 
    def show_dog(self):
        print("Muj pes se jmenuje", self.name, "a je to", self.breed)

    def zastekej(self):
        print(self.name, "dělá", self.zvuk)
    
    def stari(self):
        if (self.age <= 2):
            print(self.name, "je jeste stene")
        elif (self.age <= 10):
            print(self.name, "je pes v plené síle")
        else:
            print(self.name, "je už starší pejsek")




if __name__ == '__main__':
    main()