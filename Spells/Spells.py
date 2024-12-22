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
        Spell("Boule de Feu", 25, damage=40),
        Spell("Éclair", 20, damage=35),
        Spell("Explosion de Glace", 35, damage=55),
        Spell("Orage", 30, damage=45),
        Spell("Lance Arcanique", 22, damage=38),
        Spell("Nova de Feu", 45, damage=70),
        Spell("Sphère de Plasma", 35, damage=50, effect="burn"),
        Spell("Guérison Mineure", 20, heal=25),
        Spell("Régénération", 30, heal=40),
        Spell("Bouclier Magique", 25, effect="shield"),
    ],
    "Paladin": [
        Spell("Soin", 20, heal=30),
        Spell("Régénération Sacrée", 35, heal=50),
        Spell("Bénédiction de Vie", 25, heal=35,),
        Spell("Aura de Lumière", 40, heal=60),
        Spell("Protection Sacrée", 30, effect="shield"),
        Spell("Mur de Lumière", 35, effect="shield"),
        Spell("Prière de Rédemption", 20, heal=25),
        Spell("Châtiment Divin", 30, damage=40),
        Spell("Frappe de Lumière", 40, damage=55),
        Spell("Colère Divine", 35, damage=45),
    ],
}