import random
from typing import List, Tuple, Optional

class MapTile:
    def __init__(self, x: int, y: int, is_exit: bool = False):
        """
        Initialise une case de la map
        
        Args:
            x (int): Position x de la case
            y (int): Position y de la case
            is_exit (bool): True si c'est une sortie, False sinon
        """
        self.x = x
        self.y = y
        self.is_exit = is_exit
        self.has_monster = True
        self.visited = False 

class GameMap:
    def __init__(self, difficulty: str):
        """
        Initialise une map pour une zone de difficulté donnée
        
        Args:
            difficulty (str): Niveau de difficulté ('D', 'C', 'B', 'A', 'S')
        """
        self.difficulty = difficulty
        self.size = 3 
        self.current_position = (1, 1)
        self.grid = self.create_map()

    def create_map(self) -> List[List[MapTile]]:
        """Crée une nouvelle map 3x3 avec une sortie aléatoire sur un bord"""
        grid = [[MapTile(x, y) for x in range(self.size)] for y in range(self.size)]
        
        exit_positions = [
            (0, 1),
            (1, 0),
            (1, 2), 
            (2, 1)   
        ]
        exit_x, exit_y = random.choice(exit_positions)
        grid[exit_y][exit_x].is_exit = True
        
        grid[1][1].visited = True
        grid[1][1].has_monster = False
        
        return grid

    def get_current_tile(self) -> MapTile:
        """Retourne la tuile sur laquelle se trouve actuellement le joueur"""
        x, y = self.current_position
        return self.grid[y][x]

    def can_move(self, direction: str) -> bool:
        """
        Vérifie si le mouvement est possible dans la direction donnée
        
        Args:
            direction (str): Direction du mouvement ('up', 'down', 'left', 'right')
        
        Returns:
            bool: True si le mouvement est possible, False sinon
        """
        x, y = self.current_position
        if direction == "up" and y > 0:
            return True
        elif direction == "down" and y < self.size - 1:
            return True
        elif direction == "left" and x > 0:
            return True
        elif direction == "right" and x < self.size - 1:
            return True
        return False

    def move(self, direction: str) -> Tuple[bool, bool]:
        """
        Déplace le joueur dans la direction donnée
        
        Args:
            direction (str): Direction du mouvement ('up', 'down', 'left', 'right')
        
        Returns:
            Tuple[bool, bool]: (mouvement_réussi, case_est_sortie)
        """
        if not self.can_move(direction):
            return False, False

        x, y = self.current_position
        if direction == "up":
            y -= 1
        elif direction == "down":
            y += 1
        elif direction == "left":
            x -= 1
        elif direction == "right":
            x += 1

        self.current_position = (x, y)
        current_tile = self.grid[y][x]
        current_tile.visited = True
        
        return True, current_tile.is_exit

class MapManager:
    def __init__(self):
        """Initialise le gestionnaire de maps avec les différentes zones de difficulté"""
        self.difficulties = ["D", "C", "B", "A", "S"]
        self.current_difficulty_index = 0
        self.current_map = GameMap(self.difficulties[0])

    def get_current_difficulty(self) -> str:
        """Retourne le niveau de difficulté actuel"""
        return self.difficulties[self.current_difficulty_index]

    def advance_to_next_map(self) -> bool:
        """
        Passe à la map suivante si possible
        
        Returns:
            bool: True si une nouvelle map a été créée, False si c'était la dernière
        """
        if self.current_difficulty_index + 1 >= len(self.difficulties):
            return False
            
        self.current_difficulty_index += 1
        self.current_map = GameMap(self.difficulties[self.current_difficulty_index])
        return True

    def has_monster_at_current_position(self) -> bool:
        """Vérifie s'il y a un monstre sur la case actuelle"""
        return self.current_map.get_current_tile().has_monster

    def mark_monster_defeated(self):
        """Marque le monstre de la case actuelle comme vaincu"""
        self.current_map.get_current_tile().has_monster = False