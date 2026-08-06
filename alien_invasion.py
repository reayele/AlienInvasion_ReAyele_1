import sys
from pathlib import Path
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien 
class AlienInvasion:
    """The overall class that manges the games behavior"""
    def __init__(self):
        """Sets up the game and its main parts"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Extinction? Not Today. - Track 2")

        project_folder = Path(__file__).resolve().parent
        background_path = (
            project_folder
            / "Assets"
            / "images"
            / "volcano.jpg"
        )

        self.background = pygame.image.load(background_path).convert()

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Start the game's main loop"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """check for game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Checks when a key is pressed"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        """Checks when a key is released"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Creats a new laser"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    def _create_fleet(self):
        positions = [
            (150, 30),
            (280, 45),
            (410, 35),
            (540, 50),
            (670, 40),
            (800, 55),
            (930, 35),

            (220, 110),
            (360, 125),
            (500, 115),
            (640, 130),
            (780, 120),
            (920, 135),

            (300, 190),
            (450, 205),
            (600, 195),
            (750, 210),
            (900, 200),
        ]

        for x, y in positions:
            self._create_alien(x, y)
    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_screen(self):
        """Draws the games objects on the screen"""
        self.screen.blit(self.background, (0, 0))

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()
        


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()