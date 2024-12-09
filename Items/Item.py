class Item:
    def __init__(self, name, value, item_type):

        self.name = name
        self.value = value
        self.type = item_type

rank_s_weapon = [
    Item("Épée du Soleil", 120, 0),
    Item("Lance Céleste", 110, 0),
    Item("Arc des Étoiles", 130, 0),
    Item("Hallebarde Céleste", 125, 0),
    Item("Dague des Ombres", 115, 0),
    Item("Faux Divine", 135, 0),
]

rank_a_weapon = [
    Item("Épée de Feu", 90, 0),
    Item("Hache de Guerre", 85, 0),
    Item("Arc Fantôme", 88, 0),
    Item("Lance Ardente", 92, 0),
    Item("Marteau Tempête", 87, 0),
    Item("Faux Spectrale", 93, 0),
]

rank_b_weapon = [
    Item("Épée Enchantée", 70, 0),
    Item("Marteau de Combat", 65, 0),
    Item("Arc Long Renforcé", 68, 0),
    Item("Hache Envoûtée", 72, 0),
    Item("Dague Sombre", 66, 0),
    Item("Bâton Enchanté", 71, 0),
]

rank_c_weapon = [
    Item("Épée de Fer", 40, 0),
    Item("Dague d'Acier", 35, 0),
    Item("Arc Léger", 38, 0),
    Item("Massue Légère", 42, 0),
    Item("Hache Rugueuse", 37, 0),
    Item("Bâton de Chêne", 41, 0),
]

rank_d_weapon = [
    Item("Dague Rouillée", 10, 0),
    Item("Bâton de Bois", 8, 0),
    Item("Arc Improvisé", 15, 0),
    Item("Couteau Usé", 12, 0),
    Item("Hache Fendue", 9, 0),
    Item("Massue Ébréchée", 14, 0),
]

rank_s_armor = [
    Item("Bouclier Divin", 100, 1),
    Item("Armure de la Lumière", 90, 1),
    Item("Cuirasse Mythique", 95, 1),
    Item("Bouclier Éthéré", 98, 1),
    Item("Armure Céleste", 92, 1),
    Item("Cuirasse de l'Élu", 97, 1),
]

rank_a_armor = [
    Item("Bouclier d'Adamantium", 80, 1),
    Item("Armure Runique", 75, 1),
    Item("Plastron de Titane", 70, 1),
    Item("Bouclier de Feu", 78, 1),
    Item("Armure Fantomatique", 73, 1),
    Item("Plastron Runique", 76, 1),
]

rank_b_armor = [
    Item("Bouclier de Mithril", 60, 1),
    Item("Casque de Combat", 55, 1),
    Item("Cuirasse Solide", 50, 1),
    Item("Bouclier Enchanté", 58, 1),
    Item("Casque Renforcé", 52, 1),
    Item("Cuirasse Résistante", 56, 1),
]

rank_c_armor = [
    Item("Bouclier de Bois", 30, 1),
    Item("Casque en Cuir", 25, 1),
    Item("Armure Basique", 20, 1),
    Item("Bouclier Grossier", 28, 1),
    Item("Casque Usagé", 22, 1),
    Item("Armure de Tissu", 24, 1),
]

rank_d_armor = [
    Item("Bouclier Cassé", 5, 1),
    Item("Chapeau Usé", 3, 1),
    Item("Plastron Déchiré", 2, 1),
    Item("Couvre-Chef Endommagé", 4, 1),
    Item("Bouclier Fendu", 6, 1),
    Item("Gilet Élimé", 1, 1),
]

rank_s_potion = [
    Item("Elixir de l'Immortalité", 150, 2),
    Item("Pierre de Vie Éternelle", 140, 2),
    Item("Potion Suprême", 200, 2),
    Item("Elixir de Mana Infinie", 150, 3),
    Item("Pierre d'Esprit Éternelle", 140, 3),
    Item("Potion d'Esprit Suprême", 200, 3),
]

rank_a_potion = [
    Item("Potion de Régénération Avancée", 100, 2),
    Item("Cristal de Résilience", 90, 2),
    Item("Potion Légendaire", 120, 2),
    Item("Potion de Régénération de Mana Avancée", 100, 3),
    Item("Cristal d'Énergie", 90, 3),
    Item("Potion d'Esprit Légendaire", 120, 3),
]

rank_b_potion = [
    Item("Potion de Vie", 75, 2),
    Item("Cristal de Santé", 70, 2),
    Item("Potion Forte", 80, 2),
    Item("Potion de Mana", 75, 3),
    Item("Cristal de Mana", 70, 3),
    Item("Potion Concentrée", 80, 3),
]

rank_c_potion = [
    Item("Potion Mineure", 40, 2),
    Item("Cristal Faible", 35, 2),
    Item("Potion Simple", 45, 2),
    Item("Potion Mineure de Mana", 40, 3),
    Item("Cristal Faible de Mana", 35, 3),
    Item("Potion Simple de Mana", 45, 3),
]

rank_d_potion = [
    Item("Potion Faible", 10, 2),
    Item("Cristal Abîmé", 12, 2),
    Item("Potion Inférieure", 20, 2),
    Item("Potion Faible de Mana", 10, 3),
    Item("Cristal Abîmé de Mana", 12, 3),
    Item("Potion Inférieure de Mana", 20, 3),
]

ranked_items = {
    "S": rank_s_armor + rank_s_potion + rank_s_weapon,
    "A": rank_a_armor + rank_a_potion + rank_a_weapon,
    "B": rank_b_armor + rank_b_potion + rank_b_weapon,
    "C": rank_c_armor + rank_c_potion + rank_c_weapon,
    "D": rank_d_armor + rank_d_potion + rank_d_weapon,
}
