import pygame
from enum import Enum

from main.constants import PLAYER_SPRITE_PATH, SCREEN_HEIGHT, SCREEN_WIDTH
from main.models import Laser


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Spaceship(pygame.sprite.Sprite):
    speed = 8
    fire_delay = 10

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(PLAYER_SPRITE_PATH)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.horizontal_acceleration = 0.0
        self.vertical_acceleration = 0.0
        self.laser_group = pygame.sprite.Group()

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.rect.top > 0:
            self.accelerate(Direction.UP)
            self.rect.y -= Spaceship.speed * self.vertical_acceleration
        elif key[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.accelerate(Direction.DOWN)
            self.rect.y += Spaceship.speed * self.vertical_acceleration

        if key[pygame.K_a] and self.rect.left > 0:
            self.accelerate(Direction.LEFT)
            self.rect.x -= Spaceship.speed * self.horizontal_acceleration
        elif key[pygame.K_d] and self.rect.right < SCREEN_WIDTH:
            self.accelerate(Direction.RIGHT)
            self.rect.x += Spaceship.speed * self.horizontal_acceleration

        if not key[pygame.K_w] and not key[pygame.K_s]:
            self.decelerate(Direction.UP)
        if not key[pygame.K_a] and not key[pygame.K_d]:
            self.decelerate(Direction.LEFT)

    def accelerate(self, direction: Direction):
        match direction:
            case Direction.UP | Direction.DOWN:
                if self.vertical_acceleration < 1.0:
                    self.vertical_acceleration += 0.05
            case Direction.LEFT | Direction.RIGHT:
                if self.horizontal_acceleration < 1.0:
                    self.horizontal_acceleration += 0.05
            case _:
                raise ValueError('Invalid direction')

    def decelerate(self, direction: Direction):
        match direction:
            case Direction.UP | Direction.DOWN:
                if self.vertical_acceleration > 0.0:
                    # self.vertical_acceleration -= 0.02
                    self.vertical_acceleration = 0.0
            case Direction.LEFT | Direction.RIGHT:
                if self.horizontal_acceleration > 0.0:
                    # self.horizontal_acceleration -= 0.02
                    self.horizontal_acceleration = 0.0
            case _:
                raise ValueError('Invalid direction')

    def shoot(self):
        laser = Laser(self.x, self.y)
        self.laser_group.add(laser)
