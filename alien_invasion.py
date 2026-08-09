import sys
from pathlib import Path
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien 
from button import Button
"""
Program Name: Alien Invasion
Author: Rediet Ayele
Purpose: Alien invasion game but instead a dino extinction, main file. 
Starter Code: Python Crash Course, 3rd Edition by Eric Matthes
Date: August 5, 2026
"""
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
        self.game_active = False 
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the game's main loop"""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)
    def _update_aliens(self):
        """Updates the meteros and checks for the dino collosions"""
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(
            self.ship,
            self.aliens
        ):
            self._ship_hit()
    def _ship_hit(self):
        """Resests the game after a meteor hits the dino."""
        self.bullets.empty()
        self.aliens.empty()
        self._create_fleet()

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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _create_fleet(self):
        """creats the meteor shower"""
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
        """Creats one meteor"""
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
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
    def _update_bullets(self):
        """Update lasers and check for meteor collisons"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        pygame.sprite.groupcollide(
            self.bullets,
            self.aliens,
            True, 
            True
        )
    def _check_fleet_edges(self):
        """Checks if any of the meteors reaches an edge"""
        for alien in self.aliens.sprites():
                if alien.check_edges():
                    self._change_fleet_direction()
                    break 
    def _change_fleet_direction(self):
        """Moves the meteors down and changes the meteors direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed 
        self.settings.fleet_direction *= -1
        
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()