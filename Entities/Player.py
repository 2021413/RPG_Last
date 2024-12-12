class Player:
    def __init__(self, name, p_class, hp, mana, attack, defense):
        self.name = name
        self.p_class = p_class
        self.health = hp
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.inventory = []

        # Slots d'équipement (0 = arme, 1 = armure)
        self.equipment = {
            0: None,  # Arme
            1: None,  # Armure
        }

    def add_item_to_inventory(self, item):
        """Ajoute un objet à l'inventaire."""
        self.inventory.append(item)

    def equip_item(self, item):
        """
        Équipe un objet déjà présent dans l'inventaire.
        Si un objet du même type est déjà équipé, il est d'abord déséquipé.
        Applique les bonus de l'objet équipé.
        """
        # Vérifier que l'objet est dans l'inventaire
        if item not in self.inventory:
            raise ValueError("L'objet doit être dans l'inventaire pour être équipé.")

        item_type = item.type
        if item_type not in self.equipment:
            raise ValueError("Ce type d'objet ne peut pas être équipé.")

        currently_equipped = self.equipment[item_type]
        if currently_equipped is not None:
            # Déséquiper l'objet actuellement équipé du même type
            self.unequip_item(currently_equipped)

        # Équiper le nouvel objet
        self.equipment[item_type] = item
        self.apply_item_bonus(item)

    def unequip_item(self, item):
        """
        Déséquipe un objet et retire ses bonus,
        mais ne le retire pas de l'inventaire.
        """
        # Vérifier que l'objet est bien équipé
        item_type = item.type
        if self.equipment.get(item_type) == item:
            # Retirer ses bonus
            self.remove_item_bonus(item)
            # Libérer le slot d'équipement
            self.equipment[item_type] = None
        else:
            # Si l'objet n'était pas équipé, ne rien faire
            pass

    def apply_item_bonus(self, item):
        """
        Applique les bonus de l'objet.
        """
        if isinstance(item.type, tuple):
            for bonus_type, value in zip(item.type, item.value):
                self.apply_bonus(bonus_type, value)
        else:
            self.apply_bonus(item.type, item.value)

    def remove_item_bonus(self, item):
        """
        Retire les bonus de l'objet (inverse de apply_item_bonus).
        """
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
