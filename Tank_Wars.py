import os
import sys
import time
import UI
import map_and_enemies
from collision import *
from picture import Picture
from tank_0 import Tank0
from pygame.sprite import Group


def main():
    pygame.init()
    os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % (250, 100)
    screen = pygame.display.set_mode((1300, 800), pygame.HWSURFACE)
    screen.fill((255, 255, 255))
    pygame.display.set_caption('Tank Wars')

    t1 = 42
    enemy_num = 0
    destroyed_enemies = 0
    game_over = 0
    start = 0
    myTank = None
    walls = None
    enemies = None
    bullets = None
    bullets_1 = None
    total_enemy_number = 0
    enemies_speed = 0
    enemies_bullet_speed = 0
    enemies_firing_rate = 0
    map_ = 0
    tank_0 = 0

    blank_background = Picture('images/blank.png', 650, 390)
    blank_background1 = Picture('images/blank1.png', 650, 370)
    continue_game_word = Picture('images/继续.png', 650, 360)
    continue_game_word1 = Picture('images/继续1.png', 650, 360)
    main_interface_word = Picture('images/主界面.png', 650, 420)
    main_interface_word1 = Picture('images/主界面1.png', 650, 420)
    defeat_word = Picture('images/defeat.png', 650, 340)
    victory_word = Picture('images/victory.png', 650, 340)

    while True:
        screen.fill((255, 255, 255))
        time.sleep(0.018)

        # 初始化
        if start == 0:
            myTank = Group()
            walls = Group()
            enemies = Group()
            bullets = Group()
            bullets_1 = Group()

            total_enemy_number, enemies_speed, enemies_bullet_speed, \
                enemies_firing_rate, speed, bullet_speed, \
                firing_rate, map_ = UI.interface(screen)

            tank_0 = Tank0(screen, speed, bullet_speed, firing_rate, bullets, walls)
            myTank.add(tank_0)

            if map_ == 1:
                map_and_enemies.map1(screen, walls)
            if map_ == 2:
                map_and_enemies.map2(screen, walls)

            game_over = 0
            enemy_num = 0
            t1 = 0
            destroyed_enemies = 0
            start += 1

        # 每隔 1.5秒生成一个敌方坦克
        t2 = time.time()
        if t2 - t1 > 1.5 and enemy_num < total_enemy_number and len(enemies) < 5 and tank_0.stop2 != 1:
            map_and_enemies.create_enemies(screen, enemies, bullets_1, walls, enemies_speed, enemies_bullet_speed,
                                           enemies_firing_rate, tank_0, enemy_num, map_)
            t1 = time.time()
            enemy_num += 1

        # 碰撞测试
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
        game_over, destroyed_enemies = otherCollisions(bullets, bullets_1, enemies, myTank, game_over,
                                                       destroyed_enemies)

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
            screen.blit(blank_background.picture, blank_background.rect)
            screen.blit(continue_game_word.picture, continue_game_word.rect)
            screen.blit(main_interface_word.picture, main_interface_word.rect)
            if abs(x - 650) < 35 and abs(y - 360) < 17:
                screen.blit(continue_game_word1.picture, continue_game_word1.rect)
            if abs(x - 650) < 50 and abs(y - 420) < 17:
                screen.blit(main_interface_word1.picture, main_interface_word1.rect)

        if tank_0.back == 1:
            start = 0

        if destroyed_enemies == total_enemy_number:
            tank_0.game_over = 1
            x, y = pygame.mouse.get_pos()
            screen.blit(blank_background1.picture, blank_background1.rect)
            screen.blit(victory_word.picture, victory_word.rect)
            screen.blit(main_interface_word.picture, main_interface_word.rect)
            if abs(x - 650) < 50 and abs(y - 420) < 17:
                screen.blit(main_interface_word1.picture, main_interface_word1.rect)

        # 显示结束游戏的窗口
        if game_over == 1:
            x, y = pygame.mouse.get_pos()
            screen.blit(blank_background1.picture, blank_background1.rect)
            screen.blit(defeat_word.picture, defeat_word.rect)
            screen.blit(main_interface_word.picture, main_interface_word.rect)
            if abs(x - 650) < 50 and abs(y - 430) < 17:
                screen.blit(main_interface_word1.picture, main_interface_word1.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == 1:
                        if abs(x - 650) < 45 and abs(y - 430) < 17:
                            start = 0
                            game_over = 0

        pygame.display.flip()


if __name__ == '__main__':
    main()
