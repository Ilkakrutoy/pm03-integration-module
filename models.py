class Weapon:
    def __init__(self, weapon_id, name, damage, weapon_type):
        self.weapon_id = weapon_id
        self.name = name
        self.damage = damage
        self.weapon_type = weapon_type

    def to_dict(self):
        return {
            "id": self.weapon_id,
            "name": self.name,
            "damage": self.damage,
            "type": self.weapon_type
        }

    @staticmethod
    def from_dict(data):
        return Weapon(
            data["id"],
            data["name"],
            data["damage"],
            data["type"]
        )
