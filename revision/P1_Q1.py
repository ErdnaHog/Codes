class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def get_name(self):
        return self.__age

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age


name = input("Enter pet name: ")
animal_type = input("Enter pet type: ")
age = input("Enter age of pet: ")

pet1 = Pet(name, animal_type, age)
print(f"Pet {pet1.get_name()} is a {pet1.get_animal_type()}, and it is {pet1.get_age()}")
