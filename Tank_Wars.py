import os
import sys
import time
import UI
import map_and_enemies
from collision import *
from tank_0 import Tank0
from pygame.sprite import Group

pygame.init()
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % (250, 100)
screen = pygame.display.set_mode((1300, 800), pygame.HWSURFACE)
screen.fill((255, 255, 255))
pygame.display.set_caption('Tank Wars')

t1 = 42
e_num = 0

de = 0
game_over = 0
stop = 0
a = 0


Tank = 0
walls = 0
enemies = 0
bullets = 0
bullets_1 = 0
simulate_fire = 0
enemy_number = 0
enemies_speed = 0
enemies_bullet_speed = 0
enemies_firing_rate = 0
speed = 0
bullet_speed = 0
firing_rate = 0
map_ = 0
tank_0 = 0

blank = pygame.image.load('images/blank.png').convert_alpha()
blank1 = pygame.image.load('images/blank1.png').convert_alpha()
continue_game = pygame.image.load('images/继续.png').convert_alpha()
continue_game1 = pygame.image.load('images/继续1.png').convert_alpha()
zjm = pygame.image.load('images/主界面.png').convert_alpha()
zjm1 = pygame.image.load('images/主界面1.png').convert_alpha()
defeat = pygame.image.load('images/defeat.png').convert_alpha()
victory = pygame.image.load('images/victory.png').convert_alpha()
b_r1 = blank1.get_rect()
v_r = victory.get_rect()
b_r = blank.get_rect()
continue_game_r = continue_game.get_rect()
zjm_r = zjm.get_rect()
d_r = defeat.get_rect()
b_r.centerx = 650
b_r.centery = 390
v_r.centerx = 650
v_r.centery = 340
b_r1.centerx = 650
b_r1.centery = 370
continue_game_r.centerx = 650
continue_game_r.centery = 360
zjm_r.centerx = 650
zjm_r.centery = 420
d_r.centerx = 650
d_r.centery = 340
zjm_r1 = zjm_r


while True:
    screen.fill((255, 255, 255))
    time.sleep(0.018)
    if a == 0:

        Tank = Group()
        walls = Group()
        enemies = Group()
        bullets = Group()
        bullets_1 = Group()

        enemy_number, enemies_speed, enemies_bullet_speed, enemies_firing_rate, speed, \
            bullet_speed, firing_rate, map_ = UI.interface(screen)

        tank_0 = Tank0(screen, speed, bullet_speed, firing_rate, bullets, walls)
        Tank.add(tank_0)

        if map_ == 1:
            map_and_enemies.map1(screen, walls)
        if map_ == 2:
            map_and_enemies.map2(screen, walls)

        game_over = 0
        e_num = 0
        t1 = 0
        de = 0
        a += 1

    t2 = time.time()
    if t2 - t1 > 1.5 and e_num < enemy_number and len(enemies) < 5 and tank_0.stop2 != 1:
        map_and_enemies.create_enemies(screen, enemies, bullets_1, walls, enemies_speed,
                                       enemies_bullet_speed, enemies_firing_rate, tank_0, e_num, map_)
        t1 = time.time()
        e_num += 1

    enemies_and_enemies(enemies)
    enemies_and_walls(enemies, walls)
    bullets_and_walls(bullets, walls)
    bullets_and_walls(bullets_1, walls)
    tank_0_and_walls(tank_0, walls)
    tank_0_and_enemies(tank_0, enemies)
    for enemy in enemies:
        bullets_and_walls(enemy.simulate_fire, walls)
        enemy.simulate_fire.update()
    bullets.update()
    bullets_1.update()
    walls.update()
    enemies.update()
    game_over, de = collisions(bullets, bullets_1, enemies, Tank, game_over, de)

    if tank_0.stop2 == 1:
        for enemy in enemies:
            enemy.stop = 1
            enemy.mode = 1
        for bullet in bullets:
            bullet.stop = 1
        for bullet in bullets_1:
            bullet.stop = 1
    else:
        for enemy in enemies:
            enemy.stop = 0
        for bullet in bullets:
            bullet.stop = 0
        for bullet in bullets_1:
            bullet.stop = 0

    if tank_0.stop2 == 1:
        x, y = pygame.mouse.get_pos()
        screen.blit(blank, b_r)
        screen.blit(continue_game, continue_game_r)
        screen.blit(zjm, zjm_r)
        if abs(x - 650) < 35 and abs(y - 360) < 17:
            screen.blit(continue_game1, continue_game_r)
        if abs(x - 650) < 50 and abs(y - 420) < 17:
            screen.blit(zjm1, zjm_r1)

    if tank_0.back == 1:
        a = 0

    if de == enemy_number:
        tank_0.game_over = 1
        x, y = pygame.mouse.get_pos()
        screen.blit(blank1, b_r1)
        screen.blit(victory, v_r)
        screen.blit(zjm, zjm_r)
        if abs(x - 650) < 50 and abs(y - 420) < 17:
            screen.blit(zjm1, zjm_r1)

    if game_over == 1:
        x, y = pygame.mouse.get_pos()
        screen.blit(blank1, b_r1)
        screen.blit(defeat, d_r)
        screen.blit(zjm, zjm_r)
        if abs(x - 650) < 50 and abs(y - 430) < 17:
            screen.blit(zjm1, zjm_r1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                a = pygame.mouse.get_pressed()
                if a[0] == 1:
                    if abs(x - 650) < 45 and abs(y - 430) < 17:
                        a = 0
                        game_over = 0

    pygame.display.flip()
