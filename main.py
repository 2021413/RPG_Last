import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
import random
from Entities.Player import *
from Entities.Monster import *
from Spells.Spells import *
from Items.Item import ranked_items
from map_system import MapManager, GameMap, MapTile
from Game_ui import StatusBar, XPBar

class Canvas:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("RPG Game")
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="black")
        self.canvas.pack()
        self.widgets = []

    def create_button(self, width, height, text, x, y, command, **kwargs):
        button = tk.Button(self.root, text=text, width=width // 10, height=height // 20, command=command, bg='#2C3E50', fg='white', **kwargs)
        button.place(x=x, y=y)
        self.widgets.append(button)
        return button

    def create_input(self, x, y, width=20):
        entry = tk.Entry(self.root, width=width, bg='#34495E', fg='white')
        entry.place(x=x, y=y, anchor="nw")
        self.widgets.append(entry)
        return entry

    def display_text(self, text, x, y, font=("Arial", 20), color="white"):
        text_id = self.canvas.create_text(x, y, text=text, fill=color, font=font)
        bbox = self.canvas.bbox(text_id)
        padding = 2
        rect_id = self.canvas.create_rectangle(
            bbox[0]-padding, bbox[1]-padding,
            bbox[2]+padding, bbox[3]+padding,
            fill="black", stipple="gray50"
        )
        self.canvas.tag_lower(rect_id, text_id)

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
        self.player_icons = {}
        self.play()

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
    
    def play(self):
        self.canvas.clear()
        image = Image.open("Assets/play.png")
        resized_image = image.resize((800, 600), Image.Resampling.LANCZOS)
        self.menu_bg = ImageTk.PhotoImage(resized_image)
        self.canvas.canvas.create_image(0, 0, anchor="nw", image=self.menu_bg)
        self.canvas.create_button(80, 40, "Jouer", 320, 300, self.ask_name)

    def ask_name(self):
        self.canvas.clear()
        image = Image.open("Assets/play.png")
        resized_image = image.resize((800, 600), Image.Resampling.LANCZOS)
        self.menu_bg = ImageTk.PhotoImage(resized_image)
        self.canvas.canvas.create_image(0, 0, anchor="nw", image=self.menu_bg)
        self.canvas.display_text("Entrez votre nom :", 380, 150, font=("Arial", 20))
        name_entry = self.canvas.create_input(290, 200)

        def submit_name():
            name = name_entry.get()
            if name:
                self.player_name = name
                self.choose_class(name)
            else:
                self.canvas.display_text("Veuillez entrer un nom valide.", 370, 250, font=("Arial", 12), color="red")

        name_entry.bind('<Return>', lambda event: submit_name())
        self.canvas.create_button(100, 40, "Valider", 320, 300, submit_name)

    def choose_class(self, name):
        self.canvas.clear()
        image = Image.open("Assets/play.png")
        resized_image = image.resize((800, 600), Image.Resampling.LANCZOS)
        self.menu_bg = ImageTk.PhotoImage(resized_image)
        self.canvas.canvas.create_image(0, 0, anchor="nw", image=self.menu_bg)
        self.canvas.display_text(f"Bienvenue {name} ! Choisissez votre classe :", 400, 150, font=("Arial", 20))

        def set_class(class_name):
            classes = {
                "Guerrier": Player(name, "Guerrier", 150, 0, 25, 20),
                "Mage": Player(name, "Mage", 80, 200, 35, 10),
                "Assassin": Player(name, "Assassin", 120, 0, 40, 8),
                "Paladin": Player(name, "Paladin", 140, 100, 20, 15),
            }
            self.player = classes[class_name]
            self.load_images()
            self.show_menu()

        self.canvas.create_button(100, 40, "Guerrier", 220, 250, lambda: set_class("Guerrier"))
        self.canvas.create_button(100, 40, "Mage", 420, 250, lambda: set_class("Mage"))
        self.canvas.create_button(100, 40, "Assassin", 220, 300, lambda: set_class("Assassin"))
        self.canvas.create_button(100, 40, "Paladin", 420, 300, lambda: set_class("Paladin"))

    def load_images(self):
        tile_size = 60
        for class_name in ["Mage", "Assassin", "Guerrier", "Paladin"]:
            img = Image.open(f"Assets/{class_name.lower()}.png")
            img = img.resize((tile_size, tile_size))
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(0.7)
            self.player_icons[class_name] = ImageTk.PhotoImage(img)

        monster_icon_size = int(tile_size * 0.7)
        img = Image.open("Assets/monster.png")
        img = img.resize((monster_icon_size, monster_icon_size))
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(0.7)
        self.monster_icon = ImageTk.PhotoImage(img)

        boss_icon_size = int(tile_size * 0.8)
        img = Image.open("Assets/boss.png")
        img = img.resize((boss_icon_size, boss_icon_size))
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(0.7)
        self.boss_icon = ImageTk.PhotoImage(img)

    def show_menu(self):
        self.close_aux_windows()
        self.canvas.clear()
        class_image = f"Assets/{self.player.p_class.lower()}.png"
        image = Image.open(class_image)
        resized_image = image.resize((800, 600), Image.Resampling.LANCZOS)
        self.menu_bg = ImageTk.PhotoImage(resized_image)
        self.canvas.canvas.create_image(0, 0, anchor="nw", image=self.menu_bg)

        self.canvas.display_text(f"Menu : {self.player.name}, {self.player.p_class}", 360, 100, font=("Arial", 20), color="white")

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


        self.canvas.display_text(f"Zone actuelle : {zone_name}", 400, 50, font=("Arial", 20))

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

        player_image = self.player_icons[self.player.p_class]

        for y in range(current_map.size):
            for x in range(current_map.size):
                tile = current_map.grid[y][x]
                tile_x = start_x + (x * tile_size)
                tile_y = start_y + (y * tile_size)

                color = "#1a1a1a"
                if tile.visited:
                    color = "#2a2a2a"
                if tile.is_exit:
                    color = "#4a1a1a"

                rect_id = self.canvas.canvas.create_rectangle(
                    tile_x, tile_y,
                    tile_x + tile_size, tile_y + tile_size,
                    fill=color, outline="white", stipple="gray50"
                )

                if (x, y) == current_map.current_position:
                    self.canvas.canvas.create_image(
                        tile_x + tile_size / 2,
                        tile_y + tile_size / 2,
                        image=player_image
                    )
                elif tile.has_monster:
                    icon = self.boss_icon if tile.is_exit else self.monster_icon
                    self.canvas.canvas.create_image(
                        tile_x + tile_size / 2,
                        tile_y + tile_size / 2,
                        image=icon
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

        self.canvas.display_text(f"Combat contre {monster.name}", 400, 35, font=("Arial", 24), color="red")
        self.canvas.display_text("MONSTRE", 400, 90, font=("Arial", 20), color="darkred")
        self.canvas.display_text(monster.name, 400, 125, font=("Arial", 16), color="white")
        
        monster_health_bar = StatusBar(self.canvas.canvas, 200, 150, 400, 25, monster.max_health, monster.health, "red")
        
        self.canvas.display_text(f"ATK: {monster.attack}", 300, 190, font=("Arial", 12), color="white")
        self.canvas.display_text(f"DEF: {monster.defense}", 500, 190, font=("Arial", 12), color="white")

        self.canvas.display_text(f"{self.player.name} - {self.player.p_class}", 400, 240, font=("Arial", 20), color="lightblue")

        self.player.status_bars["health"] = StatusBar(
            self.canvas.canvas, 200, 280, 400, 25, self.player.max_health, self.player.health, "lightgreen"
        )

        if self.player.p_class in ["Mage", "Paladin"]:
            self.player.status_bars["mana"] = StatusBar(
                self.canvas.canvas, 200, 320, 400, 25, self.player.max_mana, self.player.mana, "blue"
            )

        player_health_bar = self.player.status_bars.get("health")
        player_health_bar.update(self.player.health)

        if self.player.p_class in ["Mage", "Paladin"]:
            player_mana_bar = self.player.status_bars.get("mana")
            player_mana_bar.update(self.player.mana)

        xp_bar = XPBar(self.canvas.canvas, 200, 360, 400, 25, self.player.level_system)
        
        self.canvas.display_text(f"ATK: {self.player.attack}", 300, 400, font=("Arial", 12), color="white")
        self.canvas.display_text(f"DEF: {self.player.defense}", 500, 400, font=("Arial", 12), color="white")

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

        attack_button = self.canvas.create_button(80, 40, "Attaquer", 100, 485, attack)
        spells_button = self.canvas.create_button(80, 40, "Sort", 275, 485, lambda: self.show_spells(monster))
        inventory_button = self.canvas.create_button(80, 40, "Inventaire", 450, 485, lambda: self.show_inventory(monster))
        flee_button = self.canvas.create_button(80, 40, "Fuir", 625, 485, self.current_zone)
    
    def end_combat(self, victory, monster):
        self.close_aux_windows()
        self.canvas.clear()

        if victory and not monster.rank == "S+":
            xp_gains = {
                "S": 500,
                "A": 250,
                "B": 150,
                "C": 100,
                "D": 50
            }
            xp_gained = xp_gains.get(monster.rank, 50)
            leveled_up = self.player.gain_xp(xp_gained)
            image = Image.open("Assets/chest.png")
            resized_image = image.resize((800, 600), Image.Resampling.LANCZOS)
            self.chest_bg = ImageTk.PhotoImage(resized_image)
            self.canvas.canvas.create_image(0, 0, anchor="nw", image=self.chest_bg)

            self.canvas.display_text(f"Vous avez vaincu {monster.name} et un coffre apparait !", 400, 150, font=("Arial", 16), color="lime")
            self.canvas.display_text(f"XP gagnée : {xp_gained}", 400, 190, font=("Arial", 16), color="yellow")
            
            if leveled_up:
                self.canvas.display_text(f"Niveau supérieur ! Vous êtes maintenant niveau {self.player.level_system.level}", 400, 230, color="gold")
            
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
                self.canvas.display_text(f"Loot {idx}: {item.name}", 400, 250 + idx * 30, font=("Arial", 12), color="white")
            
            self.map_manager.mark_monster_defeated()
            current_tile = self.map_manager.current_map.get_current_tile()

            if current_tile.is_exit:
                self.canvas.display_text("Vous pouvez maintenant passer à la zone suivante !", 400, 415, color="lime")
                if self.map_manager.advance_to_next_map():
                    self.zone = self.map_manager.get_current_difficulty()
                    self.canvas.create_button(120, 40, "Zone suivante", 340, 520, self.current_zone)
                else:
                    self.canvas.create_button(120, 40, "Terminer", 340, 520, self.end_game)
            else:
                self.canvas.create_button(120, 40, "Continuer", 340, 520, self.current_zone)
        elif victory and monster.rank == "S+":
            self.canvas.display_text(f"Vous avez fini le jeux brave avanturier !", 400, 50, font=("Arial Black", 20,"bold"), color="green")
            self.canvas.create_button(120, 40, "Quitter", 360, 525, self.canvas.root.destroy)
        else:
            self.canvas.display_text(f"Vous avez été vaincu par {monster.name}.", 400, 50, color="red")
            self.canvas.create_button(120, 40, "Quitter", 360, 525, self.canvas.root.destroy)

    def show_inventory(self, monster=None):
        self.close_aux_windows()

        inventory_window = tk.Toplevel(self.canvas.root)
        inventory_window.title("Inventaire")
        inventory_window.configure(bg='#2C3E50')

        x = self.main_window_x - 425
        y = self.main_window_y
        inventory_window.geometry(f"400x600+{x}+{y}")
        inventory_window.resizable(False, False)
        self.aux_windows.append(inventory_window)

        inventory_canvas = tk.Canvas(inventory_window, width=400, height=400, bg='#2C3E50')
        inventory_canvas.pack()

        inventory_canvas.create_text(200, 20, text="Inventaire", font=("Arial", 16), fill="white")

        item_buttons = {}

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

                    if monster:
                        if "health" in self.player.status_bars:
                            self.player.status_bars["health"].update(self.player.health)
                        if "mana" in self.player.status_bars:
                            self.player.status_bars["mana"].update(self.player.mana)
                        self.update_combat_status(monster)
                        self.show_inventory(monster)
                    else:
                        self.show_inventory()

                item_button = tk.Button(
                    inventory_window,
                    text=item_description,
                    command=use_item,
                    width=40,
                    height=1,
                    bg='#34495E',
                    fg='white'
                )
                item_button.place(x=25, y=y_position)
                item_buttons[y_position] = item_button

                if item != self.player.equipment.get(0) and item != self.player.equipment.get(1):
                    delete_button = tk.Button(
                        inventory_window,
                        text="❌",
                        fg="red",
                        bg='#34495E',
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
            if monster:
                self.show_inventory(monster)
            else:
                self.show_inventory()

        refresh_inventory()

    def show_spells(self, monster=None):
        self.close_aux_windows()
        if self.player.p_class not in spells:
            self.canvas.display_text("Votre classe ne peut pas utiliser de sorts.", 400, 580, font=("Arial", 14), color="red")
            return

        spells_window = tk.Toplevel(self.canvas.root)
        spells_window.title("Sorts")
        spells_window.configure(bg='#2C3E50')

        x = self.main_window_x + 825
        y = self.main_window_y
        spells_window.geometry(f"400x600+{x}+{y}")
        spells_window.resizable(False, False)
        self.aux_windows.append(spells_window)

        spells_canvas = tk.Canvas(spells_window, width=400, height=600, bg='#2C3E50')
        spells_canvas.pack()

        spells_canvas.create_text(200, 20, text="Sorts Disponibles", font=("Arial", 16), fill="white")

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
                    self.canvas.display_text("Pas assez de mana !", 400, 580, font=("Arial", 14), color="red")
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
                bg='#34495E',
                fg='white'
            )
            spell_button.place(x=20, y=y_position)
            y_position += 40

        close_button = tk.Button(spells_window, text="Fermer", command=spells_window.destroy, width=20, bg='#34495E', fg='white')
        close_button.place(x=120, y=y_position + 20)

    def change_zone(self):
        zones = ["D", "C", "B", "A", "S"]
        current_index = zones.index(self.zone)
        if current_index + 1 < len(zones):
            self.zone = zones[current_index + 1]
            self.current_zone()
        else:
            self.canvas.clear()
            self.canvas.display_text("Vous avez atteint la dernière zone !", 400, 300, color="gold")
            self.canvas.create_button(120, 40, "Retour au menu", 340, 400, self.show_menu)

    def end_game(self):
        self.canvas.clear()
        self.canvas.display_text(
            "Félicitations ! Vous avez terminé toutes les zones !",
            400, 300, color="gold"
        )
        self.canvas.create_button(120, 40, "Retour au menu", 340, 400, self.show_menu)


def main():
    Game().canvas.run()


if __name__ == "__main__":
    main()