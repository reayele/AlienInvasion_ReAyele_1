"""
Program Name: Extinction? Not Today.
Author: Rediet Ayele
Purpose: Stores and resets the games lives, score, and level. 
Starter code: python crash course, 3rd editon by eric matthes
Date: August 10, 2026 

"""

class GameStats: 
    """tracks the numbers for the game"""
    def __init__(self, ai_game):
        """initializes the games statisitic"""
        self.settings = ai_game.settings 
        self.reset_stats()
        self.high_score = 0 
    def reset_stats(self):
        """Resets the games lives, score and level """
        self.ships_left = self.settings.ship_limit 
        self.score = 0 
        self.level = 1