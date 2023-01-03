def main():
    print('Tento soubor je o psech!')
    
    # stenatko Alik
    Alik = MyCuteDog('Alík','Voříšek', 1)
    Alik.show_dog()
    Alik.zastekej(5)
    Alik.stari()
    Alik.be_cute()

    # Azor je pes v plné síle
    Azor = MyAngryDog('Azor','Vlčák', 10)
    Azor.show_dog()
    Azor.zastekej(2)
    Azor.stari()
    Azor.be_angry(3)

    # Prcek je čivava v důchodu
    Prcek = MyDog('Prcek','Čivava', 12)
    Prcek.show_dog()
    Prcek.zastekej(1)
    Prcek.stari()


class MyDog:
    zvuk = "Haf"

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

 
    def show_dog(self):
        print("\n-----")
        print("Muj pes se jmenuje", self.name, "a je to", self.breed)
        print("-----")

    def zastekej(self, count):
        print(self.name, "dělá:")
        i = 0
        while i < count:
            print(self.zvuk)
            i += 1
    
    def stari(self):
        if (self.age <= 2):
            print(self.name, "je jeste stene")
        elif (self.age <= 10):
            print(self.name, "je pes v plené síle")
        else:
            print(self.name, "je už starší pejsek")

# inheritance
class MyAngryDog(MyDog):

    def be_angry(self, count):
        print("{} is so angry!!!!".format(self.name))
        for i in range(count):
            print("VRRrrr")




# inheritance
class MyCuteDog(MyDog):

    def be_cute(self):
        print("{} is so cute!!!!".format(self.name))




if __name__ == '__main__':
    main()