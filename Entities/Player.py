class Player:
    def __init__(self, name, p_class, hp, mana, attack, defense):
        self.name = name
        self.health = hp
        self.max_health = hp  # Ajout des stats max
        self.p_class = p_class
        self.mana = mana
        self.max_mana = mana
        self.base_attack = attack  # Stats de base
        self.base_defense = defense
        self.attack = attack
        self.defense = defense
        self.inventory = []
        self.equipped_weapon = None  # Équipement actuel
        self.equipped_armor = None

    def add_item(self, item):
        if isinstance(item.type, tuple):
            for bonus_type, value in zip(item.type, item.value):
                self.apply_bonus(bonus_type, value)
        else:
            if item.type == 0:  # Arme
                # Retirer d'abord les bonus de l'arme précédente
                self.attack = self.base_attack
                if self.equipped_weapon:
                    self.equipped_weapon = None
                self.equipped_weapon = item
                self.attack += item.value
            
            elif item.type == 1:  # Armure
                # Retirer d'abord les bonus de l'armure précédente
                self.defense = self.base_defense
                if self.equipped_armor:
                    self.equipped_armor = None
                self.equipped_armor = item
                self.defense += item.value
            
            else:  # Consommables
                self.apply_bonus(item.type, item.value)

    def apply_bonus(self, bonus_type, value):
        if bonus_type == 2:  # Santé
            self.health = min(self.max_health, self.health + value)
        elif bonus_type == 3:  # Mana
            self.mana = min(self.max_mana, self.mana + value)