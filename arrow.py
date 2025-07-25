import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Arrow:
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        self.game = game 
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.arrow_file)
        self.image = pygame.transform.scale(self.image, (self.settings.arrow_w, self.settings.arrow_h))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        self.arsenal = arsenal

    def update (self):
        #updated the position of the arrow
        self._update_arrow_movement()
        self.arsenal.update_arsenal()

    def _update_arrow_movement(self):
        temp_speed = 5
        if self.moving_right:
            self.x += temp_speed
        if self.moving_left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet()

