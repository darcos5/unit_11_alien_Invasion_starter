import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Arrow:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game 
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.arrow_file)
        self.image = pygame.transform.scale(self.image, (self.settings.arrow_w, self.settings.arrow_h))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def draw(self):
        self.screen.blit(self.image, self.rect)

