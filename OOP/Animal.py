import os

def main():

    os.system('cls')

    print('Animals!')
    
    # dog Azor
    print()
    dog1 = Dog("Azor", 2)
    dog1.show_animal()
    dog1.eat()
    dog1.bark()
    dog1.make_nois()

    # cat Micka
    print()
    cat1 = Cat("Micka", 4)
    cat1.show_animal()
    cat1.eat()
    cat1.meow()
    cat1.make_nois()

    # pet Archi
    print()
    pet1 = Pet("Archi", 3)
    pet1.show_animal()
    pet1.eat()
    pet1.make_nois()



# parent class Pet
class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print ("Yummy yummy!!!")

    def show_animal(self):
        print ("Name:", self.name, "age:", self.age)

    def make_nois(self):
        print("{} says, VrrrVrrr".format(self.name))

#children class Dog
class Dog(Pet):

    def bark(self):
        print("Bark!!!!")
    
    # override method
    def make_nois(self):
        print("{} says, Bark!!!!".format(self.name))


#children class Cat
class Cat(Pet):

    def meow(self):
        print("Meow!!!!")

    # override method
    def make_nois(self):
        print("{} says, Meow!!!!".format(self.name))



if __name__ == '__main__':
    main()