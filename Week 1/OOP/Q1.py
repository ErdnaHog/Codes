class Pet:
    def __init__(self,name,animal_type,age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    #accessor methods
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age

    #mutator methods
    def set_name(self,name):
        self.__name = name
    def set_animal_type(self,animal_type):
        self.__animal_type = animal_type
    def set_age(self,age):
        self.__age = age
    def printInfo(self):
        print(f"Pet {self.__name} is a {self.__animal_type}, and it is {self.__age} years old")


pet1 = Pet(input("Enter pet name: "), input("Enter pet type: "), input("Enter age of pet: "))
pet1.printInfo()

