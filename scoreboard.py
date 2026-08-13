"""
Program Name: Scoreboard
Author: Rediet Ayele
Purpose: the scoring of the game 
Date: August 10, 2026

Asset Attribution: 
Font: Bitcount Prop Single 
Link: [https://fonts.google.com/selection?preview.script=Latn]
"""
import pygame.font
from pygame.sprite import Group
from ship import Ship
import pygame
from pathlib import Path
class ScoreBoard: 
    """Displays the games scoring"""
    def __init__(self, ai_game):
        """turns the score into an image"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings 
        self.stats = ai_game.stats 
        self.text_color = (255, 255, 255)
        project_folder = Path(__file__).resolve().parent
        font_path = (
            project_folder
            / "Assets"
            / "Fonts"
            / "SilkScreen"
            / "BitcountPropSingle-VariableFont_CRSV,ELSH,ELXP,slnt,wght.ttf"
        )

        self.font = pygame.font.Font(font_path, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    def prep_score(self):
        """Turns the score into an image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, 
            True, 
            self.text_color, 
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20 
    def prep_high_score(self):
        """Turn the high score into an image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"

        self.high_score_image = self.font.render(
            high_score_str,
            True,
            self.text_color
    )

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20
    def prep_level(self):
        """Turn the level into an image."""
        level_str = str(self.stats.level)

        self.level_image = self.font.render(
            level_str,
            True,
            self.text_color
    )
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    def show_score(self):
        """draws the score, level, lives and the highscore"""
        self.screen.blit(
            self.score_image, 
            self.score_rect
        )
        self.screen.blit(
            self.high_score_image, 
            self.high_score_rect
        )
        self.screen.blit(
            self.level_image, 
            self.level_rect
        )
        self.ships.draw(self.screen)
    def check_high_score(self):
        """checks for a new highscore"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    def prep_ships(self):
        """shows how many lived the dino has"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.image = pygame.transform.scale(ship.image, (50,50))
            ship.rect = ship.image.get_rect()
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10 
            self.ships.add(ship)