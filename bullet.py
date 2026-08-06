from pathlib import Path
import pygame
from pygame.sprite import Sprite
"""
Program Name: Alien Invasion
Author: Rediet Ayele
Purpose: Controls the bullets/rocks being thrown at the meteors
Starter Code: Python Crash Course, 3rd Edition by Eric Matthes
Date: August 5, 2026
"""
class Bullet(Sprite):
    """A class that manages the laser"""
    def __init__(self, ai_game):
        """Creates a new laser"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        project_folder = Path(__file__).resolve().parent
        image_path = (
            project_folder
            / "Assets"
            / "images"
            / "rock.png"
        )
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.midbottom = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Move the laser up the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = int(self.y)

    def draw_bullet(self):
        """Puts or Draw the laser on the screen"""
        self.screen.blit(self.image, self.rect)