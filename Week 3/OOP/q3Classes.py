class Player:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

class BasketballPlayer(Player):
    positions = ["Guard", "Forward", "Center"]

    def __init__(self, name, position):
        super(BasketballPlayer, self).__init__(name)
        self.__position = position

    def get_position(self):
        return self.__position

    def set_position(self, position):
        while position not in self.__class__.positions:
            position = input("Enter position: ")
        self.__position = position

    def __str__(self):
        s = f"{self.get_name()} playing as a {self.__position}"
        return s
