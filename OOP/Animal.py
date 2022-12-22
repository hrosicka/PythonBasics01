import os

def main():

    os.system('cls')

    print('Animals!')
    
    # dog Azor
    dog1 = Dog("Azor", 2)
    dog1.show_animal()
    dog1.eat()
    dog1.bark()

    # cat Micka
    cat1 = Cat("Micka", 4)
    cat1.show_animal()
    cat1.eat()
    cat1.meow()


# parent class Pet
class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print ("Yummy yummy!!!")

    def show_animal(self):
        print ("Name:", self.name, "age:", self.age)

#children class Dog
class Dog(Pet):

    def bark(self):
        print('Bark!!!!')


#children class Cat
class Cat(Pet):

    def meow(self):
        print('Meow!!!!')



if __name__ == '__main__':
    main()