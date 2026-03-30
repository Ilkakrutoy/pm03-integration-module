import json
from models import Weapon

FILE_NAME = "weapons.json"


def load_weapons():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Weapon.from_dict(w) for w in data]
    except:
        return []


def save_weapons(weapons):
    with open(FILE_NAME, "w") as file:
        json.dump([w.to_dict() for w in weapons], file, indent=4)
