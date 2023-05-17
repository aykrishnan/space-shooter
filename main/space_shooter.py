import pygame
from pygame.locals import *

from constants import BACKGROUND_SPRITE_PATH, SCREEN_WIDTH, SCREEN_HEIGHT
from models import Laser, Spaceship

clock = pygame.time.Clock()
fps = 60

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Shooter')

background = pygame.image.load(BACKGROUND_SPRITE_PATH)


def draw_background():
    screen.blit(background, (0, 0))


spaceship_group = pygame.sprite.Group()
spaceship = Spaceship(int(SCREEN_WIDTH / 2), SCREEN_HEIGHT - 100)
spaceship_group.add(spaceship)

laser_group = pygame.sprite.Group()

run = True
while run:
    clock.tick(fps)
    draw_background()

    # key = pygame.key.get_pressed()
    # if key[pygame.K_w]:
    #     rectangle.move_ip(0, -1)
    # if key[pygame.K_s]:
    #     rectangle.move_ip(0, 1)
    # elif key[pygame.K_a]:
    #     rectangle.move_ip(-1, 0)
    # elif key[pygame.K_d]:
    #     rectangle.move_ip(1, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update spaceship
    spaceship.update()

    # Update sprite groups
    laser_group.update()

    # Draw sprite groups
    spaceship_group.draw(screen)
    laser_group.draw(screen)

    pygame.display.update()

pygame.quit()
