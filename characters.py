# Characters
characters = {
    'Evelyn': {
        'adjective': 'ambitious',
        'skills': 'strength',
        'health_points': '150'
    },
    'Avery': {
        'adjective': 'funny',
        'skills': 'speed',
        'health_points': '100'
    }
}

# The characters' inventories
avery_inventory = {
    'glowstick': {
        'description': 'Releases posion when it breaks through skin',
        'damage': '20',
        'healing': '0'
    },
    'bubble gum': {
        'description': 'Hubba bubba bubble gum',
        'damage': '0',
        'healing': '25'
    },
}

evelyn_inventory = {
    'dagger': {
        'description': 'An old but sharp dagger',
        'damage': '30',
        'healing': '0'
    },
    'rotten apple': {
        'description': 'A commonly found health item',
        'damage': '0',
        'healing': '5'
    },
}


# Prompt for User to Choose a character
for character, description in characters.items():
    Adjective = description['adjective']
    Skills = description['skills']
    Health_points = description['health_points']
    print(f"{character.title()}: ")
    print(f"{character} is {Adjective}.")
    print(f"{character}'s skill is {Skills}.")
    print(f"{character} has {Health_points} health points.")
    print("\n")


prompt_1 = "Choose a character: "


def user_action_1(character):
    """user chooses a character to play,
    character's inventory is printed"""
    choice = f"{character}"
    return choice.title()

while True:
    response = input(prompt_1)
    if response.lower() == "avery":
        print("\nAvery's Inventory:")
        for item, stats in avery_inventory.items():
            Description = stats['description']
            Damage = stats['damage']
            Healing = stats['healing']

            print(f"* {item.title()}")
            print(f"Description: {Description}")
            print(f"Damage: {Damage}")
            print(f"Healing: {Healing}\n")
        break

    elif response.lower() == "evelyn":
        print("\nEvelyn's Inventory:")
        for item, stats in evelyn_inventory.items():
            Description = stats['description']
            Damage = stats['damage']
            Healing = stats['healing']

            print(f"* {item.title()}")
            print(f"Description: {Description}")
            print(f"Damage: {Damage}")
            print(f"Healing: {Healing}\n")
        break
