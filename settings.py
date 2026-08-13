"""
Program Name: Alien Invasion
Author: Rediet Ayele
Purpose: The settings file
Starter Code: Python Crash Course, 3rd Edition by Eric Matthes
Date: August 5, 2026
"""
class Settings:
    """Class stores the game settings"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_limit = 3
        
        self.bullet_width = 3 
        self.bullet_height = 15 
        self.bullet_color = (60, 50, 60)
        self.bullets_allowed = 3
        self.fleet_drop_speed = 30
        self.speedup_scale = 1.25
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        """Set the settings that can change during the game."""
        self.alien_speed = 2.0
        self.fleet_direction = 1
        self.ship_speed = 1.6
        self.bullet_speed = 2.5

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale 
        self.bullet_speed *= self.speedup_scale 
        self.alien_speed *= self.speedup_scale
    
    
    
    
    
    
    

