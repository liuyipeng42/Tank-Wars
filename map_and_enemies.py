import pygame
import random
from enemy import Enemy
from pygame.sprite import Sprite


class Wall1(Sprite):
    def __init__(self, screen, centerx, centery):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.wall = pygame.image.load('images/wall1.png').convert_alpha()
        self.rect = self.wall.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

    def update(self):
        self.screen.blit(self.wall, self.rect)


class Wall2(Sprite):
    def __init__(self, screen, centerx, centery):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.wall = pygame.image.load('images/wall2.png').convert_alpha()
        self.rect = self.wall.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

    def update(self):
        self.screen.blit(self.wall, self.rect)


class Wall3(Sprite):
    def __init__(self, screen, centerx, centery):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.wall = pygame.image.load('images/wall3.png').convert_alpha()
        self.rect = self.wall.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

    def update(self):
        self.screen.blit(self.wall, self.rect)


class Wall4(Sprite):
    def __init__(self, screen, centerx, centery):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.wall = pygame.image.load('images/wall4.png').convert_alpha()
        self.rect = self.wall.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

    def update(self):
        self.screen.blit(self.wall, self.rect)


class Wall5(Sprite):
    def __init__(self, screen, centerx, centery):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.wall = pygame.image.load('images/wall5.png').convert_alpha()
        self.rect = self.wall.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

    def update(self):
        self.screen.blit(self.wall, self.rect)


class Wall6(Sprite):
    def __init__(self, screen, centerx, centery):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.wall = pygame.image.load('images/wall6.png').convert_alpha()
        self.rect = self.wall.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

    def update(self):
        self.screen.blit(self.wall, self.rect)


class Wall7(Sprite):
    def __init__(self, screen, centerx, centery):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.wall = pygame.image.load('images/wall7.png').convert_alpha()
        self.rect = self.wall.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

    def update(self):
        self.screen.blit(self.wall, self.rect)


class Wall8(Sprite):
    def __init__(self, screen, centerx, centery):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.wall = pygame.image.load('images/wall8.png').convert_alpha()
        self.rect = self.wall.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

    def update(self):
        self.screen.blit(self.wall, self.rect)


def map1(screen, walls):

    for row in [150, 400, 650]:
        for col in [275, 525, 775, 1025]:
            new_wall = Wall1(screen, col, row)
            walls.add(new_wall)


def map2(screen, walls):
    new_wall = Wall2(screen, 280, 120)
    walls.add(new_wall)
    new_wall = Wall2(screen, 1020, 680)
    walls.add(new_wall)
    new_wall = Wall2(screen, 575, 450)
    walls.add(new_wall)
    new_wall = Wall3(screen, 429, 679)
    walls.add(new_wall)
    new_wall = Wall3(screen, 870, 120)
    walls.add(new_wall)
    new_wall = Wall4(screen, 137, 180)
    walls.add(new_wall)
    new_wall = Wall4(screen, 1162, 178)
    walls.add(new_wall)
    new_wall = Wall5(screen, 1162, 520)
    walls.add(new_wall)
    new_wall = Wall5(screen, 137, 520)
    walls.add(new_wall)
    new_wall = Wall5(screen, 877, 515)
    walls.add(new_wall)
    walls.add(new_wall)
    new_wall = Wall6(screen, 282, 400)
    walls.add(new_wall)
    new_wall = Wall6(screen, 1008, 400)
    walls.add(new_wall)
    new_wall = Wall7(screen, 590, 242)
    walls.add(new_wall)
    walls.add(new_wall)
    new_wall = Wall8(screen, 722, 558)
    walls.add(new_wall)


# 设置敌方坦克出生地
def create_enemies(screen, enemies, bullets_1, walls, enemies_speed,
                   enemies_bullet_speed, enemies_firing_rate, tank_0, e_num, map_):
    bpx = 60
    bpy = 60
    if map_ == 1:
        if e_num % 3 == 0:
            bpx = 400
        if e_num % 3 == 1:
            bpx = 650
        if e_num % 3 == 2:
            bpx = 900
    if map_ == 2:
        if e_num % 5 == 0:
            bpx = 400
            bpy = 50
        if e_num % 5 == 1:
            bpx = 900
            bpy = 180
        if e_num % 5 == 2:
            bpx = 1240
            bpy = 150
        if e_num % 5 == 3:
            bpx = 450
            bpy = 330
        if e_num % 5 == 4:
            bpx = 925
            bpy = 620
    dirs = [1, 2, 3, 4]
    dir = random.choice(dirs)
    new_enemy = Enemy(screen, bullets_1, dir, tank_0, walls, enemies_speed,
                      enemies_bullet_speed, enemies_firing_rate, tank_0, bpx, bpy)

    enemies.add(new_enemy)
