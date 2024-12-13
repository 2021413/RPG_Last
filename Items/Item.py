class Item:
   def __init__(self, name, value, item_type):
       self.name = name
       self.value = value
       self.type = item_type

rank_s_weapon = [
   Item("Épée du Soleil", 80, 0),
   Item("Lance Céleste", 80, 0),
   Item("Arc des Étoiles", 73, 0),
   Item("Hallebarde Céleste", 74, 0),
   Item("Dague des Ombres", 78, 0),
   Item("Faux Divine", 78, 0),
]

rank_a_weapon = [
   Item("Épée de Feu", 60, 0),
   Item("Hache de Guerre", 60, 0),
   Item("Arc Fantôme", 50, 0),
   Item("Lance Ardente", 56, 0),
   Item("Marteau Tempête", 57, 0),
   Item("Faux Spectrale", 58, 0),
]

rank_b_weapon = [
   Item("Épée Enchantée", 43, 0),
   Item("Marteau de Combat", 45, 0),
   Item("Arc Long Renforcé", 40, 0),
   Item("Hache Envoûtée", 44, 0),
   Item("Dague Sombre", 45, 0),
   Item("Bâton Enchanté", 42, 0),
]

rank_c_weapon = [
   Item("Épée de Fer", 30, 0),
   Item("Dague d'Acier", 29, 0),
   Item("Arc Léger", 25, 0),
   Item("Massue Légère", 28, 0),
   Item("Hache Rugueuse", 30, 0),
   Item("Bâton de Chêne", 26, 0),
]

rank_d_weapon = [
   Item("Dague Rouillée", 14, 0),
   Item("Bâton de Bois", 8, 0),
   Item("Arc Improvisé", 13, 0),
   Item("Couteau Usé", 15, 0),
   Item("Hache Fendue", 12, 0),
   Item("Massue Ébréchée", 15, 0),
]

rank_s_armor = [
   Item("Grèves Divines", 70, 1),
   Item("Armure de la Lumière", 70, 1),
   Item("Cuirasse Mythique", 68, 1),
   Item("Brassards Éthérés", 67, 1),
   Item("Armure Céleste", 68, 1),
   Item("Cuirasse de l'Élu", 70, 1),
]

rank_a_armor = [
   Item("Grèves d'Adamantium", 49, 1),
   Item("Armure Runique", 47, 1),
   Item("Plastron de Titane", 50, 1),
   Item("Brassards de Feu", 50, 1),
   Item("Armure Fantomatique", 45, 1),
   Item("Plastron Runique", 46, 1),
]

rank_b_armor = [
   Item("Jambières de Mithril", 35, 1),
   Item("Gants de Combat", 30, 1),
   Item("Cuirasse Solide", 35, 1),
   Item("Grèves Enchantées", 34, 1),
   Item("Brassards Renforcés", 33, 1),
   Item("Cuirasse Résistante", 32, 1),
]

rank_c_armor = [
   Item("Grèves de Bois", 15, 1),
   Item("Gants en Cuir", 18, 1),
   Item("Armure Basique", 19, 1),
   Item("Brassards Grossiers", 20, 1),
   Item("Gants Usagés", 17, 1),
   Item("Armure de Tissu", 16, 1),
]

rank_d_armor = [
   Item("Gants Cassés", 6, 1),
   Item("Gants Usés", 4, 1),
   Item("Plastron Déchiré", 7, 1),
   Item("Brassards Endommagés", 4, 1),
   Item("Grèves Fendues", 9, 1),
   Item("Gilet Élimé", 10, 1),
]

rank_s_potion = [
   Item("Elixir de l'Immortalité", 100, 2),
   Item("Pierre de Vie Éternelle", 110, 2),
   Item("Potion Suprême", 120, 2),
   Item("Elixir de Mana Infinie", 100, 3),
   Item("Pierre d'Esprit Éternelle", 110, 3),
   Item("Potion d'Esprit Suprême", 120, 3),
]

rank_a_potion = [
   Item("Potion de Régénération Avancée", 80, 2),
   Item("Cristal de Résilience", 85, 2),
   Item("Potion Légendaire", 90, 2),
   Item("Potion de Régénération de Mana Avancée", 80, 3),
   Item("Cristal d'Énergie", 85, 3),
   Item("Potion d'Esprit Légendaire", 90, 3),
]

rank_b_potion = [
   Item("Potion de Vie", 60, 2),
   Item("Cristal de Santé", 65, 2),
   Item("Potion Forte", 70, 2),
   Item("Potion de Mana", 60, 3),
   Item("Cristal de Mana", 65, 3),
   Item("Potion Concentrée", 70, 3),
]

rank_c_potion = [
   Item("Potion Mineure", 40, 2),
   Item("Cristal Faible", 42, 2),
   Item("Potion Simple", 50, 2),
   Item("Potion Mineure de Mana", 40, 3),
   Item("Cristal Faible de Mana", 42, 3),
   Item("Potion Simple de Mana", 50, 3),
]

rank_d_potion = [
   Item("Potion Faible", 20, 2),
   Item("Cristal Abîmé", 24, 2),
   Item("Potion Inférieure", 30, 2),
   Item("Potion Faible de Mana", 20, 3),
   Item("Cristal Abîmé de Mana", 25, 3),
   Item("Potion Inférieure de Mana", 30, 3),
]

ranked_items = {
   "S": rank_s_armor + rank_s_potion + rank_s_weapon,
   "A": rank_a_armor + rank_a_potion + rank_a_weapon,
   "B": rank_b_armor + rank_b_potion + rank_b_weapon,
   "C": rank_c_armor + rank_c_potion + rank_c_weapon,
   "D": rank_d_armor + rank_d_potion + rank_d_weapon,
}
