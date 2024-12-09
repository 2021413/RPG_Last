import tkinter as tk
import random
from Entities.Player import *
from Entities.Monster import *
from Spells.Spells import *
from Items.Item import ranked_items


class Canvas:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("RPG Game")
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack()
        self.widgets = []

    def create_button(self, width, height, text, x, y, command):
        button = tk.Button(self.root, text=text, width=width // 10, height=height // 20, command=command)
        button.place(x=x, y=y)
        self.widgets.append(button)

    def create_input(self, x, y, width=20):
        entry = tk.Entry(self.root, width=width)
        entry.place(x=x, y=y, anchor="nw")
        self.widgets.append(entry)
        return entry

    def display_text(self, text, x, y, font=("Arial", 14), color="black"):
        self.canvas.create_text(x, y, text=text, fill=color, font=font)

    def clear(self):
        self.canvas.delete("all")
        for widget in self.widgets:
            widget.destroy()
        self.widgets.clear()

    def run(self):
        self.root.mainloop()


class Game:
    def __init__(self):
        self.canvas = Canvas(800, 600)
        self.center_window(800, 600)
        self.player = None
        self.zone = "D"
        self.zone_monsters = {key: ranked_monsters[key][:] for key in ranked_monsters}
        self.aux_windows = []
        self.start_menu()

    def center_window(self, width, height):
        screen_width = self.canvas.root.winfo_screenwidth()
        screen_height = self.canvas.root.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.canvas.root.geometry(f"{width}x{height}+{x}+{y}")

        self.main_window_x = x
        self.main_window_y = y

    def close_aux_windows(self):
        for window in self.aux_windows:
            if window.winfo_exists():
                window.destroy()
        self.aux_windows.clear()

    def start_menu(self):
        self.canvas.clear()
        self.canvas.create_button(80, 40, "Jouer", 360, 300, self.ask_name)

    def ask_name(self):
        self.canvas.clear()
        self.canvas.display_text("Entrez votre nom :", 400, 150, font=("Arial", 16))
        name_entry = self.canvas.create_input(320, 200)

        def submit_name():
            name = name_entry.get()
            if name:
                self.player_name = name
                self.choose_class(name)
            else:
                self.canvas.display_text("Veuillez entrer un nom valide.", 400, 250, font=("Arial", 12), color="red")

        self.canvas.create_button(100, 40, "Valider", 350, 300, submit_name)

    def choose_class(self, name):
        self.canvas.clear()
        self.canvas.display_text(f"Bienvenue {name} ! Choisissez votre classe :", 400, 150, font=("Arial", 16))

        def set_class(class_name):
            classes = {
                "Guerrier": Player(name, "Guerrier", 180, 40, 20, 20),
                "Mage": Player(name, "Mage", 50000, 5000, 50000, 5000),
                "Assassin": Player(name, "Assassin", 140, 80, 35, 0),
                "Paladin": Player(name, "Paladin", 160, 60, 25, 25),
            }
            self.player = classes[class_name]
            self.show_menu()

        self.canvas.create_button(100, 40, "Guerrier", 250, 250, lambda: set_class("Guerrier"))
        self.canvas.create_button(100, 40, "Mage", 450, 250, lambda: set_class("Mage"))
        self.canvas.create_button(100, 40, "Assassin", 250, 300, lambda: set_class("Assassin"))
        self.canvas.create_button(100, 40, "Paladin", 450, 300, lambda: set_class("Paladin"))

    def show_menu(self):
        self.close_aux_windows()
        self.canvas.clear()
        self.canvas.display_text(f"Menu : {self.player.name}, {self.player.p_class}", 400, 100, font=("Arial", 16), color="blue")  # Recentré
        stats = [
            f"HP: {self.player.health}",
            f"Mana: {self.player.mana}",
            f"Attaque: {self.player.attack}",
            f"Défense: {self.player.defense}",
        ]
        for i, stat in enumerate(stats, start=1):
            self.canvas.display_text(stat, 400, 150 + i * 20)

        self.canvas.create_button(100, 40, "Jouer", 350, 300, self.current_zone)
        self.canvas.create_button(100, 40, "Quitter", 350, 400, self.canvas.root.destroy)

    def current_zone(self):
        self.close_aux_windows()
        self.canvas.clear()
        zones = {
            "D": "Forêt Enchantée",
            "C": "Grottes Cristallines",
            "B": "Marais Putrides",
            "A": "Forteresse Ardente",
            "S": "Citadelle Céleste",
        }
        zone_name = zones.get(self.zone, "Zone Inconnue")
        self.canvas.display_text(f"Zone actuelle : {zone_name}", 400, 100, font=("Arial", 16))

        if not self.zone_monsters[self.zone]:
            self.canvas.display_text("Tous les monstres ont été vaincus.", 400, 200, font=("Arial", 14), color="blue")
            self.canvas.create_button(120, 40, "Changer de Zone", 340, 300, self.change_zone)
            return

        monster = random.choice(self.zone_monsters[self.zone])
        self.zone_monsters[self.zone].remove(monster)

        self.canvas.display_text(f"Monstre : {monster.name} (Rang {monster.rank})", 400, 200, font=("Arial", 14), color="red")
        self.canvas.create_button(120, 40, "Combattre", 340, 250, lambda: self.start_combat(monster))
        self.canvas.create_button(120, 40, "Menu", 340, 300, self.show_menu)
        self.canvas.create_button(120, 40, "Inventaire", 340, 350,self.show_inventory)

    def start_combat(self, monster):
        self.close_aux_windows()
        self.update_combat_status(monster)

    def update_combat_status(self, monster):
        self.canvas.clear()
        self.canvas.display_text(f"Combat contre {monster.name}", 400, 50, font=("Arial", 16), color="red")

        self.canvas.display_text("Statistiques du Monstre :", 200, 100, font=("Arial", 14), color="darkred")
        self.canvas.display_text(f"Nom : {monster.name}", 200, 130, font=("Arial", 12), color="black")
        self.canvas.display_text(f"HP : {monster.health}", 200, 160, font=("Arial", 12), color="black")
        self.canvas.display_text(f"Attaque : {monster.attack}", 200, 190, font=("Arial", 12), color="black")
        self.canvas.display_text(f"Défense : {monster.defense}", 200, 220, font=("Arial", 12), color="black")

        self.canvas.display_text("Statistiques du Joueur :", 600, 100, font=("Arial", 14), color="blue")
        self.canvas.display_text(f"Nom : {self.player.name}", 600, 130, font=("Arial", 12), color="black")
        self.canvas.display_text(f"HP : {self.player.health}", 600, 160, font=("Arial", 12), color="black")
        self.canvas.display_text(f"Mana : {self.player.mana}", 600, 190, font=("Arial", 12), color="black")
        self.canvas.display_text(f"Attaque : {self.player.attack}", 600, 220, font=("Arial", 12), color="black")
        self.canvas.display_text(f"Défense : {self.player.defense}", 600, 250, font=("Arial", 12), color="black")

        def attack():
            damage_to_monster = max(0, self.player.attack - monster.defense)
            monster.health -= damage_to_monster
            damage_to_player = max(0, monster.attack - self.player.defense)
            self.player.health -= damage_to_player

            if monster.health <= 0:
                self.end_combat(victory=True, monster=monster)
            elif self.player.health <= 0:
                self.end_combat(victory=False, monster=monster)
            else:
                self.update_combat_status(monster)

        self.canvas.create_button(120, 40, "Attaquer", 340, 300, attack)
        self.canvas.create_button(120, 40, "Fuir", 340, 350, self.current_zone)
        self.canvas.create_button(120, 40, "Inventaire", 340, 400, lambda :self.show_inventory(monster))
        self.canvas.create_button(120, 40, "Sort", 340, 450, lambda: self.show_spells(monster))

    def end_combat(self, victory, monster):
        self.close_aux_windows()
        self.canvas.clear()
        if victory:
            self.canvas.display_text(f"Vous avez vaincu {monster.name} !", 400, 100, font=("Arial", 16), color="green")
            loot = random.sample(ranked_items[monster.rank], 2)
            for i, item in enumerate(loot, start=1):
                self.player.inventory.append(item)
                self.canvas.display_text(f"Loot {i}: {item.name}", 400, 130 + i * 30)
            self.canvas.create_button(120, 40, "Retour à la zone", 340, 520, self.current_zone)
        else:
            self.canvas.display_text(f"Vous avez été vaincu par {monster.name}.", 250, 50, font=("Arial", 16), color="red")
            self.canvas.create_button(120, 40, "Quitter", 190, 200, self.canvas.root.destroy)

    def show_inventory(self, monster=None):
        self.close_aux_windows()
        def refresh_inventory():
            for button in item_buttons.values():
                button.destroy()
            item_buttons.clear()

            y_position = 60
            for item in self.player.inventory:
                if isinstance(item.type, tuple):
                    item_types = [f"{['Attaque', 'Défense', 'Soin', 'Mana'][t]} +{v}" for t, v in zip(item.type, item.value)]
                    item_description = f"{item.name} ({', '.join(item_types)})"
                else:
                    item_type = ["Attaque", "Défense", "Soin", "Mana"][item.type]
                    item_description = f"{item.name} ({item_type} +{item.value})"

                def use_item(item=item):
                    self.player.add_item(item)
                    self.player.inventory.remove(item)
                    refresh_inventory()
                    if monster:
                        self.update_combat_status(monster)

                item_button = tk.Button(
                    inventory_window,
                    text=item_description,
                    command=use_item,
                    width=40,
                    height=1,
                )
                item_button.place(x=25, y=y_position)
                item_buttons[y_position] = item_button
                y_position += 40

            inventory_height = max(100, len(self.player.inventory) * 40 + 100)
            inventory_canvas.config(height=inventory_height)
            inventory_window.geometry(f"400x{inventory_height}")

        inventory_window = tk.Toplevel(self.canvas.root)
        inventory_window.title("Inventaire")

        x = self.main_window_x - 425
        y = self.main_window_y
        inventory_window.geometry(f"400x600+{x}+{y}")
        inventory_window.resizable(False, False)
        self.aux_windows.append(inventory_window)

        inventory_canvas = tk.Canvas(inventory_window, width=400, height=400, bg="white")
        inventory_canvas.pack()

        inventory_canvas.create_text(200, 20, text="Inventaire", font=("Arial", 16), fill="black")

        item_buttons = {}

        refresh_inventory()

    def show_spells(self, monster=None):
        self.close_aux_windows()
        if self.player.p_class not in spells:
            self.canvas.display_text("Votre classe ne peut pas utiliser de sorts.", 250, 480, font=("Arial", 14), color="red")
            return

        spells_window = tk.Toplevel(self.canvas.root)
        spells_window.title("Sorts")

        x = self.main_window_x + 825
        y = self.main_window_y
        spells_window.geometry(f"400x600+{x}+{y}")
        spells_window.resizable(False, False)
        self.aux_windows.append(spells_window)

        spells_canvas = tk.Canvas(spells_window, width=400, height=600, bg="white")
        spells_canvas.pack()

        spells_canvas.create_text(200, 20, text="Sorts Disponibles", font=("Arial", 16), fill="black")

        y_position = 60
        for spell in spells[self.player.p_class]:
            spell_description = spell.name
            if spell.damage:
                spell_description += f" (Dégâts: {spell.damage})"
            if spell.heal:
                spell_description += f" (Soin: {spell.heal})"
            spell_description += f" (Mana: {spell.mana_cost})"

            def cast_spell(current_spell=spell):
                if self.player.mana < current_spell.mana_cost:
                    self.canvas.display_text("Pas assez de mana !", 250, 480, font=("Arial", 14), color="red")
                    spells_window.destroy()
                    return

                self.player.mana -= current_spell.mana_cost
                if current_spell.damage > 0 and monster:
                    monster.health -= current_spell.damage
                if current_spell.heal > 0:
                    self.player.health += current_spell.heal

                if monster and monster.health <= 0:
                    self.end_combat(victory=True, monster=monster)
                else:
                    self.update_combat_status(monster)

            spell_button = tk.Button(
                spells_window,
                text=spell_description,
                command=cast_spell,
                width=40,
                height=1,
            )
            spell_button.place(x=20, y=y_position)
            y_position += 40

        close_button = tk.Button(spells_window, text="Fermer", command=spells_window.destroy, width=20)
        close_button.place(x=120, y=y_position + 20)

    def change_zone(self):
            zones = ["D", "C", "B", "A", "S"]
            current_index = zones.index(self.zone)
            if current_index + 1 < len(zones):
                self.zone = zones[current_index + 1]
                self.current_zone()
            else:
                self.canvas.clear()
                self.canvas.display_text("Vous avez atteint la dernière zone !", 400, 300, font=("Arial", 16), color="gold")
                self.canvas.create_button(120, 40, "Retour au menu", 340, 400, self.show_menu)


def main():
    Game().canvas.run()


if __name__ == "__main__":
    main()
