import random

# value returning function to create a character
def create_character():
    print("\n🛠️ Let's create your character!")
    name = input("Enter character name: ")
    health = int(input("Enter health points (e.g., 100): "))
    attack = int(input("Enter attack points (e.g., 10): "))
    defense = int(input("Enter defense points (e.g., 5): "))
    items = []

    character = {
        "name": name,
        "health": health,
        "attack": attack,
        "defense": defense,
        "items": items
    }

    return character

# non value returning function to display character
def display_character(character):
    print("\n📜 Character Details:")
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")

# character fights a monster
def fight_monster(character):
    print("\n👹 A wild monster is about to Attack!")
    monster_health = random.randint(20, 50)
    monster_attack = random.randint(5, 15)
    print(f"The monster has {monster_health} HP and {monster_attack} attack.")

    while monster_health > 0 and character["health"] > 0:
        action = input("Do you want to attack (a) or run (r)? ").lower()
        if action == 'a':
            damage = character["attack"] - random.randint(0, 3)
            monster_health -= damage
            print(f"🗡️ You hit the monster for {damage} damage! Monster HP: {monster_health}")

            if monster_health > 0:
                received = monster_attack - character["defense"]
                received = max(received, 0)
                character["health"] -= received
                print(f"💥 The monster hits back for {received} damage! Your HP: {character['health']}")
        elif action == 'r':
            print("🏃 You escaped!")
            return
        else:
            print("❌ Invalid action!")

    if character["health"] <= 0:
        print("💀 You have been defeated...")
    else:
        print("🎉 You defeated the monster!")
        found_item = random.choice(["Health Potion 🍷", "Sword 🗡️", "Shield 🛡️", "Teddy Bear 🧸"])
        character["items"].append(found_item)
        print(f"You found an item: {found_item}")

# use an item
def use_item(character):
    if not character["items"]:
        print("🧺 You have no items to use.")
        return

    print("\n🎒 Your items:")
    for idx, item in enumerate(character["items"], 1):
        print(f"{idx}. {item}")

    choice = int(input("Which item do you want to use? (number): "))
    if 1 <= choice <= len(character["items"]):
        item = character["items"].pop(choice - 1)
        if "Health Potion" in item:
            heal = random.randint(10, 30)
            character["health"] += heal
            print(f"🧪 You used {item} and recovered {heal} HP! Current HP: {character['health']}")
        elif "Sword" in item:
            boost = random.randint(3, 7)
            character["attack"] += boost
            print(f"🗡️ You equipped the {item} and gained +{boost} attack! Current Attack: {character['attack']}")
        elif "Shield" in item:
            print(f"🧱 You used {item}, but nothing happened... maybe it's a dummy shield.")
        else:
            print(f"📦 You used {item}, but nothing happened... maybe it's just for show.")
    else:
        print("❌ Invalid choice.")

# main function menu
def main():
    print("🎮 Welcome to the Character Creation Game!")
    character = create_character()

    while character["health"] > 0:
        print("\n📜 Menu:")
        print("1. Display Character")
        print("2. Fight Monster")
        print("3. Use Item")
        print("4. Exit Game")
        choice = input("Choose an option: ")

        if choice == "1":
            display_character(character)
        elif choice == "2":
            fight_monster(character)
        elif choice == "3":
            use_item(character)
        elif choice == "4":
            print("👋 Thanks for playing! Goodbye.")
            break
        else:
            print("❌ Invalid choice.")

    if character["health"] <= 0:
        print("💀 Game Over! Your character has fallen in battle.")

# Only run main if this script is the entry point (I do not understand what that is)
if __name__ == "__main__":
    main()
