import maps

# Locations
locations = ['sewer', 'shopping centre', 'scrap yard', 'city tower']

# print location maps
print("Location Maps:")

# Prompt for user to choose a location
print("Locations:")
for location in locations:
    print(location.title())

prompt_2 = "Choose a location: "


# Function for user to choose a location
def user_action_2(location):
    """user chooses a location to start in"""
    choice = f"{location}"
    return choice.title()

while True:
    response = input(prompt_2)
    if response.lower() == "sewer":
        print("\nWelcome to the Sewer")
        break
    elif response.lower() == "shopping centre":
        print("\nWelcome to the Shopping Centre")
        break
    elif response.lower() == "scrap yard":
        print("\nWelcome to the Scrap Yard")
        break
    elif response.lower() == "city tower":
        print("Welcome to the City Tower")
        break
