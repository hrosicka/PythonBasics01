import os

def main():

    os.system('cls')

    print('People')
    print('------')
    
    # Person1
    Person1 = Person('Adam')
    Person1.show_person()

    # Person2
    Person2 = Person('Andreas')
    Person2.show_person()

    # Person3
    Person3 = Person('Barbora')
    Person3.show_person()



class Person:
    
    new_id = 1

    def __init__(self, name):
        self.id = Person.new_id
        Person.new_id += 1
        self.name = name
 
    # show name and id of person
    def show_person(self):
        print("Name:", self.name, "\tid:", self.id)

if __name__ == '__main__':
    main()