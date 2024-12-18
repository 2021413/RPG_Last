import tkinter as tk
from PIL import Image, ImageTk
import random
from Entities.Player import *
from Entities.Monster import *
from Spells.Spells import *
from Items.Item import ranked_items
from map_system import MapManager, GameMap, MapTile

class Canvas:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("RPG Game")
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="black")
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

    def display_text(self, text, x, y, font=("bold", 20), color="black"):
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
        self.aux_windows = []
        self.map_manager = MapManager()
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
        image = Image.open("Assets/menu.png")
        resized_image = image.resize((800, 600), Image.Resampling.LANCZOS)
        self.menu_bg = ImageTk.PhotoImage(resized_image)
        self.canvas.canvas.create_image(0, 0, anchor="nw", image=self.menu_bg)
        self.canvas.create_button(80, 40, "Jouer", 320, 300, self.ask_name)

    def ask_name(self):
        self.canvas.clear()

        image = Image.open("Assets/menu.png")
        resized_image = image.resize((800, 600), Image.Resampling.LANCZOS)
        self.menu_bg = ImageTk.PhotoImage(resized_image)
        self.canvas.canvas.create_image(0, 0, anchor="nw", image=self.menu_bg)

        self.canvas.display_text("Entrez votre nom :", 380, 150, font=("bold", 20))
        name_entry = self.canvas.create_input(290, 200)

        def submit_name():
            name = name_entry.get()
            if name:
                self.player_name = name
                self.choose_class(name)
            else:
                self.canvas.display_text("Veuillez entrer un nom valide.", 370, 250, font=("bold", 12), color="red")

        name_entry.bind('<Return>', lambda event: submit_name())

        self.canvas.create_button(100, 40, "Valider", 320, 300, submit_name)

    def choose_class(self, name):
        self.canvas.clear()

        image = Image.open("Assets/menu.png")
        resized_image = image.resize((800, 600), Image.Resampling.LANCZOS)
        self.menu_bg = ImageTk.PhotoImage(resized_image)
        self.canvas.canvas.create_image(0, 0, anchor="nw", image=self.menu_bg)

        self.canvas.display_text(f"Bienvenue {name} ! Choisissez votre classe :", 400, 150, font=("bold", 20))

        def set_class(class_name):
            classes = {
                "Guerrier": Player(name, "Guerrier", 150, 0, 25, 20),
                "Mage": Player(name, "Mage", 50000, 5000, 50000, 5000),
                "Assassin": Player(name, "Assassin", 120, 0, 40, 8),
                "Paladin": Player(name, "Paladin", 140, 100, 20, 15),
            }
            self.player = classes[class_name]
            self.show_menu()

        self.canvas.create_button(100, 40, "Guerrier", 220, 250, lambda: set_class("Guerrier"))
        self.canvas.create_button(100, 40, "Mage", 420, 250, lambda: set_class("Mage"))
        self.canvas.create_button(100, 40, "Assassin", 220, 300, lambda: set_class("Assassin"))
        self.canvas.create_button(100, 40, "Paladin", 420, 300, lambda: set_class("Paladin"))

    def show_menu(self):
        self.close_aux_windows()
        self.canvas.clear()

        image = Image.open("Assets/menu.png")
        resized_image = image.resize((800, 600), Image.Resampling.LANCZOS)
        self.menu_bg = ImageTk.PhotoImage(resized_image)
        self.canvas.canvas.create_image(0, 0, anchor="nw", image=self.menu_bg)

        self.canvas.display_text(f"Menu : {self.player.name}, {self.player.p_class}", 360, 100, font=("bold", 20), color="blue")

        stats = [
            f"HP: {self.player.health}",
            f"Mana: {self.player.mana}",
            f"Attaque: {self.player.attack}",
            f"Défense: {self.player.defense}",
        ]
        for i, stat in enumerate(stats, start=1):
            self.canvas.display_text(stat, 360, 125 + i * 35)

        self.canvas.create_button(100, 40, "Jouer", 310, 300, self.current_zone)
        self.canvas.create_button(100, 40, "Quitter", 310, 400, self.canvas.root.destroy)

    def current_zone(self):
        self.close_aux_windows()
        self.canvas.clear()

        zone_images = {
            "D": "Assets/foret_enchantee.png",
            "C": "Assets/grottes_cristallines.png",
            "B": "Assets/marais_putrides.png",
            "A": "Assets/forteresse_ardente.png",
            "S": "Assets/citadelle_celeste.png",
        }

        zones = {
            "D": "Forêt Enchantée",
            "C": "Grottes Cristallines",
            "B": "Marais Putrides",
            "A": "Forteresse Ardente",
            "S": "Citadelle Céleste",
        }
        zone_name = zones.get(self.zone, "Zone Inconnue")
        zone_image_path = zone_images.get(self.zone)

        image = Image.open(zone_image_path)
        image = image.resize((800, 600), Image.Resampling.LANCZOS)
        self.zone_bg = ImageTk.PhotoImage(image)
        self.canvas.canvas.create_image(0, 0, anchor="nw", image=self.zone_bg)

        self.canvas.display_text(f"Zone actuelle : {zone_name}", 400, 50, font=("bold", 20))

        self.draw_map()
        self.create_movement_buttons()
        self.canvas.create_button(120, 40, "Menu", 250, 530, self.show_menu)
        self.canvas.create_button(120, 40, "Inventaire", 450, 530, self.show_inventory)


    def draw_map(self):
        current_map = self.map_manager.current_map
        max_map_size = 5 
        
        canvas_size = 300 
        tile_size = canvas_size // max_map_size
        
        margin = (max_map_size - current_map.size) * tile_size // 2
        start_x = 250 + margin
        start_y = 70 + margin
        

        for y in range(current_map.size):
            for x in range(current_map.size):
                tile = current_map.grid[y][x]
                tile_x = start_x + (x * tile_size)
                tile_y = start_y + (y * tile_size)

                color = "lightgray"
                if tile.visited:
                    color = "white"
                if (x, y) == current_map.current_position:
                    color = "yellow"
                if tile.is_exit:
                    color = "green"

                self.canvas.canvas.create_rectangle(
                    tile_x, tile_y,
                    tile_x + tile_size, tile_y + tile_size,
                    fill=color, outline="black"
                )

                if tile.has_monster:
                    text = "BOSS" if tile.is_exit else "M"
                    font_size = 10 if tile.is_exit else 12

                    self.canvas.canvas.create_text(
                        tile_x + tile_size/2,
                        tile_y + tile_size/2,
                        text=text,
                        font=("Arial", font_size, "bold" if tile.is_exit else "normal")

                    )

    def create_movement_buttons(self):
        def move_player(direction):
            success, is_exit = self.map_manager.current_map.move(direction)

            if success:
                if is_exit and self.map_manager.has_monster_at_current_position():
                    if self.zone == "S":
                        monster = Monster(Boss_final.name, Boss_final.health, 
                                    Boss_final.attack, Boss_final.defense, 
                                    Boss_final.rank)

                    else:
                        zones = ["D", "C", "B", "A", "S"]
                        next_zone_index = zones.index(self.zone) + 1
                        next_zone = zones[next_zone_index]
                        template_monster = random.choice(ranked_monsters[next_zone])
                        monster = Monster(template_monster.name, template_monster.health, 
                                    template_monster.attack, template_monster.defense, 
                                    template_monster.rank)
                    self.start_combat(monster)
                elif is_exit and not self.map_manager.has_monster_at_current_position():
                    if self.map_manager.advance_to_next_map():
                        self.zone = self.map_manager.get_current_difficulty()
                        self.current_zone()
                    else:
                        self.end_game()
                elif self.map_manager.has_monster_at_current_position():
                    template_monster = random.choice(ranked_monsters[self.zone])
                    monster = Monster(template_monster.name, template_monster.health, 
                                template_monster.attack, template_monster.defense, 
                                template_monster.rank)
                    self.start_combat(monster)
                else:
                    self.current_zone()

        self.canvas.create_button(80, 40, "↑", 360, 395, lambda: move_player("up"))
        self.canvas.create_button(80, 40, "↓", 360, 445, lambda: move_player("down"))
        self.canvas.create_button(80, 40, "←", 260, 420, lambda: move_player("left"))
        self.canvas.create_button(80, 40, "→", 460, 420, lambda: move_player("right"))
    

    def start_combat(self, monster):
        self.close_aux_windows()
        self.update_combat_status(monster)

    def update_combat_status(self, monster):
        self.canvas.clear()
        self.canvas.canvas.create_image(0, 0, anchor="nw", image=self.zone_bg)
        self.canvas.display_text(f"Combat contre {monster.name}", 250, 25, font=("bold", 20), color="red")

        self.canvas.display_text("Statistiques du Monstre :", 625, 75, font=("bold", 20), color="darkred")
        self.canvas.display_text(f"Nom : {monster.name}", 600, 105, font=("bold", 20), color="black")
        self.canvas.display_text(f"HP : {monster.health}", 600, 135, font=("bold", 20), color="black")
        self.canvas.display_text(f"Attaque : {monster.attack}", 600, 165, font=("bold", 20), color="black")
        self.canvas.display_text(f"Défense : {monster.defense}", 600, 195, font=("bold", 20), color="black")

        self.canvas.display_text("Statistiques du Joueur :", 175, 290, font=("bold", 20), color="blue")
        self.canvas.display_text(f"Nom : {self.player.name}", 125, 330, font=("bold", 20), color="black")
        self.canvas.display_text(f"HP : {self.player.health}", 125, 360, font=("bold", 20), color="black")
        self.canvas.display_text(f"Mana : {self.player.mana}", 125, 390, font=("bold", 20), color="black")
        self.canvas.display_text(f"Attaque : {self.player.attack}", 125, 420, font=("bold", 20), color="black")
        self.canvas.display_text(f"Défense : {self.player.defense}", 125, 450, font=("bold", 20), color="black")

        def attack():
            damage_to_monster = max(0, self.player.attack - monster.defense)
            monster.health -= damage_to_monster
            damage_to_player = max(0, monster.attack - self.player.defense)
            if monster.health > 0:
                self.player.health -= damage_to_player

            if monster.health <= 0:
                self.end_combat(victory=True, monster=monster)
            elif self.player.health <= 0:
                self.end_combat(victory=False, monster=monster)
            else:
                self.update_combat_status(monster)

        self.canvas.create_button(120, 40, "Attaquer", 75, 525, attack)
        self.canvas.create_button(120, 40, "Sort", 250, 525, lambda: self.show_spells(monster))
        self.canvas.create_button(120, 40, "Inventaire", 425, 525, lambda :self.show_inventory(monster))
        self.canvas.create_button(120, 40, "Fuir", 600, 525, self.current_zone)

    def end_combat(self, victory, monster):
        self.close_aux_windows()
        self.canvas.clear()

        if victory:
            image = Image.open("Assets/chest.png")
            resized_image = image.resize((800, 600), Image.Resampling.LANCZOS)
            self.chest_bg = ImageTk.PhotoImage(resized_image)
            self.canvas.canvas.create_image(0, 0, anchor="nw", image=self.chest_bg)

            self.canvas.display_text(f"Vous avez vaincu {monster.name} et un coffre apparait !", 400, 200, font=("bold", 20), color="green")
            self.player.mana = min(self.player.max_mana, self.player.mana + 10)

            loot = []
            i = 0

            while i < 2:
                item = random.choice(ranked_items[monster.rank])
                if item.type in (0, 1):
                    if item not in self.player.inventory and item not in loot:
                        loot.append(item)
                        i += 1
                elif item.type == 3:
                    if self.player.p_class in ("Mage", "Paladin"):
                        loot.append(item)
                        i += 1
                else:
                    loot.append(item)
                    i += 1

            for idx, item in enumerate(loot, start=1):
                self.player.inventory.append(item)
                self.canvas.display_text(f"Loot {idx}: {item.name}", 400, 215 + idx * 30)
            self.map_manager.mark_monster_defeated()

            current_tile = self.map_manager.current_map.get_current_tile()

            if current_tile.is_exit:
                self.canvas.display_text("Vous pouvez maintenant passer à la zone suivante !", 400, 315, font=("bold", 20), color="green")
                if self.map_manager.advance_to_next_map():
                    self.zone = self.map_manager.get_current_difficulty()
                    self.canvas.create_button(120, 40, "Zone suivante", 340, 520, self.current_zone)
                else:
                    self.canvas.create_button(120, 40, "Terminer", 340, 520, self.end_game)
            else:
                self.canvas.create_button(120, 40, "Continuer", 340, 520, self.current_zone)
        else:
            self.canvas.display_text(f"Vous avez été vaincu par {monster.name}.", 400, 50, font=("bold", 20), color="red")
            self.canvas.create_button(120, 40, "Quitter", 360, 525, self.canvas.root.destroy)

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
                    item_type_name = ["Attaque", "Défense", "Soin", "Mana"][item.type]
                    item_description = f"{item.name} ({item_type_name} +{item.value})"

                if item == self.player.equipment.get(0):
                    item_description += " (arme)"
                elif item == self.player.equipment.get(1):
                    item_description += " (armure)"

                def use_item(item=item):
                    if item.type in (0, 1):
                        self.player.equip_item(item)
                    else:
                        self.player.apply_item_bonus(item)
                        self.player.inventory.remove(item)
                    if monster:
                        self.update_combat_status(monster)
                    self.show_inventory()

                item_button = tk.Button(
                    inventory_window,
                    text=item_description,
                    command=use_item,
                    width=40,
                    height=1,
                )
                item_button.place(x=25, y=y_position)
                item_buttons[y_position] = item_button

                # Ajouter un bouton rouge pour supprimer l'item (si non équipé)
                if item != self.player.equipment.get(0) and item != self.player.equipment.get(1):
                    delete_button = tk.Button(
                        inventory_window,
                        text="❌",
                        fg="red",
                        command=lambda i=item: delete_item(i),
                        width=2,
                        height=1
                    )
                    delete_button.place(x=350, y=y_position)

                y_position += 40

            inventory_height = max(100, len(self.player.inventory) * 40 + 100)
            inventory_canvas.config(height=inventory_height)
            inventory_window.geometry(f"400x{inventory_height}")

        def delete_item(item):
            self.player.inventory.remove(item)
            self.show_inventory()

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
            self.canvas.display_text("Votre classe ne peut pas utiliser de sorts.", 350, 480, font=("Arial", 14), color="red")
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
                    self.canvas.display_text("Pas assez de mana !", 350, 480, font=("Arial", 14), color="red")
                    self.close_aux_windows()
                    return

                self.player.mana -= current_spell.mana_cost
                
                if current_spell.damage > 0 and monster:
                    monster.health -= current_spell.damage
                if current_spell.heal > 0:
                    self.player.health += current_spell.heal
                if monster:
                    damage_to_player = max(0, monster.attack - self.player.defense)
                    self.player.health -= damage_to_player

                if monster and monster.health <= 0:
                    self.end_combat(victory=True, monster=monster)
                elif self.player.health <= 0:
                    self.end_combat(victory=False, monster=monster)
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
            self.canvas.display_text("Vous avez atteint la dernière zone !", 400, 300, font=("bold", 20), color="gold")
            self.canvas.create_button(120, 40, "Retour au menu", 340, 400, self.show_menu)

    def end_game(self):
        self.canvas.clear()
        self.canvas.display_text(
            "Félicitations ! Vous avez terminé toutes les zones !",
            400, 300, font=("bold", 20), color="gold"
        )
        self.canvas.create_button(120, 40, "Retour au menu", 340, 400, self.show_menu)

def main():
    Game().canvas.run()


if __name__ == "__main__":
    main()
