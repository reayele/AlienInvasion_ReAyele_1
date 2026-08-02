from pathlib import Path
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        project_folder = Path(__file__).resolve().parent
        image_path = (
            project_folder
            / "Assets"
            / "images"
            / "meteor.png")
        
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.iage.get_rect()
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height 
        self.x = float(self.rect.x)