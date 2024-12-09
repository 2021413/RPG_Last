class Player:
    def __init__(self, name, p_class, hp, mana, attack, defense):
        self.name = name
        self.health = hp
        self.p_class = p_class
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.inventory = []

    def add_item(self, item):
        if isinstance(item.type, tuple):
            for bonus_type, value in zip(item.type, item.value):
                self.apply_bonus(bonus_type, value)
        else:
            self.apply_bonus(item.type, item.value)

    def apply_bonus(self, bonus_type, value):
        if bonus_type == 0:  # Attaque
            self.attack += value
        elif bonus_type == 1:  # Défense
            self.defense += value
        elif bonus_type == 2:  # Santé
            self.health += value
        elif bonus_type == 3:  # Mana
            self.mana += value

