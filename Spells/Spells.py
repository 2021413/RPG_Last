class Spell:
    def __init__(self, name, mana_cost, damage=0, heal=0, effect=None):
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
        self.heal = heal
        self.effect = effect  # Exemple : "stun", "burn", "shield"

# Liste des sortilèges
spells = {
    "Mage": [
        Spell("Boule de Feu", 30, damage=50),
        Spell("Éclair", 20, damage=40),
        Spell("Explosion de Glace", 40, damage=60),
        Spell("Orage", 35, damage=55),
        Spell("Lance Arcanique", 25, damage=45),
        Spell("Nova de Feu", 50, damage=80),
        Spell("Sphère de Plasma", 30, damage=50, effect="burn"),
        Spell("Guérison Mineure", 20, heal=30),
        Spell("Régénération", 30, heal=50),
        Spell("Bouclier Magique", 25, effect="shield"),
    ],
    "Paladin": [
        Spell("Soin", 20, heal=40),
        Spell("Régénération Sacrée", 30, heal=60),
        Spell("Bénédiction de Vie", 25, heal=50,),
        Spell("Aura de Lumière", 40, heal=70),
        Spell("Protection Sacrée", 30, effect="shield"),
        Spell("Mur de Lumière", 35, effect="shield"),
        Spell("Prière de Rédemption", 20, heal=30),
        Spell("Châtiment Divin", 35, damage=45),
        Spell("Frappe de Lumière", 50, damage=70),
        Spell("Colère Divine", 40, damage=60),
    ],
}

