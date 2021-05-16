import pygame
import sys
import time

from picture import Picture


def list_to_number(list_number):
    str_number = ''
    for i in list_number:
        str_number += i
    if '.' in str_number:
        return round(float(str_number), 2)
    else:
        return round(int(str_number), 2)


def load_data():
    with open('data.txt', 'r') as f:
        data = []
        for line in f.readlines():
            data.append([c for c in line if c != '\n'])

    return data


def show_number(screen, numbers, number, pos):
    for i in number:
        if i == '.':
            screen.blit(numbers['dot'], (pos[0], pos[1]))
            pos[0] += 14
        if i == '0':
            screen.blit(numbers['zero'], (pos[0], pos[1]))
            pos[0] += 24
        if i == '1':
            screen.blit(numbers['one'], (pos[0], pos[1]))
            pos[0] += 19
        if i == '2':
            screen.blit(numbers['two'], (pos[0], pos[1]))
            pos[0] += 24
        if i == '3':
            screen.blit(numbers['three'], (pos[0], pos[1]))
            pos[0] += 24
        if i == '4':
            screen.blit(numbers['four'], (pos[0], pos[1]))
            pos[0] += 24
        if i == '5':
            screen.blit(numbers['five'], (pos[0], pos[1]))
            pos[0] += 24
        if i == '6':
            screen.blit(numbers['six'], (pos[0], pos[1]))
            pos[0] += 24
        if i == '7':
            screen.blit(numbers['seven'], (pos[0], pos[1]))
            pos[0] += 24
        if i == '8':
            screen.blit(numbers['eight'], (pos[0], pos[1]))
            pos[0] += 24
        if i == '9':
            screen.blit(numbers['nine'], (pos[0], pos[1]))
            pos[0] += 24


def show_and_select_map(screen, maps, x, y, map_flag):
    if map_flag == 0 or map_flag == 2:
        screen.blit(maps['first_map'].picture, maps['first_map'].rect)
    else:
        screen.blit(maps['first_map1'].picture, maps['first_map1'].rect)
    if map_flag == 0 or map_flag == 1:
        screen.blit(maps['second_map'].picture, maps['second_map'].rect)
    else:
        screen.blit(maps['second_map1'].picture, maps['second_map1'].rect)

    if abs(x - 461) < 81 and abs(y - 660) < 50:
        screen.blit(maps['first_map1'].picture, maps['first_map1'].rect)

    if abs(x - 661) < 81 and abs(y - 660) < 50:
        screen.blit(maps['second_map1'].picture, maps['second_map1'].rect)
    return map_flag


def select_text_area(screen, shadow, x, y, text_area_pos, text_input_flag):

    text_area_flag = 0
    if abs(x - 684) < 57:
        if abs(y - 190) < 14:
            text_area_flag = 1
        if abs(y - 247) < 14:
            text_area_flag = 2
        if abs(y - 300) < 14:
            text_area_flag = 3
        if abs(y - 352) < 14:
            text_area_flag = 4
        if abs(y - 407) < 14:
            text_area_flag = 5
        if abs(y - 461) < 14:
            text_area_flag = 6
        if abs(y - 514) < 14:
            text_area_flag = 7

    if text_area_flag:
        screen.blit(shadow, text_area_pos[text_area_flag - 1])
    if text_input_flag:
        screen.blit(shadow, text_area_pos[text_input_flag - 1])

    return text_area_flag


def settings_(screen, back2, data):
    back = Picture('images/back.png', 300, 150)
    back1 = Picture('images/back1.png', 300, 150)
    cursor = pygame.image.load('images/光标.png').convert_alpha()
    attributes_title = Picture('images/-.png', 500, 380)

    numbers = {
        'zero': pygame.image.load('images/.0.png').convert_alpha(),
        'one': pygame.image.load('images/.1.png').convert_alpha(),
        'two': pygame.image.load('images/.2.png').convert_alpha(),
        'three': pygame.image.load('images/.3.png').convert_alpha(),
        'four': pygame.image.load('images/.4.png').convert_alpha(),
        'five': pygame.image.load('images/.5.png').convert_alpha(),
        'six': pygame.image.load('images/.6.png').convert_alpha(),
        'seven': pygame.image.load('images/.7.png').convert_alpha(),
        'eight': pygame.image.load('images/.8.png').convert_alpha(),
        'nine': pygame.image.load('images/.9.png').convert_alpha(),
        'dot': pygame.image.load('images/dot.png').convert_alpha()
    }

    maps = {
        'first_map': Picture('images/map1.png', 461, 660),
        'first_map1': Picture('images/map1(2).png', 461, 660),
        'second_map': Picture('images/map2.png', 661, 660),
        'second_map1': Picture('images/map2(2).png', 661, 660)
    }

    shadow = pygame.image.load('images/shadow.png').convert_alpha()

    text_input_flag = 0

    t1 = 0
    map_flag = 2
    start_s = True
    while start_s:
        time.sleep(0.005)

        text_area_pos = [[633, 176], [633, 233], [633, 286], [633, 338], [633, 393], [633, 447], [633, 500]]

        screen.fill((255, 255, 255))
        screen.blit(back.picture, back.rect)
        screen.blit(attributes_title.picture, attributes_title.rect)

        x, y = pygame.mouse.get_pos()
        if abs(x - back.x) < 25 and abs(y - back.y) < 15:
            back2 = 1
            screen.blit(back1.picture, back1.rect)

        map_flag = show_and_select_map(screen, maps, x, y, map_flag)
        text_area_flag = select_text_area(screen, shadow, x, y, text_area_pos, text_input_flag)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                a = pygame.mouse.get_pressed()
                if a[0] == 1:
                    if back2 == 1:
                        start_s = False
                    for i in range(1, 8):
                        if text_area_flag == i:
                            text_input_flag = i
                            t1 = 0
                            break
                        else:
                            text_input_flag = 0

                    if abs(x - 461) < 81 and abs(y - 691) < 50:
                        map_flag = 1
                        data[-1] = ['1']

                    if abs(x - 661) < 81 and abs(y - 691) < 50:
                        map_flag = 2
                        data[-1] = ['2']

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE and len(data[text_input_flag - 1]) > 0:
                    del data[text_input_flag - 1][-1]

                if text_input_flag in [1, 2, 3, 4, 5, 6, 7] and len(data[text_input_flag - 1]) < 4:
                    if event.key == pygame.K_KP_PERIOD and (text_input_flag - 1) != 0:
                        data[text_input_flag - 1].append('.')
                    if event.key == pygame.K_KP0 or event.key == pygame.K_0:
                        data[text_input_flag - 1].append('0')
                    if event.key == pygame.K_KP1 or event.key == pygame.K_1:
                        data[text_input_flag - 1].append('1')
                    if event.key == pygame.K_KP2 or event.key == pygame.K_2:
                        data[text_input_flag - 1].append('2')
                    if event.key == pygame.K_KP3 or event.key == pygame.K_3:
                        data[text_input_flag - 1].append('3')
                    if event.key == pygame.K_KP4 or event.key == pygame.K_4:
                        data[text_input_flag - 1].append('4')
                    if event.key == pygame.K_KP5 or event.key == pygame.K_5:
                        data[text_input_flag - 1].append('5')
                    if event.key == pygame.K_KP6 or event.key == pygame.K_6:
                        data[text_input_flag - 1].append('6')
                    if event.key == pygame.K_KP7 or event.key == pygame.K_7:
                        data[text_input_flag - 1].append('7')
                    if event.key == pygame.K_KP8 or event.key == pygame.K_8:
                        data[text_input_flag - 1].append('8')
                    if event.key == pygame.K_KP9 or event.key == pygame.K_9:
                        data[text_input_flag - 1].append('9')

        num = 0
        for number in data[:-1]:
            show_number(screen, numbers, number, text_area_pos[num])
            num += 1

        if text_input_flag in [1, 2, 3, 4, 5, 6, 7]:
            if t1 == 0:
                t1 = time.time() - 0.6
            t2 = time.time()
            if t2 - t1 >= 0.6:
                screen.blit(cursor, (text_area_pos[text_input_flag - 1][0], text_area_pos[text_input_flag - 1][1]))
                if t2 - t1 >= 1.2:
                    t1 = time.time()

        pygame.display.flip()

    return_data = []

    with open('data.txt', 'w') as f:
        for num_list in data:
            num = list_to_number(num_list)
            f.write(str(num) + '\n')
            return_data.append(num)

    return return_data


def interface(screen):
    # pygame.mixer.init()
    # pygame.mixer.music.load('music/Star-Wars.mp3')
    # pygame.mixer.music.play(-1, 0)
    # pygame.mixer.music.set_volume(0.05)

    tank_wars_title = Picture('images/tank wars.png', 650, 220)
    play_word = Picture('images/play.png', 650, 360)
    play1_word = Picture('images/play1.png', 650, 360)
    settings_word = Picture('images/settings.png', 650, 410)
    settings1_word = Picture('images/settings1.png', 650, 410)

    return_data = []
    start = True
    while start:
        time.sleep(0.005)
        play = 0
        settings = 0
        back2 = 0
        screen.fill((255, 255, 255))

        screen.blit(tank_wars_title.picture, tank_wars_title.rect)
        screen.blit(play_word.picture, play_word.rect)
        screen.blit(settings_word.picture, settings_word.rect)

        x, y = pygame.mouse.get_pos()

        if abs(x - 650) < 70 and abs(y - 360) < 16.5:
            play = 1
            screen.blit(play1_word.picture, play1_word.rect)

        if abs(x - 650) < 107 and abs(y - 410) < 16.5:
            settings = 1
            screen.blit(settings1_word.picture, settings1_word.rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                a = pygame.mouse.get_pressed()
                if a[0] == 1:
                    if play == 1:
                        return_data = []
                        with open('data.txt', 'r') as f:
                            for line in f.readlines():
                                return_data.append(eval(line.split('\n')[0]))
                        start = False
                    if settings == 1:
                        data = load_data()
                        return_data = settings_(screen, back2, data)

        pygame.display.flip()

    return return_data
