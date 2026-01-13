import random
from colorama import Fore, Style
import json

class Monster:
    def __init__(self, name, hp, level, type_):
        """
        Initializes a Monster object.
        :param name: The name of the monster
        :param hp: The hit points (health) of the monster
        :param level: The level of the monster
        :param type_: The type of the monster (Fire, Water, Grass)
        """
        self.name = name
        self.hp = hp
        self.level = level
        self.type = type_
        self.special_move = None

    def __str__(self):
        """Returns a string representation of the Monster."""
        color_mapping = {
            'Fire': Fore.RED,
            'Water': Fore.BLUE,
            'Grass': Fore.GREEN
        }
        color = color_mapping.get(self.type, Style.RESET_ALL)
        return f"{color}{self.name} (Type: {self.type}, Level: {self.level}, HP: {self.hp}, Special Move: {self.special_move or 'None'}){Style.RESET_ALL}"

    def to_dict(self):
        """Converts the Monster object to a dictionary."""
        return {
            "name": self.name,
            "hp": self.hp,
            "level": self.level,
            "type": self.type,
            "special_move": self.special_move,
        }

    @staticmethod
    def from_dict(data):
        """Creates a Monster object from a dictionary."""
        monster = Monster(data["name"], data["hp"], data["level"], data["type"])
        monster.special_move = data.get("special_move", None)
        return monster

    def level_up(self):
        """
        Levels up the monster and assigns a new special move.
        """
        self.level += 1
        tech_words = ["Firewall", "Overclock", "Bit", "Cache", "Stack", "Quantum"]
        actions = ["Blast", "Tackle", "Strike", "Smash", "Wave"]
        self.special_move = f"{random.choice(tech_words)} {random.choice(actions)}"


def save_game(monsters, filename):
    """
    Saves the list of monsters to a JSON file.
    :param monsters: The list of Monster objects to save
    :param filename: The JSON file where the data will be saved
    """
    data = [monster.to_dict() for monster in monsters]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def main():
    while True:
        print("\nMonster Game Menu")
        print("1. Create a Monster")
        print("2. Load Monsters from File")
        print("3. Save Monsters to File")
        print("4. List All Monsters")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter monster name: ")
            hp = int(input("Enter monster HP: "))
            level = int(input("Enter monster Level: "))
            type_ = input("Enter monster Type (Fire, Water, Grass): ")
            monsters.append(Monster(name, hp, level, type_))
        elif choice == "2":
            filename = input("Enter filename: ")
            loaded_monsters = load_game(filename)
            if loaded_monsters:
                monsters.extend(loaded_monsters)
                print("Monsters loaded successfully.")
            else:
                print("No monsters were loaded.")
        elif choice == "3":
            filename = input("Enter filename: ")
            save_game(monsters, filename)
            print("Monsters saved successfully.")
        elif choice == "4":
            if monsters:
                for m in monsters:
                    print(m)
            else:
                print("No monsters available.")
        elif choice == "5":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

monsters = []
def load_game(filename):
    """
    Loads the list of monsters from a JSON file.
    :param filename: The JSON file to load data from
    :return: A list of Monster objects
    """
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [Monster.from_dict(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# ADD THIS TO THE VERY BOTTOM:
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Oops! The game crashed: {e}")
        input("Press Enter to close...")