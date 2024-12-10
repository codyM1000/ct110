#matheney_cody
# game project
import random

# Define character classes, stats, and weapons
character_classes = {
    "Cleric": {
        "Strength": 6,
        "Agility": 5,
        "Intelligence": 8,
        "Health": 70,
        "Weapons": {
            "Mace": {"Damage": (5, 10)},
            "Holy Staff": {"Damage": (4, 8)},
            "Hammer": {"Damage": (6, 12)},
        },
    },
    "Warrior": {
        "Strength": 12,
        "Agility": 7,
        "Intelligence": 5,
        "Health": 80,
        "Weapons": {
            "Sword": {"Damage": (8, 12)},
            "Great Sword": {"Damage": (10, 15)},
            "Axe": {"Damage": (9, 14)},
        },
    },
    "Mage": {
        "Strength": 3,
        "Agility": 4,
        "Intelligence": 10,
        "Health": 50,
        "Weapons": {
            "Wand": {"Damage": (4, 8)},
            "Staff": {"Damage": (5, 9)},
            "Tome": {"Damage": (3, 7)},
        },
    },
}

# Define boss stats and abilities
boss = {
    "Name": "Dark Overlord",
    "Strength": 10,
    "Health": 100,
    "Healing Ability": (10, 20),  # Boss can heal for a random amount
    "Block Chance": 0.3,  # 30% chance to block on its turn
}

# Get the player's name
character_name = input("Enter your character's name: ")

# Display available classes
print("\nChoose a class:")
for i, cls in enumerate(character_classes.keys(), 1):
    print(f"{i}. {cls}")

# Get the user's class choice
while True:
    try:
        class_choice = int(input("\nEnter the number of your chosen class: "))
        if 1 <= class_choice <= len(character_classes):
            chosen_class = list(character_classes.keys())[class_choice - 1]
            player_stats = character_classes[chosen_class]
            break
        else:
            print("Invalid choice. Please choose a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Display available weapons for the chosen class
print(f"\nYou chose the {chosen_class} class.")
print("Now, choose your weapon:")
weapons = player_stats["Weapons"]
for i, (weapon, attributes) in enumerate(weapons.items(), 1):
    print(f"{i}. {weapon} (Damage: {attributes['Damage'][0]}-{attributes['Damage'][1]})")

# Get the user's weapon choice
while True:
    try:
        weapon_choice = int(input("\nEnter the number of your chosen weapon: "))
        if 1 <= weapon_choice <= len(weapons):
            chosen_weapon = list(weapons.keys())[weapon_choice - 1]
            weapon_damage = weapons[chosen_weapon]["Damage"]
            break
        else:
            print("Invalid choice. Please choose a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Display chosen class, weapon, and stats
print(f"\nCharacter Name: {character_name}")
print(f"Chosen Class: {chosen_class}")
print(f"Chosen Weapon: {chosen_weapon} (Damage: {weapon_damage[0]}-{weapon_damage[1]})")
print("Stats:")
for stat, value in player_stats.items():
    if stat != "Weapons":
        print(f"  {stat}: {value}")

# Add inventory
inventory = {"Healing Potion": 2}  # Player starts with 2 healing potions

# Begin the battle
print(f"\n{character_name}, the {chosen_class}, armed with a {chosen_weapon}, will now fight the {boss['Name']}!")

player_health = player_stats["Health"]
boss_health = boss["Health"]
boss_block = False  # Boss blocking state

# Battle loop
while player_health > 0 and boss_health > 0:
    print("\nYour Turn!")
    print("1. Attack")
    print("2. Block")
    print("3. Use Item")

    # Player turn
    while True:
        try:
            action = int(input("Choose your action (1-3): "))
            if action == 1:  # Attack
                player_damage = random.randint(weapon_damage[0], weapon_damage[1])
                if boss_block:
                    player_damage = max(0, player_damage - random.randint(5, 10))
                    print(f"\nThe {boss['Name']} blocked part of your attack! Damage reduced to {player_damage}.")
                boss_health -= player_damage
                print(f"\nYou attack the {boss['Name']} with your {chosen_weapon} for {player_damage} damage!")
                boss_block = False  # Reset boss block status
                break
            elif action == 2:  # Block
                print("\nYou prepare to block the next attack, reducing damage!")
                block = True
                break
            elif action == 3:  # Use Item
                if inventory["Healing Potion"] > 0:
                    heal_amount = random.randint(15, 30)
                    player_health += heal_amount
                    inventory["Healing Potion"] -= 1
                    print(f"\nYou used a Healing Potion and restored {heal_amount} health!")
                else:
                    print("\nYou have no Healing Potions left!")
                continue  # Allow the player to pick another action if no potions remain
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Check if the boss is defeated
    if boss_health <= 0:
        print(f"\nThe {boss['Name']} is defeated! You are victorious!")
        break

    # Boss turn
    print(f"\nThe {boss['Name']}'s Turn!")
    boss_action = random.choice(["Attack", "Heal", "Block"])
    if boss_action == "Attack":
        print(f"The {boss['Name']} attacks!")
        boss_damage = random.randint(5, boss["Strength"])
        if "block" in locals() and block:  # Reduce damage if the player blocks
            boss_damage = max(0, boss_damage - random.randint(3, 7))
            print(f"You blocked some of the damage! Reduced to {boss_damage}.")
        player_health -= boss_damage
        print(f"The {boss['Name']} hits you for {boss_damage} damage!")
        block = False  # Reset player block status
    elif boss_action == "Heal":
        heal_amount = random.randint(boss["Healing Ability"][0], boss["Healing Ability"][1])
        boss_health += heal_amount
        print(f"The {boss['Name']} uses its dark magic to heal for {heal_amount} health!")
    elif boss_action == "Block":
        boss_block = True
        print(f"The {boss['Name']} prepares to block your next attack!")

    # Check if the player is defeated
    if player_health <= 0:
        print(f"\n{character_name} has been defeated by the {boss['Name']}... Game Over.")
        break

    # Display current health and inventory
    print(f"\n{character_name}'s Health: {player_health}")
    print(f"{boss['Name']}'s Health: {boss_health}")
    print(f"Inventory: {inventory}")

# End of the game
if player_health > 0:
    print("\nCongratulations on your victory!")
else:
    print("\nBetter luck next time!")
