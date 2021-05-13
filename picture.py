import pygame


class Picture:
    def __init__(self, picture_path, pos_x, pos_y):
        self.picture = pygame.image.load(picture_path).convert_alpha()
        self.rect = self.picture.get_rect()
        self.x = pos_x
        self.y = pos_y
        self.rect.centerx = pos_x
        self.rect.centery = pos_y

