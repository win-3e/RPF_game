from custom_error import CharacterDefeatedError, NotEnoughManaError, NotEnoughArrowsError
#base class
class Character:
    def __init__(self, name, attack_power, max_health):
        self.name = name 
        self.attack_power = attack_power
        self.__health = max_health
        self.max_health = max_health
    # retrieve methods
    def get_health(self):
        return self.__health 
    
    def is_alive(self):
        if self.__health > 0:
            return True
        if self.__health == 0:
            return False
    
    def get_class_name(self):
        obj_class = type(self).__name__
        return obj_class
    
    def display_info(self):
        print(f"""==== STATS ====
Name: {self.name}
Class: {self.get_class_name()}
Health: {self.__health}""")

    # action methods        
    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("Damage cannot be negative")
        
        self.__health = max(0, self.__health - amount) #minimum health is 0, negative values still return as 0
        return self.get_health()
        
    def heal(self, amount):
        if amount <= 0 :
            raise ValueError("Healing cannot be negative.")
        
        self.__health = min(self.max_health, self.__health + amount )
        return self.get_health()
    
    # effect tells you the times of damage
    def attack(self, target, effect=1):
        target_survive = target.is_alive()
        self_survive = self.is_alive()
        if self_survive:
            if target_survive:
                amount = self.attack_power * effect
                target.take_damage(amount)
                return amount
            elif not target_survive:
                raise CharacterDefeatedError(target)
        elif not self_survive:
            raise CharacterDefeatedError(self)
        
def special_move(self, target, effect=1):
    self.attack(target, effect)

#Warrior child class
class Warrior(Character):
    def __init__(self, name, attack_power, max_health, defense):
        super().__init__(name, attack_power, max_health)
        self.defense = defense 
    
    def get_class_name(self):
        return super().get_class_name()
    
    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("Damage cannot be negative.")
        damage = max(1, amount - self.defense) #min damage is 1, negative values still return as 1
        return super().take_damage(damage) #moves back to the original method so we can access .__health
        
    
    def special_move(self, target, effect=2):
        self.attack(target, effect)
        self.power_name = "Power Strike"
        
        
    def display_info(self):
        super().display_info()
        print(f"Defense: {self.defense}")

#Mage child class 
class Mage(Character):
    def __init__(self, name, attack_power, max_health, mana=50):
        super().__init__(name, attack_power, max_health)
        self.mana = mana

    def get_class_name(self):
        return super().get_class_name()
    
    def special_move(self, target, effect =3):
        self.power_name = "Fireball"
        if self.mana >= 20:
            self.mana -= 20
            self.attack(target, effect)
        elif self.mana < 20:
            raise NotEnoughManaError(self)
    
    def display_info(self):
        super().display_info()
        print(f"Mana: {self.mana}")

        
# Child class Archer
class Archer(Character):
    def __init__(self, name, attack_power, max_health, arrows =10):
        super().__init__(name, attack_power, max_health)
        self.arrows = arrows
    
    def get_class_name(self):
        return super().get_class_name()

    def display_info(self):
        super().display_info()
        print(f"Arrows: {self.arrows}")
    
    def attack(self, target, effect =1):
        target_survive = target.is_alive()
        self_survive = self.is_alive()
        if self_survive and target_survive:
            if self.arrows > 0:
                self.arrows -= 1
                amount = self.attack_power *effect
            elif self.arrows == 0:
                amount = 2
            target.take_damage(amount)
        else: 
            dead = self if not self_survive else target
            raise CharacterDefeatedError(dead)

    def special_move(self, target, effect=2):
        self.power_name = "Double Shot"
        if self.arrows >= 2:
            self.arrows -= 1
            self.attack(target, effect) 
        else:
            raise NotEnoughArrowsError(self)  
       

