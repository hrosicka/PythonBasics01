import os

def main():

    os.system('cls')

    print()
    print('-----------')
    print('Our Company')
    print('-----------')


    emp1 = Employee()
    emp2 = Employee()
    emp3 = Employee()
    m1 = Meeting()

    m1 + emp1
    m1 + emp2
    print("Meeting about {} people.".format(m1.__len__()))
    m1 + emp3
    print("Meeting about {} people.".format(len(m1)))


# class employee
class Employee():

    # start id for new Employee
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

# class meeting
class Meeting():

    def __init__(self):
        self.attendees = []


    # Dunder Methods - overloading
    def __add__(self, employee):
        print("ID {} employee added.".format(employee.id))
        self.attendees.append(employee)

    # Dunder Methods - overloading
    def __len__(self):
        return len(self.attendees)   



if __name__ == '__main__':
    main()