class StatusBar:
    def __init__(self, canvas, x, y, width, height, max_value, current_value, color, bg_color="gray"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_value = max_value
        self.current_value = current_value
        self.color = color
        self.bg_color = bg_color
        
        self.background = canvas.create_rectangle(x, y, x + width, y + height, 
                                               fill=bg_color, outline="black")
        self.bar = canvas.create_rectangle(x, y, x + (current_value/max_value) * width, 
                                         y + height, fill=color, outline="")
        self.text = canvas.create_text(x + width/2, y + height/2, 
                                     text=f"{current_value}/{max_value}", 
                                     fill="white", font=("Arial", 10, "bold"))
        
    def update(self, current_value):
        self.current_value = min(current_value, self.max_value)
        bar_width = (self.current_value/self.max_value) * self.width
        self.canvas.coords(self.bar, self.x, self.y, self.x + bar_width, self.y + self.height)
        self.canvas.itemconfig(self.text, text=f"{int(self.current_value)}/{self.max_value}")

class LevelSystem:
    def __init__(self, base_xp=100, level_multiplier=1.5):
        self.level = 1
        self.current_xp = 0
        self.base_xp = base_xp
        self.level_multiplier = level_multiplier
        
    def xp_required_for_level(self, level):
        return int(self.base_xp * (self.level_multiplier ** (level - 1)))
    
    def add_xp(self, amount):
        self.current_xp += amount
        while self.current_xp >= self.xp_required_for_level(self.level):
            self.current_xp -= self.xp_required_for_level(self.level)
            self.level += 1
            return True 
        return False
    
    def get_progress_percentage(self):
        xp_for_level = self.xp_required_for_level(self.level)
        return (self.current_xp / xp_for_level) * 100

class XPBar(StatusBar):
    def __init__(self, canvas, x, y, width, height, level_system):
        super().__init__(canvas, x, y, width, height, 
                        level_system.xp_required_for_level(level_system.level),
                        level_system.current_xp, "gold", "#444444")
        self.level_text = canvas.create_text(x - 50, y + height/2,
                                           text=f"Niv.{level_system.level}",
                                           fill="white", font=("Arial", 12, "bold"))
        
    def update_level(self, level_system):
        self.max_value = level_system.xp_required_for_level(level_system.level)
        self.current_value = level_system.current_xp
        self.canvas.itemconfig(self.level_text, text=f"Niv.{level_system.level}")
        super().update(self.current_value)