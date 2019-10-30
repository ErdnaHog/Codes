from monsterClass import Monster

class FireMonster(Monster):
    def __init__(self):
        super().__init__("firebug", 10, 9, 4)

class WaterMonster(Monster):
    def __init__(self):
        super().__init__("waterbird", 15, 6, 3)

class GrassMonster(Monster):
    def __init__(self):
        super().__init__("grasshopper", 20, 5, 3)


