class Weapon:
    def __init__(self, name, damage, weapon_type):
        self.name = name
        self.damage = damage
        self.weapon_type = weapon_type

weapons = []

def add_weapon(name, damage, weapon_type):
    weapon = Weapon(name, damage, weapon_type)
    weapons.append(weapon)

def get_weapons():
    return [(w.name, w.damage, w.weapon_type) for w in weapons]


# тест работы
add_weapon("Sword", 50, "Melee")
add_weapon("Gun", 80, "Ranged")

print(get_weapons())
