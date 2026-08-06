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
        
        self.image = pygame.Surface((70, 70))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.x = float(self.rect.x)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.image = pygame.transform.rotate(self.image, 70)