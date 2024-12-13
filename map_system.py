import random
from typing import List, Tuple, Optional

class MapTile:
    def __init__(self, x: int, y: int, is_exit: bool = False):
        self.x = x
        self.y = y
        self.is_exit = is_exit
        self.has_monster = True
        self.visited = False 

class GameMap:
    def __init__(self, difficulty: str):
        self.difficulty = difficulty
        self.size = self._get_map_size(difficulty)
        self.current_position = (self.size // 2, self.size // 2)  
        self.grid = self.create_map()

    def _get_map_size(self, difficulty: str) -> int:
        sizes = {
            "D": 3, 
            "C": 4,  
            "B": 5,  
            "A": 5,  
            "S": 5  
        }
        return sizes.get(difficulty, 3)

    def create_map(self) -> List[List[MapTile]]:
        grid = [[MapTile(x, y) for x in range(self.size)] for y in range(self.size)]
        
        exit_positions = []
        for i in range(self.size):
            if i not in [0, self.size-1]: 
                exit_positions.extend([
                    (0, i),     
                    (i, 0),     
                    (i, self.size-1),
                    (self.size-1, i) 
                ])
        
        exit_x, exit_y = random.choice(exit_positions)
        grid[exit_y][exit_x].is_exit = True
        
        center = self.size // 2
        grid[center][center].visited = True
        grid[center][center].has_monster = False
        
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