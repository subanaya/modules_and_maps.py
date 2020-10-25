# Actions
actions = [
    'attack enemy', 'explore', 'move right', 'move left',
    'move up', 'move down', 'fill up oxygen tank'
    ]

# Prompt for user to choose an action
prompt_3 = "\nComplete one of the following actions:\n"
for action in actions:
    prompt_3 += f"\n{action}"
prompt_3 += "\n\n"


def user_action_3(action):
    """user chooses an action in their location"""
    choice = f"{action}"
    return choice.title()

while True:
    response = input(prompt_3)
    if response.lower() == 'attack enemy':
        print("You attacked the enemy")
        break
    elif response.lower() == 'explore':
        print("You explored")
        break
    elif response.lower() == 'move right':
        print("You moved to the right")
        break
    elif response.lower() == 'move left':
        print("You moved to the left")
        break
    elif response.lower() == 'move up':
        print("You moved up")
        break
    elif response.lower() == 'move down':
        print("You moved down")
        break
    elif response.lower() == 'fill up oxygen tank':
        print("you filled up your oxygen tank")
        break
