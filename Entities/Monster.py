class Monster:
    def __init__(self, name, hp, attack, defense, rank):
        self.name = name
        self.max_health = hp
        self.health = hp
        self.attack = attack
        self.defense = defense
        self.rank = rank

Boss_final = Monster("ROI Démon Imortel", 1500, 150, 100, "S+")

ranked_monsters = {
    "S": [  # Rang S - Monstres très puissants
        Monster("Dragon Ancien", 970, 125, 70, "S"),
        Monster("Démon Suprême", 840, 130, 75, "S"),
        Monster("Titan Colossal", 1000, 105, 80, "S"),
        Monster("Phénix", 900, 120, 65, "S"),
        Monster("Seigneur des Tempêtes", 870, 105, 60, "S"),
    ],
    "A": [  # Rang A - Monstres puissants
        Monster("Chevalier Noir", 580, 84, 50, "A"),
        Monster("Seigneur Vampire", 540, 90, 42, "A"),
        Monster("Hydre à Trois Têtes", 590, 79, 45, "A"),
        Monster("Archidémon", 560, 85, 40, "A"),
        Monster("Géant des Flammes", 600, 72, 44, "A"),
    ],
    "B": [  # Rang B - Monstres moyennement dangereux
        Monster("Géant des Montagnes", 400, 42, 32, "B"),
        Monster("Wyverne", 340, 55, 29, "B"),
        Monster("Golem de Pierre", 370, 42, 35, "B"),
        Monster("Loup Alpha", 300, 60, 25, "B"),
        Monster("Troll des Cavernes", 355, 47, 27, "B"),
    ],
    "C": [  # Rang C - Monstres ordinaires
        Monster("Squelette Guerrier", 180, 32, 20, "C"),
        Monster("Araignée Géante", 185, 30, 19, "C"),
        Monster("Gobelin Berserker", 175, 40, 15, "C"),
        Monster("Ogre Sauvage", 200, 35, 18, "C"),
        Monster("Serpent des Marais", 170, 30, 15, "C"),
    ],
    "D": [  # Rang D - Monstres faibles
        Monster("Slime", 100, 15, 6, "D"),
        Monster("Squelette", 120, 20, 10, "D"),
        Monster("Gobelin", 110, 25, 8, "D"),
        Monster("Chauve-Souris", 80, 16, 4, "D"),
        Monster("Rat Géant", 90, 18, 5, "D"),
    ],
}
