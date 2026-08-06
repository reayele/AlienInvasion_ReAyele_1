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
        """Sets the game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.alien_speed = 3.0
        self.fleet_drop_speed = 10 
        self.fleet_direction = 1
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.6
        self.bullet_speed = 2.5 
        self.bullet_width = 3 
        self.bullet_height = 15 
        self.bullet_color = (60, 50, 60)
        self.bullets_allowed = 3
