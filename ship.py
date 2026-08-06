from pathlib import Path
import pygame

class Ship:
    """A class that manges the players custom ship"""
    def __init__(self, ai_game):
        """Creats the players ship"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        project_folder = Path(__file__).resolve().parent
        image_path = (
            project_folder
            / "Assets"
            / "images"
            / "dino.png"
        )

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (250,250))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ships position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """Draws the ship on the screen"""
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        """Centers the Dino"""
        self.rect.midbottom = self.screen_rect.midbottom 
        self.x = float(self.rect.x)