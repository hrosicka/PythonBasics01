import os

def main():

    os.system('cls')
    print()
    print('Animals!')
    
    # dog Azor
    print()
    dog1 = Dog("Azor", 2)
    dog1.show_animal()
    dog1.eat()
    dog1.bark()
    dog1.make_noise()

    # dog Alik
    print()
    dog2 = CuteDog("Alik", 1)
    dog2.show_animal()
    dog2.eat()
    dog2.bark()
    dog2.make_noise()
    dog2.be_cute()

    # cat Micka
    print()
    cat1 = Cat("Micka", 4)
    cat1.show_animal()
    cat1.eat()
    cat1.meow()
    cat1.make_noise()

    # cat Micina
    print()
    cat2 = AngryCat("Micina", 8)
    cat2.show_animal()
    cat2.eat()
    cat2.meow()
    cat2.make_noise()
    cat2.be_angry()

    # pet Archi
    print()
    pet1 = Pet("Archi", 3)
    pet1.show_animal()
    pet1.eat()
    pet1.make_noise()


    # example of Polymorphism
    animals = [dog1, dog2, cat1, cat2, pet1]
    print()
    print("-------------")
    print("We make noice")
    print("-------------")
    for o in animals:
     o.make_noise()



# parent class Pet
class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        """
        Pet eats and makes yummy yummy

        Print Yummy yummy
        """
        print ("Yummy yummy!!!")

    def show_animal(self):
        print ("Name:", self.name, "age:", self.age)

    def make_noise(self):
        print("{} says, VrrrVrrr".format(self.name))

#children class Dog
class Dog(Pet):

    def bark(self):
        print("Bark!!!!")
    
    # override method
    def make_noise(self):
        print("{} says, Bark!!!!".format(self.name))


# multiple inheritance
class CuteDog(Dog):

    def be_cute(self):
        print("{} is so cute!!!!".format(self.name))



#children class Cat
class Cat(Pet):

    def meow(self):
        print("Meow!!!!")

    # override method
    def make_noise(self):
        print("{} says, Meow!!!!".format(self.name))


# multiple inheritance
class AngryCat(Cat):

    def be_angry(self):
        print("{} is so angry!!!!".format(self.name))

if __name__ == '__main__':
    main()