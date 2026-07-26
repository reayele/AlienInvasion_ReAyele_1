from pathlib import Path
import pygame 

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        image_path = Path("Assets") / "images" / 'ship2(no bg).png'
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
    def draw(self):
        self.screen.blit(self.image, self.rect)