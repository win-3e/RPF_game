from characters import Character, Warrior, Mage, Archer
from custom_error import NotEnoughManaError, NotEnoughArrowsError, CharacterDefeatedError
import random, time

class Game: 
    def __init__(self):
        self.characters = {}
        self.battle_log = []
        self.wins =  {}
    
    def add_character(self, character):
        if character.name in self.characters:
            raise ValueError("This character already exists.")   
        self.characters[character.name]  = character
        self.wins[character.name] = 0
        #use try/ except in the main program to catch the error
    
    def find_character(self, name):
        if name not in self.characters:
            raise ValueError(f"Character {name} not found.")
        else:
            return self.characters[name]
    
    def remove_character(self, name):
        self.find_character(name)
        # it returns the character not its name
        del self.characters[name]
        del self.wins[name]

    
    def show_all_characters(self):
        if not self.characters: #check if dict is empty
            print("No characters have been created yet.")
            return
        for character in self.characters.values():
            character.display_info()
        #values() = calls the object itself, so it can execute display method 

    def heal_character(self, name, amount): #helps you choose a character to heal
        character = self.find_character(name)
        character.heal(amount)
        return character.get_health()
            
    def fight(self, name1, name2):
        player1 = self.find_character(name1)
        player2 = self.find_character(name2)
        #name1 and name2 are strings, this turns them into usable objects
        if player1 is player2:
           raise ValueError("A character cannot fight itself.")
        
        print(f"===== BATTLE: {name1} VS {name2} =====")
        round = 1
        turn = name1
        choices = [ "attack","special move"]

        while player1.is_alive() and player2.is_alive() :
            try:
                next_move = random.choice(choices)
                #previous health of each player
                old_health1 = player1.get_health()
                old_health2 = player2.get_health()
                
                if turn == name1:
                    if next_move == "attack":
                        player1.attack(player2)  #after attack, .get_health returns a new value
                        amount = old_health2 - player2.get_health()
                        log = f"Round {round}: {name1} attacked {name2} for {amount} damage. ({name2}: {player2.get_health()}/{player2.max_health})"
                    else:
                        player1.special_move(player2)
                        amount = old_health2 - player2.get_health()
                        log = f"Round {round}: {name1} used {player1.power_name} on {name2} for {amount} damage. ({name2}: {player2.get_health()}/{player2.max_health})"
                    print(log)
                    time.sleep(1)
                    self.battle_log.append(log)
                    
                    
                else:
                    if next_move == "attack":
                        player2.attack(player1)
                        amount = old_health1 - player1.get_health()
                        log = f"Round {round}: {name2} attacked {name1} for {amount} damage. ({name1}: {player1.get_health()}/{player1.max_health})"
                    else:
                        player2.special_move(player1)
                        amount = old_health1 - player1.get_health()
                        log = f"Round {round}: {name2} used {player2.power_name} on {name1} for {amount} damage. ({name1}: {player1.get_health()}/{player1.max_health})"
                    print(log)
                    time.sleep(1)
                    self.battle_log.append(log)


            except NotEnoughManaError as e1:
                print(e1) 
                self.battle_log.append(str(e1))

            except NotEnoughArrowsError as e2:
                print(e2)
                self.battle_log.append(str(e2))

            except CharacterDefeatedError as e3:
                print(e3)
                self.battle_log.append(str(e3))
                break
            
            round += 1
            turn = name2 if turn == name1 else name1
            # ternary: A if B is true, else C. A is the true value while B is the false value

        if not player1.is_alive():
            loser = player1
            winner = player2
        elif not player2.is_alive():
            loser = player2
            winner = player1
        print(f"""{loser.name} has been defeated!
Winner: {winner.name} ({winner.get_class_name()})""")

        self.wins[winner.name] += 1 #acts as a counter for wins
        return winner 

    def show_battle_log(self):
        if not self.battle_log:
            print("No battles yet")
            return
        for logs in self.battle_log :
            print(logs)
    
    def get_strongest(self):
        #accounts for when the dict is empty and when no one has won yet
        if not self.wins and max(self.win.values())== 0 : 
            print("No battles won yet.")
            return
        return max(self.wins, key= self.wins.get)
    # max(a, key=a.get) where a is the dict, key= basically goes: for key in a: b = a.get(key), so you also don't need () after get, cuz it does that for you.
    