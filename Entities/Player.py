class Player:
    def __init__(self, name, p_class, hp, mana, attack, defense):
        self.name = name
        self.p_class = p_class
        self.health = hp
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.inventory = []
        self.equipment = {
            0: None,  # Arme
            1: None,  # Armure
        }

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

        self.equipment[item_type] = item
        self.apply_item_bonus(item)

    def unequip_item(self, item):
        item_type = item.type
        if self.equipment.get(item_type) == item:
            self.remove_item_bonus(item)
            self.equipment[item_type] = None
        else:
            pass

    def apply_item_bonus(self, item):
        if isinstance(item.type, tuple):
            for bonus_type, value in zip(item.type, item.value):
                self.apply_bonus(bonus_type, value)
        else:
            self.apply_bonus(item.type, item.value)

    def remove_item_bonus(self, item):
        if isinstance(item.type, tuple):
            for bonus_type, value in zip(item.type, item.value):
                self.remove_bonus(bonus_type, value)
        else:
            self.remove_bonus(item.type, item.value)

    def apply_bonus(self, bonus_type, value):
        if bonus_type == 0:  # Attaque
            self.attack += value
        elif bonus_type == 1:  # Défense
            self.defense += value
        elif bonus_type == 2:  # Santé
            self.health += value
        elif bonus_type == 3:  # Mana
            self.mana += value

    def remove_bonus(self, bonus_type, value):
        if bonus_type == 0:
            self.attack -= value
        elif bonus_type == 1:
            self.defense -= value
        elif bonus_type == 2:
            self.health -= value
        elif bonus_type == 3:
            self.mana -= value
