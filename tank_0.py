import sys
import math
import time
import pygame
from bullet import Bullet
from pygame.sprite import Sprite


class Tank0(Sprite):

    def __init__(self, screen, speed, bullet_speed, firing_rate, bullets, walls):
        super().__init__()
        self.screen = screen
        self.walls = walls
        self.tank = pygame.image.load('images/tank 1.png').convert_alpha()
        self.gun = pygame.image.load('images/1.png').convert_alpha()
        self.gun1 = pygame.image.load('images/2.png').convert_alpha()

        self.rect = self.tank.get_rect()
        self.gun_rect = self.gun.get_rect()
        self.gun1_rect = self.gun1.get_rect()
        self.screen_rect = screen.get_rect()

        self.speed = speed
        self.bullet_speed = bullet_speed
        self.firing_rate = firing_rate

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.x_move = self.rect.centerx
        self.y_move = self.rect.centery
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.collision = [0, 0, 0, 0]

        self.c = 42
        self.bullets = bullets
        self.up = 1

        self.b = [-20, -10, 0, 10, 20]
        self.blood = pygame.image.load('images/blood.png').convert_alpha()
        self.rect1 = self.blood.get_rect()
        self.hit = 0
        self.die = 0
        self.stop = pygame.image.load('images/stop.png').convert_alpha()
        self.stop1 = pygame.image.load('images/stop1.png').convert_alpha()
        self.stop2 = 0
        self.back = 0
        self.game_over = 0

    def update(self):

        x, y = pygame.mouse.get_pos()
        z = math.sqrt((x-self.rect.centerx)**2+(y-self.rect.centery)**2)
        if z == 0:
            z = 50

        if self.game_over == 1:
            self.stop2 = 1

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                a = pygame.mouse.get_pressed()
                if a[0] == 1:
                    if self.stop2 == 0:
                        b = time.time()

                        if abs(x - 1265) < 15 and abs(y - 35) < 15:
                            self.stop2 = 1

                        if b - self.c >= self.firing_rate:
                            new_bullet = Bullet(int(self.rect.centerx + 55*((x-self.rect.centerx)/z)),
                                                int(self.rect.centery + 55*((y-self.rect.centery)/z)),
                                                self.rect.centerx, self.rect.centery,
                                                self.bullet_speed, self.screen, self.walls, 0, 0)
                            self.c = time.time()
                            self.bullets.add(new_bullet)
                    else:
                        if abs(x - 650) < 55 and abs(y - 430) < 17:
                            self.back = 1
                        if abs(x - 650) < 35 and abs(y - 360) < 17:
                            if self.game_over == 0:
                                self.stop2 = 0

            elif event.type == pygame.KEYDOWN and self.stop2 == 0:

                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                if event.key == pygame.K_d:
                    self.moving_right = True
                    self.moving_left = False
                    self.moving_up = False
                    self.moving_down = False
                    self.tank = pygame.image.load('images/tank 2.png').convert_alpha()
                elif event.key == pygame.K_a:
                    self.moving_left = True
                    self.moving_right = False
                    self.moving_up = False
                    self.moving_down = False
                    self.tank = pygame.image.load('images/tank 2.png').convert_alpha()
                elif event.key == pygame.K_w:
                    self.moving_up = True
                    self.moving_right = False
                    self.moving_left = False
                    self.moving_down = False
                    self.tank = pygame.image.load('images/tank 1.png').convert_alpha()
                elif event.key == pygame.K_s:
                    self.moving_down = True
                    self.moving_right = False
                    self.moving_left = False
                    self.moving_up = False
                    self.tank = pygame.image.load('images/tank 1.png').convert_alpha()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.moving_right = False
                if event.key == pygame.K_a:
                    self.moving_left = False
                if event.key == pygame.K_w:
                    self.moving_up = False
                if event.key == pygame.K_s:
                    self.moving_down = False

        if self.moving_up and self.rect.top > 0:
            if self.collision[0] != 1:
                self.y_move -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            if self.collision[1] != 1:
                self.y_move += self.speed
        if self.moving_left and self.rect.left > 0:
            if self.collision[2] != 1:
                self.x_move -= self.speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            if self.collision[3] != 1:
                self.x_move += self.speed

        self.collision = [0, 0, 0, 0]

        self.rect.centerx = int(self.x_move + 0.5)
        self.rect.centery = int(self.y_move + 0.5)

        self.gun_rect.centerx = self.rect.centerx
        self.gun_rect.centery = self.rect.centery
        x3 = int(self.rect.centerx + 50*((x-self.rect.centerx)/z))
        y3 = int(self.rect.centery + 50*((y-self.rect.centery)/z))
        self.gun1_rect.centerx = x3
        self.gun1_rect.centery = y3

        self.screen.blit(self.tank, self.rect)
        self.screen.blit(self.gun1, self.gun1_rect)
        pygame.draw.line(self.screen, (20, 20, 20), (self.rect.centerx, self.rect.centery), (x3, y3), 10)
        self.screen.blit(self.gun, self.gun_rect)

        if self.hit == 1:
            del self.b[-1]
            self.hit = 0
        if len(self.b) == 0:
            self.die = 1
        for x1 in self.b:
            self.screen.blit(self.blood, (self.rect.centerx+x1-2, self.rect.centery-55))

        self.screen.blit(self.stop, (1250, 20))
        if abs(x - 1265) < 15 and abs(y - 35) < 15:
            self.screen.blit(self.stop1, (1250, 20))
