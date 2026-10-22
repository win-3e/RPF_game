from characters import Character, Warrior, Mage, Archer
from custom_error import NotEnoughManaError, NotEnoughArrowsError, CharacterDefeatedError
from game_dictionary import Game 

game = Game()
running = True

while running:
    print(""" ===== RPG Battle Menu =====
1. Create warrior
2. Create mage
3. Create archer
4. Show all characters
5. Start a battle
6. Heal a character
7. Show battle log
8. Show strongest character
9. Remove character
10. Exit 
""")
    
    while True: #another loop so that after the exception you return back to input and not the battle menu
        try:
            user_choice = int(input("Enter your choice: "))
            if user_choice == 1 or user_choice == 2 or user_choice==3:
                name = input("Enter name: ").strip()
                max_health = int(input("Enter max health: ").strip())
                attack_power = int(input("Enter attack power: ").strip())

                if user_choice== 1:
                    defense = int(input("Enter defense: ").strip())
                    new_character = Warrior(name, attack_power, max_health, defense)
                    game.add_character(new_character)
                
                elif user_choice == 2:
                    new_character = Mage(name, attack_power, max_health)
                    game.add_character(new_character)
                
                elif user_choice == 3:
                    new_character = Archer(name, attack_power, max_health)
                    game.add_character(new_character)
                print(f"{new_character.get_class_name()} {name} successfully created!")
                break

            elif user_choice == 4:
                game.show_all_characters()
                break

            elif user_choice == 5:
                name1 = input("Enter first fighter: ").strip()
                name2 = input("Enter second fighter: ").strip()
                game.fight(name1, name2)
                break

            elif user_choice == 6:
                heal_choice = input("Which character would you like to heal? ")
                heal_amount = int(input("Enter healing amount: ").strip())
                new_health = game.heal_character(heal_choice, heal_amount)
                print(f"{heal_choice}'s health restored to {new_health}!")
                break

            elif user_choice == 7:
                game.show_battle_log()
                break

            elif user_choice == 8:
                if not game.battle_log:
                    print("No champion has been crowned yet.....")
                else:
                    strongest = game.get_strongest()
                    print(f"{strongest} is the strongest character!")
                break
            
            elif user_choice == 9:
                remove_choice = input("Which character would you like to remove? ")
                game.remove_character(remove_choice)
                break 
            
            elif user_choice == 10:
                print("Thank you! Good luck on your next adventure....")
                running = False
                break 

        except ValueError as e: #handles every single Value error, including ones from inside a method
            print(f"Error: {e}, Check your input!")