import pygame
import random
from enemy import Enemy
from pygame.sprite import Sprite


class Wall(Sprite):
    def __init__(self, screen, pos, picture):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.wall = pygame.image.load(picture).convert_alpha()
        self.rect = self.wall.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

    def update(self):
        self.screen.blit(self.wall, self.rect)


def map1(screen, walls):
    for row in [150, 400, 650]:
        for col in [275, 525, 775, 1025]:
            new_wall = Wall(screen, (col, row), 'images/wall1.png')
            walls.add(new_wall)


def map2(screen, walls):
    pos = [
        (280, 120), (1020, 680), (575, 450), (429, 679),
        (870, 120), (137, 180), (1162, 178), (1162, 520),
        (137, 520), (877, 515), (282, 400), (1008, 400),
        (590, 242), (722, 558)
    ]

    picture = [
        'images/wall2.png', 'images/wall2.png', 'images/wall2.png', 'images/wall3.png',
        'images/wall3.png', 'images/wall4.png', 'images/wall4.png', 'images/wall5.png',
        'images/wall5.png', 'images/wall5.png', 'images/wall6.png', 'images/wall6.png',
        'images/wall7.png', 'images/wall8.png'
    ]

    for i in range(len(picture)):
        walls.add(Wall(screen, pos[i], picture[i]))
        

# 设置敌方坦克出生地
def create_enemies(screen, enemies, bullets_1, walls, enemies_speed,
                   enemies_bullet_speed, enemies_firing_rate, tank_0, enemy_num, map_):
    bpx = 60
    bpy = 60
    if map_ == 1:
        if enemy_num % 3 == 0:
            bpx = 400
        if enemy_num % 3 == 1:
            bpx = 650
        if enemy_num % 3 == 2:
            bpx = 900
            
    if map_ == 2:
        if enemy_num % 5 == 0:
            bpx = 400
            bpy = 50
        if enemy_num % 5 == 1:
            bpx = 900
            bpy = 180
        if enemy_num % 5 == 2:
            bpx = 1240
            bpy = 150
        if enemy_num % 5 == 3:
            bpx = 450
            bpy = 330
        if enemy_num % 5 == 4:
            bpx = 925
            bpy = 620
            
    direction = random.choice([1, 2, 3, 4])
    new_enemy = Enemy(screen, bullets_1, direction, tank_0, walls, enemies_speed,
                      enemies_bullet_speed, enemies_firing_rate, tank_0, bpx, bpy)

    enemies.add(new_enemy)
