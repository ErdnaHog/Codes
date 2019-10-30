class Owner:
    def __init__(self, name):
        self.__name = name
        self.__email = "" # no instructions to how we should set email

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email


