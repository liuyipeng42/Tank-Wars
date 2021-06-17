import math
import time
import pygame
import random
from bullet import Bullet
from pygame.sprite import Sprite, Group


class Enemy(Sprite):
    def __init__(self, screen, bullets_1, move_direction, tank_0, walls, speed, bullet_speed, firing_rate, tank0, bpx, bpy):
        super().__init__()
        self.tank_0 = tank0
        self.screen = screen
        self.walls = walls
        self.tank = pygame.image.load('images/tank 3.png').convert_alpha()
        self.gun = pygame.image.load('images/3.png').convert_alpha()
        self.gun1 = pygame.image.load('images/4.png').convert_alpha()

        self.rect = self.tank.get_rect()
        self.gun_rect = self.gun.get_rect()
        self.gun1_rect = self.gun1.get_rect()
        self.screen_rect = screen.get_rect()

        self.speed = speed
        self.bullet_speed = bullet_speed
        self.firing_rate = firing_rate
        self.mode = 1

        self.rect.centerx = bpx
        self.rect.centery = bpy
        self.x_move = self.rect.centerx
        self.y_move = self.rect.centery

        self.tank_0 = tank_0
        self.bullets_1 = bullets_1
        self.simulate_fire = Group()
        self.t1 = time.time()
        self.t3 = 0
        self.t5 = 0
        self.t7 = 0
        self.t9 = 0
        self.t11 = 0
        self.t13 = 0
        self.t15 = 0
        self.x3 = self.rect.centerx
        self.y3 = self.rect.centery + 50
        self.move_direction = move_direction
        self.gunDirection = [1.57, random.uniform(0, 6.283185307)]

        self.nowgd = 0
        self.lastgd = 4.71238898025
        self.nextgd = 4.71238898025
        self.direction = 0
        self.collision = [0, 0, 0, 0]

        self.b = [-20, -10, 0, 10, 20]
        self.blood = pygame.image.load('images/blood.png').convert_alpha()
        self.rect1 = self.blood.get_rect()
        self.hit = 0
        self.delete = 0
        self.stop = 0

    def generateMoveDirection(self):
        t2 = time.time()
        if t2 - self.t1 >= 2:
            if self.move_direction == 1:
                a = [2, 3, 3, 4, 4]
                self.move_direction = random.choice(a)
            elif self.move_direction == 2:
                a = [1, 3, 3, 4, 4]
                self.move_direction = random.choice(a)
            elif self.move_direction == 3:
                a = [1, 1, 2, 2, 4]
                self.move_direction = random.choice(a)
            elif self.move_direction == 4:
                a = [1, 1, 2, 2, 3]
                self.move_direction = random.choice(a)
            self.t1 = time.time()

        if abs(self.rect.right - self.screen_rect.right) < 3 and self.move_direction == 4:
            a = [1, 2, 3, 3]
            self.move_direction = random.choice(a)
        if self.rect.left < 3 and self.move_direction == 3:
            a = [1, 2, 4, 4]
            self.move_direction = random.choice(a)
        if self.rect.top < 3 and self.move_direction == 1:
            a = [2, 2, 3, 4]
            self.move_direction = random.choice(a)
        if abs(self.rect.bottom - self.screen_rect.bottom) < 3 and self.move_direction == 2:
            a = [1, 1, 3, 4]
            self.move_direction = random.choice(a)

    def changeDirection(self):

        if self.move_direction == 1 and self.rect.top > 0:
            if self.collision[0] != 1:
                self.tank = pygame.image.load('images/tank 3.png').convert_alpha()
                self.y_move -= self.speed
            else:
                a = [2, 3, 4, 3, 4]
                self.move_direction = random.choice(a)
        if self.move_direction == 2 and self.rect.bottom < self.screen_rect.bottom:
            if self.collision[1] != 1:
                self.tank = pygame.image.load('images/tank 3.png').convert_alpha()
                self.y_move += self.speed
            else:
                a = [1, 3, 4, 3, 4]
                self.move_direction = random.choice(a)
        if self.move_direction == 3 and self.rect.left > 0:
            if self.collision[2] != 1:
                self.tank = pygame.image.load('images/tank 4.png').convert_alpha()
                self.x_move -= self.speed
            else:
                a = [1, 2, 1, 2, 4]
                self.move_direction = random.choice(a)
        if self.move_direction == 4 and self.rect.right < self.screen_rect.right:
            if self.collision[3] != 1:
                self.tank = pygame.image.load('images/tank 4.png').convert_alpha()
                self.x_move += self.speed
            else:
                a = [1, 2, 1, 2, 3]
                self.move_direction = random.choice(a)

    def fireSimulateBullet(self):
        t10 = time.time()
        if t10 - self.t9 >= 0.1:
            x = self.tank_0.rect.centerx
            y = self.tank_0.rect.centery
            z = math.sqrt((x - self.rect.centerx) ** 2 + (y - self.rect.centery) ** 2)
            if z == 0:
                z = 50
            x4 = int(self.rect.centerx + 30 * ((x - self.rect.centerx) / z))
            y4 = int(self.rect.centery + 30 * ((y - self.rect.centery) / z))
            new_bullet = Bullet(x4, y4, self.rect.centerx, self.rect.centery,
                                3, self.screen, self.walls, self.tank_0, 1)
            new_bullet.invisible = 1
            new_bullet.reflection = 1
            new_bullet.simulate = 1
            self.simulate_fire.add(new_bullet)
            self.t9 = time.time()

    def fireBullet(self):
        if self.mode == 1:
            t4 = time.time()
            t8 = time.time()
            if t4 - self.t3 >= 1.3:
                self.direction = random.uniform(0, 6.283185307)
                self.lastgd = self.gunDirection[0]
                self.nextgd = self.gunDirection[1]
                self.gunDirection[0] = self.gunDirection[1]
                self.gunDirection[1] = self.direction
                self.nowgd = self.lastgd
                self.t3 = time.time()
            else:
                if t8 - self.t7 > 0.002:
                    self.nowgd, self.x3, self.y3 = self.change_direction(self.lastgd, self.nowgd, self.nextgd,
                                                                         self.rect.centerx, self.rect.centery,
                                                                         self.move_direction, self.speed)
                    self.t7 = time.time()

        if self.mode == 2:
            t14 = time.time()
            t16 = time.time()
            if t14 - self.t13 >= 0.1:
                delta_x = self.tank_0.rect.centerx - self.rect.centerx
                delta_y = self.tank_0.rect.centery - self.rect.centery
                self.direction = math.atan2(delta_y, delta_x)
                self.lastgd = self.nowgd
                self.nextgd = self.gunDirection[1]
                self.gunDirection[0] = self.gunDirection[1]
                self.gunDirection[1] = self.direction
                self.nowgd = self.lastgd
                self.t13 = time.time()
            else:
                if t16 - self.t15 > 0.002:
                    self.nowgd, self.x3, self.y3 = self.change_direction(self.lastgd, self.nowgd, self.nextgd,
                                                                         self.rect.centerx, self.rect.centery,
                                                                         self.move_direction, self.speed)
                    self.t15 = time.time()

        t6 = time.time()
        if t6 - self.t5 >= self.firing_rate and self.stop == 0 and self.mode == 2:
            new_bullet = Bullet(self.x3, self.y3, self.rect.centerx, self.rect.centery,
                                self.bullet_speed, self.screen, self.walls, 0, 1)
            self.t5 = time.time()
            self.bullets_1.add(new_bullet)

    def moveAndBlit(self):
        self.rect.centerx = int(self.x_move + 0.5)
        self.rect.centery = int(self.y_move + 0.5)
        self.gun_rect.centerx = self.rect.centerx
        self.gun_rect.centery = self.rect.centery
        self.gun1_rect.centerx = self.x3
        self.gun1_rect.centery = self.y3
        self.screen.blit(self.tank, self.rect)
        self.screen.blit(self.gun1, self.gun1_rect)
        pygame.draw.line(self.screen, (195, 10, 10), (self.rect.centerx, self.rect.centery), (self.x3, self.y3), 10)
        self.screen.blit(self.gun, self.gun_rect)

    def bloodAndHitBullet(self):
        if self.hit == 1:
            del self.b[-1]
            self.hit = 0
        if len(self.b) == 0:
            self.delete = 1
        for x in self.b:
            self.screen.blit(self.blood, (self.rect.centerx + x - 2, self.rect.centery - 55))
        self.collision = [0, 0, 0, 0]

    @staticmethod
    def change_direction(last, now, _next, centerx, centery, move_direction, speed):
        if abs(_next - last) <= 3.1415926535:
            if abs(_next - now) > 0.06:
                if _next > last:
                    now += 0.08
                if _next < last:
                    now -= 0.08
        else:
            if _next - last > 0:
                if now >= _next - 6.283185307:
                    now -= 0.08
            else:
                if now <= _next + 6.283185307:
                    now += 0.08

        x3 = int(centerx + 52 * math.cos(now))
        y3 = int(centery + 52 * math.sin(now))

        if move_direction == 4:
            x3 += speed
        if move_direction == 3:
            x3 -= speed
        if move_direction == 1:
            y3 -= speed
        if move_direction == 2:
            y3 += speed

        return now, x3, y3

    def update(self):

        self.generateMoveDirection()

        if self.stop == 0:
            self.changeDirection()

        self.fireSimulateBullet()

        if self.stop == 0:
            self.fireBullet()

        self.moveAndBlit()
        self.bloodAndHitBullet()
