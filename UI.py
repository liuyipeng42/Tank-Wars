import pygame
import sys
import time


def list_to_number(number):
    d = 1
    e = 0
    xiaoshu = 0
    zhengshu = 0
    for i in number:
        if i == '.':
            e = 1
            continue
        if e == 1:
            xiaoshu = xiaoshu + int(i) * (0.1 ** d)
            d += 1
        else:
            zhengshu = int(i) + zhengshu * 10

    shuzi = round((xiaoshu + zhengshu), 2)

    return shuzi


def str_to_list(num, numbers):
    with open('data.txt') as a:
        data = a.readlines()
    strnumber = data[num]
    for i in strnumber:
        if i != '.' and i != '\n':
            numbers[num].append(int(i))
        else:
            numbers[num].append(i)
    del numbers[num][-1]


def input_(screen, number1, pos1):
    zero = pygame.image.load('images/.0.png').convert_alpha()
    one = pygame.image.load('images/.1.png').convert_alpha()
    two = pygame.image.load('images/.2.png').convert_alpha()
    three = pygame.image.load('images/.3.png').convert_alpha()
    four = pygame.image.load('images/.4.png').convert_alpha()
    five = pygame.image.load('images/.5.png').convert_alpha()
    six = pygame.image.load('images/.6.png').convert_alpha()
    seven = pygame.image.load('images/.7.png').convert_alpha()
    eight = pygame.image.load('images/.8.png').convert_alpha()
    nine = pygame.image.load('images/.9.png').convert_alpha()
    dot = pygame.image.load('images/dot.png').convert_alpha()
    for i in number1:
        if i == '.':
            screen.blit(dot, (pos1[0], pos1[1]))
            pos1[0] += 14
        if i == 0:
            screen.blit(zero, (pos1[0], pos1[1]))
            pos1[0] += 24
        if i == 1:
            screen.blit(one, (pos1[0], pos1[1]))
            pos1[0] += 19
        if i == 2:
            screen.blit(two, (pos1[0], pos1[1]))
            pos1[0] += 24
        if i == 3:
            screen.blit(three, (pos1[0], pos1[1]))
            pos1[0] += 24
        if i == 4:
            screen.blit(four, (pos1[0], pos1[1]))
            pos1[0] += 24
        if i == 5:
            screen.blit(five, (pos1[0], pos1[1]))
            pos1[0] += 24
        if i == 6:
            screen.blit(six, (pos1[0], pos1[1]))
            pos1[0] += 24
        if i == 7:
            screen.blit(seven, (pos1[0], pos1[1]))
            pos1[0] += 24
        if i == 8:
            screen.blit(eight, (pos1[0], pos1[1]))
            pos1[0] += 24
        if i == 9:
            screen.blit(nine, (pos1[0], pos1[1]))
            pos1[0] += 24


def settings_(screen, back2, numbers):
    back = pygame.image.load('images/back.png').convert_alpha()
    back1 = pygame.image.load('images/back1.png').convert_alpha()
    shadow = pygame.image.load('images/shadow.png').convert_alpha()
    guangbiao = pygame.image.load('images/光标.png').convert_alpha()
    n = pygame.image.load('images/-.png').convert_alpha()
    map1 = pygame.image.load('images/map1.png').convert_alpha()
    map12 = pygame.image.load('images/map1(2).png').convert_alpha()
    map2 = pygame.image.load('images/map2.png').convert_alpha()
    map22 = pygame.image.load('images/map2(2).png').convert_alpha()

    back_rect = back.get_rect()
    back1_rect = back1.get_rect()
    n_rect = n.get_rect()
    shadow1_rect = shadow.get_rect()

    back_rect.centerx = 300
    back_rect.centery = 150
    back1_rect.centerx = back_rect.centerx
    back1_rect.centery = back_rect.centery
    n_rect.centerx = 500
    n_rect.centery = 380
    shadow1_rect.x = 633
    shadow1_rect.y = 176
    shuru = 0

    enemy_number = 0
    t1 = 0
    map_ = 2
    smap = 0
    start_s = True
    while start_s:
        time.sleep(0.005)
        pos_ = []
        for i in range(7):
            pos_.append([])
            for j in range(2):
                if j == 0:
                    pos_[i].append(633)
                if j == 1:
                    if i == 0:
                        pos_[i].append(176)
                    if i == 1:
                        pos_[i].append(233)
                    if i == 2:
                        pos_[i].append(286)
                    if i == 3:
                        pos_[i].append(338)
                    if i == 4:
                        pos_[i].append(393)
                    if i == 5:
                        pos_[i].append(447)
                    if i == 6:
                        pos_[i].append(500)
        pos = pos_
        shadow1 = 0
        screen.fill((255, 255, 255))
        screen.blit(back, back_rect)
        screen.blit(n, n_rect)

        if smap == 0 or smap == 2:
            screen.blit(map1, (380, 610))
        else:
            screen.blit(map12, (380, 610))
        if smap == 0 or smap == 1:
            screen.blit(map2, (580, 610))
        else:
            screen.blit(map22, (580, 610))

        x, y = pygame.mouse.get_pos()
        if abs(x - back_rect.centerx) < 25 and abs(y - back_rect.centery) < 15:
            back2 = 1
            screen.blit(back1, back1_rect)

        if abs(x - 461) < 81 and abs(y - 660) < 50:
            screen.blit(map12, (380, 610))

        if abs(x - 661) < 81 and abs(y - 660) < 50:
            screen.blit(map22, (580, 610))

        if abs(x-684) < 57:
            if abs(y - 190) < 14:
                shadow1 = 1
                screen.blit(shadow, (633, 176))
            if abs(y - 247) < 14:
                shadow1 = 2
                screen.blit(shadow, (633, 233))
            if abs(y - 300) < 14:
                shadow1 = 3
                screen.blit(shadow, (633, 286))
            if abs(y - 352) < 14:
                shadow1 = 4
                screen.blit(shadow, (633, 338))
            if abs(y - 407) < 14:
                shadow1 = 5
                screen.blit(shadow, (633, 393))
            if abs(y - 461) < 14:
                shadow1 = 6
                screen.blit(shadow, (633, 447))
            if abs(y - 514) < 14:
                shadow1 = 7
                screen.blit(shadow, (633, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                a = pygame.mouse.get_pressed()
                if a[0] == 1:
                    if back2 == 1:
                        start_s = False
                    for i in range(1, 8):
                        if shadow1 == i:
                            shuru = i
                            t1 = 0
                            break
                        else:
                            shuru = 0

                    if abs(x - 461) < 81 and abs(y - 691) < 50:
                        map_ = 1
                        smap = 1

                    if abs(x - 661) < 81 and abs(y - 691) < 50:
                        map_ = 2
                        smap = 2

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE and len(numbers[shuru - 1]) > 0:
                    del numbers[shuru - 1][-1]

                if shuru in [1, 2, 3, 4, 5, 6, 7] and len(numbers[shuru - 1]) < 4:
                    if event.key == pygame.K_KP_PERIOD and (shuru - 1) != 0:
                        numbers[shuru - 1].append('.')
                    if event.key == pygame.K_KP0:
                        numbers[shuru - 1].append(0)
                    if event.key == pygame.K_KP1:
                        numbers[shuru - 1].append(1)
                    if event.key == pygame.K_KP2:
                        numbers[shuru - 1].append(2)
                    if event.key == pygame.K_KP3:
                        numbers[shuru - 1].append(3)
                    if event.key == pygame.K_KP4:
                        numbers[shuru - 1].append(4)
                    if event.key == pygame.K_KP5:
                        numbers[shuru - 1].append(5)
                    if event.key == pygame.K_KP6:
                        numbers[shuru - 1].append(6)
                    if event.key == pygame.K_KP7:
                        numbers[shuru - 1].append(7)
                    if event.key == pygame.K_KP8:
                        numbers[shuru - 1].append(8)
                    if event.key == pygame.K_KP9:
                        numbers[shuru - 1].append(9)

        if shuru == 1:
            screen.blit(shadow, (633, 176))
        if shuru == 2:
            screen.blit(shadow, (633, 233))
        if shuru == 3:
            screen.blit(shadow, (633, 286))
        if shuru == 4:
            screen.blit(shadow, (633, 338))
        if shuru == 5:
            screen.blit(shadow, (633, 393))
        if shuru == 6:
            screen.blit(shadow, (633, 447))
        if shuru == 7:
            screen.blit(shadow, (633, 500))

        num = 0
        for number in numbers:
            input_(screen, number, pos[num])
            num += 1

        if shuru in [1, 2, 3, 4, 5, 6, 7]:
            if t1 == 0:
                t1 = time.time() - 0.6
            t2 = time.time()
            if t2 - t1 >= 0.6:
                screen.blit(guangbiao, (pos[shuru - 1][0], pos[shuru - 1][1]))
                if t2 - t1 >= 1.2:
                    t1 = time.time()

        pygame.display.flip()

    for i in numbers[0]:
        enemy_number = int(i) + enemy_number * 10

    with open('data.txt') as a:
        b = a.readlines()
    c = []
    for i in range(len(b)):
        c.append(eval(b[i]))
    c[0] = enemy_number
    c[1] = list_to_number(numbers[1])
    c[2] = list_to_number(numbers[2])
    c[3] = list_to_number(numbers[3])
    c[4] = list_to_number(numbers[4])
    c[5] = list_to_number(numbers[5])
    c[6] = list_to_number(numbers[6])
    c[7] = map_
    a = open('data.txt', 'w')
    for i in c:
        a.write(str(i))
        a.write('\n')
    a.close()

    return c[0], c[1], c[2], c[3], c[4], c[5], c[6], map_


def interface(screen):

    pygame.mixer.init()
    pygame.mixer.music.load('music/Star-Wars.mp3')
    pygame.mixer.music.play(-1, 0)
    pygame.mixer.music.set_volume(0.05)

    tank_wars = pygame.image.load('images/tank wars.png').convert_alpha()
    play = pygame.image.load('images/play.png').convert_alpha()
    play1 = pygame.image.load('images/play1.png').convert_alpha()
    settings = pygame.image.load('images/settings.png').convert_alpha()
    settings1 = pygame.image.load('images/settings1.png').convert_alpha()

    tank_wars_rect = tank_wars.get_rect()
    play_rect = play.get_rect()
    play1_rect = play1.get_rect()
    settings_rect = settings.get_rect()
    settings1_rect = settings1.get_rect()

    tank_wars_rect.centerx = 650
    tank_wars_rect.centery = 220
    play_rect.centerx = 650
    play_rect.centery = 360
    play1_rect.centerx = play_rect.centerx
    play1_rect.centery = play_rect.centery
    settings_rect.centerx = 650
    settings_rect.centery = 410
    settings1_rect.centerx = settings_rect.centerx
    settings1_rect.centery = settings_rect.centery

    start = True
    numbers = []
    for i in range(7):
        numbers.append([])
        for j in range(0):
            numbers[i].append(i)

    with open('data.txt') as a:
        data = a.readlines()

    enemy_number = int(data[0])
    enemies_speed = float(data[1])
    enemies_bullet_speed = float(data[2])
    enemies_firing_rate = float(data[3])
    speed = float(data[4])
    bullet_speed = float(data[5])
    firing_rate = float(data[6])
    map_ = int(data[7])

    str_to_list(0, numbers)
    str_to_list(1, numbers)
    str_to_list(2, numbers)
    str_to_list(3, numbers)
    str_to_list(4, numbers)
    str_to_list(5, numbers)
    str_to_list(6, numbers)

    while start:
        time.sleep(0.005)
        play2 = 0
        settings2 = 0
        back2 = 0
        screen.fill((255, 255, 255))

        screen.blit(tank_wars, tank_wars_rect)
        screen.blit(play, play_rect)
        screen.blit(settings, settings_rect)

        x, y = pygame.mouse.get_pos()

        if abs(x-650) < 70 and abs(y-360) < 16.5:
            play2 = 1
            screen.blit(play1, play1_rect)

        if abs(x-650) < 107 and abs(y-410) < 16.5:
            settings2 = 1
            screen.blit(settings1, settings1_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                a = pygame.mouse.get_pressed()
                if a[0] == 1:
                    if play2 == 1:
                        start = False
                    if settings2 == 1:
                        enemy_number, enemies_speed, enemies_bullet_speed, enemies_firing_rate, speed, \
                                      bullet_speed, firing_rate, map_ = settings_(screen, back2, numbers)

        pygame.display.flip()

    return enemy_number, enemies_speed, enemies_bullet_speed, \
        enemies_firing_rate, speed, bullet_speed, firing_rate, map_
