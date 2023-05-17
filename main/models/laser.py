import pygame

from main.constants import LASER_SPRITE_PATH


class Laser(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(LASER_SPRITE_PATH)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self) -> None:
        speed = 8
        self.rect.y -= speed
        if self.rect.bottom < 0:
            pass  # Delete instance

