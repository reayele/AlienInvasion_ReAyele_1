"""
Program Name: Extinction? Not Today? 
Author: Rediet Ayele
Purpose: Creates a reusable play button
date: August 9, 2026

Asset Attribution: 
Play button: play.png
Link: [https://creazilla.com/media/icon/3411680/rounded-green-play-button-right]
"""
from pathlib import Path
import pygame
class Button: 
    """creats and displays the play button"""
    def __init__(self, ai_game, msg):
        """runs the play button"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        project_folder = Path(__file__).resolve().parent
        button_path = (
            project_folder
            / "Assets"
            / "images"
            / "play.png"
        )
        self.image = pygame.image.load(button_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        
    def draw_button(self):
        """draws the button"""
        self.screen.blit(self.image, self.rect )