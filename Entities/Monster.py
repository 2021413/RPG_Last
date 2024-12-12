class Monster:
    def __init__(self, name, hp, attack, defense, rank):
        self.name = name
        self.health = hp
        self.attack = attack
        self.defense = defense
        self.rank = rank

Boss_final = Monster("ROI Démon Imortel", 2000, 200, 150, "S+")

ranked_monsters = {
    "S": [  # Rang S - Monstres très puissants
        Monster("Dragon Ancien", 1000, 140, 100, "S"),
        Monster("Démon Suprême", 900, 130, 90, "S"),
        Monster("Titan Colossal", 1200, 160, 120, "S"),
        Monster("Phénix", 800, 120, 80, "S"),
        Monster("Seigneur des Tempêtes", 1040, 150, 110, "S"),
    ],
    "A": [  # Rang A - Monstres puissants
        Monster("Chevalier Noir", 600, 100, 70, "A"),
        Monster("Seigneur Vampire", 560, 110, 60, "A"),
        Monster("Hydre à Trois Têtes", 640, 120, 80, "A"),
        Monster("Archidémon", 700, 130, 70, "A"),
        Monster("Géant des Flammes", 660, 120, 80, "A"),
    ],
    "B": [  # Rang B - Monstres moyennement dangereux
        Monster("Géant des Montagnes", 500, 80, 60, "B"),
        Monster("Wyverne", 440, 70, 40, "B"),
        Monster("Golem de Pierre", 560, 60, 100, "B"),
        Monster("Loup Alpha", 400, 70, 30, "B"),
        Monster("Troll des Cavernes", 540, 100, 50, "B"),
    ],
    "C": [  # Rang C - Monstres ordinaires
        Monster("Squelette Guerrier", 300, 40, 20, "C"),
        Monster("Araignée Géante", 320, 50, 30, "C"),
        Monster("Gobelin Berserker", 280, 60, 16, "C"),
        Monster("Ogre Sauvage", 360, 70, 40, "C"),
        Monster("Serpent des Marais", 340, 56, 36, "C"),
    ],
    "D": [  # Rang D - Monstres faibles
        Monster("Slime", 100, 20, 4, "D"),
        Monster("Squelette", 120, 30, 10, "D"),
        Monster("Gobelin", 140, 24, 8, "D"),
        Monster("Chauve-Souris", 80, 16, 4, "D"),
        Monster("Rat Géant", 110, 28, 12, "D"),
    ],
}
