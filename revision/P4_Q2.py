from P4_Q1 import Monster


class FireMonster(Monster):
    def __init__(self):
        super().__init__("firebug", 10, 9, 4)


class WaterMonster(Monster):
    def __init__(self):
        super().__init__("waterbird", 15, 6, 3)


class GrassMonster(Monster):
    def __init__(self):
        super().__init__("grassshoper", 20, 5, 3)


def display_info(class_variable):
    if isinstance(class_variable, FireMonster):
        type = "Fire Type"
    elif isinstance(class_variable, WaterMonster):
        type = "Water Type"
    else:
        type = "Grass TYpe"
    print(f"{class_variable.get_name()} is a {type} monster")

m1 = FireMonster()
m2 = WaterMonster()

display_info(m1)
display_info(m2)

listt =[9,5,3,21,0]
listt.s
