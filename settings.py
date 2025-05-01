class Settings: 
    """Store all settings"""

    def __init__(self):
        """initialize the game segttings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 6.5

        self.bullet_speed = 8.0
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)