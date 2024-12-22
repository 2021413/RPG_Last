from Game_ui import LevelSystem

class Player:
    def __init__(self, name, p_class, hp, mana, attack, defense):
        self.name = name
        self.health = hp
        self.max_health = hp
        self.p_class = p_class
        self.mana = mana
        self.max_mana = mana
        self.base_attack = attack
        self.base_defense = defense
        self.attack = attack
        self.defense = defense
        self.inventory = []
        self.equipment = {
            0: None,  # Arme
            1: None,  # Armure
        }
        self.level_system = LevelSystem()
        self.status_bars = {}
        

    def add_item_to_inventory(self, item):
        self.inventory.append(item)

    def equip_item(self, item):
        if item not in self.inventory:
            raise ValueError("L'objet doit être dans l'inventaire pour être équipé.")
        item_type = item.type
        if item_type not in self.equipment:
            raise ValueError("Ce type d'objet ne peut pas être équipé.")

        currently_equipped = self.equipment[item_type]
        if currently_equipped is not None:
            self.unequip_item(currently_equipped)

        if item_type == 0:
            self.attack = self.base_attack
        else:
            self.defense = self.base_defense

        self.equipment[item_type] = item
        self.apply_item_bonus(item)

    def unequip_item(self, item):
        item_type = item.type
        if self.equipment.get(item_type) == item:
            self.remove_item_bonus(item)
            self.equipment[item_type] = None

    def apply_item_bonus(self, item):
        if isinstance(item.type, tuple):  # Plusieurs bonus
            for bonus_type, value in zip(item.type, item.value):
                self.apply_bonus(bonus_type, value)
        else:  # Bonus unique
            self.apply_bonus(item.type, item.value)

        if item.type in [2, 3]:  # 2 = Santé, 3 = Mana
            if item in self.inventory:
                self.inventory.remove(item)

    def unequip_item(self, slot):
        if slot in self.equipment:
            item = self.equipment[slot]
            if isinstance(item.type, tuple):
                for t, v in zip(item.type, item.value):
                    if t == 0:
                        self.attack -= v
                    elif t == 1:
                        self.defense -= v
            else:
                if item.type == 0:
                    self.attack -= item.value
                elif item.type == 1:
                    self.defense -= item.value
            del self.equipment[slot]
            
    def remove_item_bonus(self, item):
        if isinstance(item.type, tuple):
            for bonus_type, value in zip(item.type, item.value):
                self.remove_bonus(bonus_type, value)
        else:
            self.remove_bonus(item.type, item.value)

    def apply_bonus(self, bonus_type, value):
        if bonus_type == 0:    # Attaque
            self.attack += value
        elif bonus_type == 1:  # Défense
            self.defense += value
        elif bonus_type == 2:  # Santé
            self.health = min(self.max_health, self.health + value)
        elif bonus_type == 3:  # Mana
            self.mana = min(self.max_mana, self.mana + value)

    def remove_bonus(self, bonus_type, value):
        if bonus_type == 0:
            self.attack -= value
        elif bonus_type == 1:
            self.defense -= value
        elif bonus_type == 2:
            self.health -= value
        elif bonus_type == 3:
            self.mana -= value

    def gain_xp(self, amount):
        leveled_up = self.level_system.add_xp(amount)
        if leveled_up :
            self.max_health += 10
            self.health = self.max_health
            if self.p_class in ["Mage" , "Paladin"] :
                self.max_mana += 5
                self.mana = self.max_mana
            self.base_attack += 2
            self.base_defense += 1
            self.attack = self.base_attack
            self.defense = self.base_defense
            for item in self.equipment.values():
                if item:
                    self.apply_item_bonus(item)
            return True
        return False