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
        """
        Constructor of MyDog

        Parameters:

        name =  dogs name = what is its name?

        breed = dogs breed

        age = dogs age = how old is it?
        """
        self.name = name
        self.breed = breed
        self.age = age

 
    def show_dog(self):
        """
        Print all information about dog.
        """
        print("\n-----")
        print("Muj pes se jmenuje", self.name, "a je to", self.breed)
        print("-----")

    def zastekej(self, count):
        """
        Print the sound the animal makes.
        
        Parameters:

        count =  how many times?
        """
        print(self.name, "dělá:")
        i = 0
        while i < count:
            print(self.zvuk)
            i += 1
    
    def stari(self):
        """
        Print information about dogs age.
        """
        if (self.age <= 2):
            print(self.name, "je jeste stene")
        elif (self.age <= 10):
            print(self.name, "je pes v plené síle")
        else:
            print(self.name, "je už starší pejsek")

# inheritance
class MyAngryDog(MyDog):
    """
    Child class that inherits from MyDog
    """
    def be_angry(self, count):
        """
        Print information about angry dog.
        """
        print("{} is so angry!!!!".format(self.name))
        for i in range(count):
            print("VRRrrr")

# inheritance
class MyCuteDog(MyDog):
    """
    Child class that inherits from MyDog
    """
    def be_cute(self):
        """
        Print information about cute dog.
        """
        print("{} is so cute!!!!".format(self.name))




if __name__ == '__main__':
    main()