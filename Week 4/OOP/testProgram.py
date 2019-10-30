from monsterSubClasses import *

def display_info(class_var):
    Type = ""
    if isinstance(class_var, FireMonster):
        Type = "Fire"
    elif isinstance(class_var, WaterMonster):
        Type = "Water"
    else:
        Type = "Grass"
    print(f"{class_var.get_name()} is a {Type} Type monster")

