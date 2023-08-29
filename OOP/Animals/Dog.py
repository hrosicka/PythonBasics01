def main():
    print('All about dogs!!!')
    
    # young dog Alik
    Alik = MyCuteDog('Alík','Voříšek', 1)
    Alik.show_dog()
    Alik.make_noice(5)
    Alik.how_old()
    Alik.be_cute()


class MyDog:
    """
    Parent class
    """
    noice = "Haf"

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
        print("My dog's name is", self.name, "and it is", self.breed)
        print("-----")

    def make_noice(self, count):
        """
        Print the sound the animal makes.
        """
        print(self.name, "makes:")
        i = 0
        while i < count:
            print(self.noice)
            i += 1
    
    def how_old(self):
        """
        Print information about dogs age.
        """
        if (self.age <= 2):
            print(self.name, "is a young dog.")
        elif (self.age <= 10):
            print(self.name, "is a adult dog.")
        else:
            print(self.name, "is a really old dog.")

class MyAngryDog(MyDog):
    """
    Child class that inherits from MyDog
    """
    def be_angry(self, count):
        print("{} is so angry!!!!".format(self.name))
        for i in range(count):
            print("VRRrrr")

class MyCuteDog(MyDog):
    """
    Child class that inherits from MyDog
    """
    def be_cute(self):
        print("{} is so cute!!!!".format(self.name))



if __name__ == '__main__':
    main()