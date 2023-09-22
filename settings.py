class Settings():
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize game settings"""
        self.name = "Alien Invasion"
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (128, 135, 138)
        # Ship Settings
        self.ship_speed_factor = 3.5
        # Bullet Settings
        self.bullet_speed_factor = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (5, 5, 5)
        self.bullets_allowed = 10