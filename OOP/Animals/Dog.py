class MyDog:
    zvuk = "Haf"

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

 
    def show_dog(self):
        print("\n-----")
        print("My dog's name is", self.name, "and it is", self.breed)
        print("-----")

    def make_noice(self, count):
        print(self.name, "make:")
        i = 0
        while i < count:
            print(self.zvuk)
            i += 1
    
    def how_old(self):
        if (self.age <= 2):
            print(self.name, "is a young dog.")
        elif (self.age <= 10):
            print(self.name, "is a adult dog.")
        else:
            print(self.name, "is a really old dog.")

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