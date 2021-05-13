import math
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, bullet_x, bullet_y, tank_x, tank_y, bullet_speed, screen, walls, tank_0, color):
        super().__init__()
        self.bullet_x = bullet_x
        self.bullet_y = bullet_y
        self.tank_x = tank_x
        self.tank_y = tank_y
        self.b_x = 0
        self.b_y = 0
        self.screen = screen
        self.walls = walls
        self.collision = 0
        self.collision1 = 0
        self.collision2 = 0
        self.reflection = 0
        self.screen_rect = screen.get_rect()
        self.bullet_speed = bullet_speed
        self.v = 0
        self.rect = pygame.Rect(self.bullet_x, self.bullet_y, 9, 9)
        self.rect.centerx = bullet_x
        self.rect.centery = bullet_y
        self.bullet_posx = self.rect.centerx
        self.bullet_posy = self.rect.centery
        self.k = math.tan(math.atan2(self.bullet_y - self.tank_y, self.bullet_x - self.tank_x))
        self.b = self.tank_y - self.k * self.tank_x
        self.boundary = 3
        self.invisible = 0
        self.tank_0 = tank_0
        self.hit = 0
        self.change = 0
        self.simulate = 0
        self.stop = 0
        self.color = color

    def update(self):

        if self.hit == 0:
            if self.collision == 1:
                self.b_x = self.rect.centerx
                self.b_y = self.rect.centery
                self.k = -self.k
                self.b = self.b_y - self.k * self.b_x
                self.collision = 2

            if self.stop == 0:
                if abs(self.k) < 1:
                    self.v = math.sqrt(1/(self.k**2+1))*self.bullet_speed
                    if self.simulate == 1:
                        self.v = 4*self.v
                    if self.collision1 == 1:
                        if self.bullet_x > self.tank_x:
                            self.bullet_posx -= self.v
                        else:
                            self.bullet_posx += self.v
                    else:
                        if self.bullet_x > self.tank_x:
                            self.bullet_posx += self.v
                        else:
                            self.bullet_posx -= self.v
                    self.rect.centerx = int(self.bullet_posx + 0.5)
                    self.rect.centery = int(self.k*self.bullet_posx+self.b+1)
                else:
                    self.v = math.sqrt((self.k**2)/(self.k**2+1))*self.bullet_speed
                    if self.simulate == 1:
                        self.v = 4*self.v
                    if self.collision1 == 2:
                        if self.bullet_y > self.tank_y:
                            self.bullet_posy -= self.v
                        else:
                            self.bullet_posy += self.v
                    else:
                        if self.bullet_y > self.tank_y:
                            self.bullet_posy += self.v
                        else:
                            self.bullet_posy -= self.v
                    self.rect.centery = int(self.bullet_posy+0.5)
                    self.rect.centerx = int((self.bullet_posy-self.b)/self.k+1)

            if self.invisible == 0:
                if self.color == 0:
                    pygame.draw.circle(self.screen, (0, 0, 0), (self.rect.centerx, self.rect.centery), 5)
                else:
                    pygame.draw.circle(self.screen, (200, 0, 0), (self.rect.centerx, self.rect.centery), 5)

            right = abs(self.rect.right-self.screen_rect.right)
            left = abs(self.rect.left-self.screen_rect.left)
            up = abs(self.rect.top-self.screen_rect.top)
            down = abs(self.rect.bottom-self.screen_rect.bottom)

            if self.simulate == 1:
                self.boundary = 10

            if right <= self.boundary or left <= self.boundary or up <= self.boundary or down <= self.boundary:
                self.collision = 1
                self.reflection += 1
                if right <= self.boundary or left <= self.boundary:
                    self.collision1 = 1
                if up <= self.boundary or down <= self.boundary:
                    self.collision1 = 2

        if self.hit == 1:
            if self.change == 0:
                self.bullet_posx = self.tank_0.rect.centerx
                self.bullet_posy = self.tank_0.rect.centery
                self.change = 1

            if self.tank_0.moving_right:
                self.bullet_posx += self.tank_0.speed - 0.65
            if self.tank_0.moving_left:
                self.bullet_posx -= self.tank_0.speed - 0.65
            if self.tank_0.moving_up:
                self.bullet_posy -= self.tank_0.speed - 0.65
            if self.tank_0.moving_down:
                self.bullet_posy += self.tank_0.speed - 0.65

            self.rect.centery = int(self.bullet_posy)
            self.rect.centerx = int(self.bullet_posx)

