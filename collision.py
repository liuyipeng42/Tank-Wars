import pygame


def judge(object1, object2):
    o1_t = object1.rect.top
    o1_b = object1.rect.bottom
    o1_l = object1.rect.left
    o1_r = object1.rect.right
    o2_t = object2.rect.top
    o2_b = object2.rect.bottom
    o2_l = object2.rect.left
    o2_r = object2.rect.right
    top = o1_t - object2.rect.bottom
    bottom = o1_b - object2.rect.top
    left = o1_l - object2.rect.right
    right = o1_r - object2.rect.left
    if abs(bottom) <= 2:
        if (left * right < 0) or (o1_l <= o2_l <= o1_r or o1_l <= o2_r <= o1_r):
            return 2
    elif abs(top) <= 2:
        if (left * right < 0) or (o1_l <= o2_l <= o1_r or o1_l <= o2_r <= o1_r):
            return 1
    elif abs(right) <= 2:
        if (top * bottom < 0) or (o1_t <= o2_t <= o1_b or o1_t <= o2_b <= o1_b):
            return 4
    elif abs(left) <= 2:
        if (top * bottom < 0) or (o1_t <= o2_t <= o1_b or o1_t <= o2_b <= o1_b):
            return 3
    else:
        return 0


def tank_0_and_walls(tank_0, walls):
    for wall in walls.copy():
        c = judge(tank_0, wall)
        if c == 1:
            tank_0.collision[0] = 1
        elif c == 2:
            tank_0.collision[1] = 1
        elif c == 3:
            tank_0.collision[2] = 1
        elif c == 4:
            tank_0.collision[3] = 1


def enemies_and_walls(enemies, walls):
    for enemy in enemies:
        for wall in walls:
            c = judge(enemy, wall)
            if c == 1:
                enemy.collision[0] = 1
            elif c == 2:
                enemy.collision[1] = 1
            elif c == 3:
                enemy.collision[2] = 1
            elif c == 4:
                enemy.collision[3] = 1


def tank_0_and_enemies(tank_0, enemies):
    for enemy in enemies.copy():
        c = judge(enemy, tank_0)
        if c == 1:
            enemy.collision[0] = 1
            tank_0.collision[1] = 1
        elif c == 2:
            enemy.collision[1] = 1
            tank_0.collision[0] = 1
        elif c == 3:
            enemy.collision[2] = 1
            tank_0.collision[3] = 1
        elif c == 4:
            enemy.collision[3] = 1
            tank_0.collision[2] = 1


def enemies_and_enemies(enemies):
    for enemy in enemies:
        for enemy1 in enemies:
            if enemy != enemy1:
                c = judge(enemy, enemy1)
                if c == 1:
                    enemy.collision[0] = 1
                    enemy1.collision[1] = 1
                elif c == 2:
                    enemy.collision[1] = 1
                    enemy1.collision[0] = 1
                elif c == 3:
                    enemy.collision[2] = 1
                    enemy1.collision[3] = 1
                elif c == 4:
                    enemy.collision[3] = 1
                    enemy1.collision[2] = 1


def bullets_and_walls(bullets, walls):
    for bullet in bullets.copy():
        if bullet.reflection >= 2:
            bullets.remove(bullet)
        for wall in walls.copy():
            wt = wall.rect.top
            wb = wall.rect.bottom
            wl = wall.rect.left
            wr = wall.rect.right
            top = wt - bullet.rect.bottom
            bottom = wb - bullet.rect.top
            right = wr - bullet.rect.left
            left = wl - bullet.rect.right
            if abs(left) <= 3 or abs(right) <= 3:
                if (top * bottom < 0) or (wt <= bullet.rect.top <= wb or wt <= bullet.rect.bottom <= wb):
                    bullet.collision = 1
                    bullet.reflection += 1
                    bullet.collision1 = 1
                    if abs(left) <= bullet.boundary:
                        bullet.rect.right -= 3
                    if abs(right) <= bullet.boundary:
                        bullet.rect.left += 3
            if abs(top) <= 3 or abs(bottom) <= 3:
                if (left * right < 0) or (wl <= bullet.rect.right <= wr or wl <= bullet.rect.left <= wr):
                    bullet.collision = 1
                    bullet.reflection += 1
                    bullet.collision1 = 2
                    if abs(top) <= bullet.boundary:
                        bullet.rect.bottom -= 3
                    if abs(bottom) <= bullet.boundary:
                        bullet.rect.top += 3


def otherCollisions(bullets, bullets_1, enemies, tank, game_over, de):
    for tank_0 in tank.copy():
        if pygame.sprite.groupcollide(bullets_1, tank, True, False):
            tank_0.hit = 1
        if tank_0.die == 0:
            tank_0.update()
        else:
            game_over = 1
            tank.remove(tank_0)

    pygame.sprite.groupcollide(bullets, bullets_1, True, True)

    for enemy in enemies.copy():

        for bullet in enemy.simulate_fire.copy():
            if bullet.hit == 0:
                if pygame.sprite.spritecollideany(bullet, tank):
                    enemy.mode = 2
                    bullet.hit = 1
            else:
                if pygame.sprite.spritecollideany(bullet, tank):
                    pass
                else:
                    enemy.mode = 1
                    enemy.simulate_fire.remove(bullet)

        enemies.remove(enemy)
        pygame.sprite.groupcollide(bullets_1, enemies, True, False)
        enemies.add(enemy)

        if pygame.sprite.spritecollide(enemy, bullets, True):
            enemy.hit = 1
        if enemy.delete == 1:
            de += 1
            print(de)
            enemies.remove(enemy)

    for bullet in bullets_1.copy():
        if bullet.reflection == 1:
            pygame.sprite.groupcollide(bullets_1, enemies, True, False)

    for bullet in bullets.copy():
        if bullet.reflection == 1:
            pygame.sprite.groupcollide(bullets, tank, True, False)

    return game_over, de
