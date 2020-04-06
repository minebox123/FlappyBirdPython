import pygame
import os


class Base:

    def __init__(self, x, y, surface):
        self.x = x
        self.y = y
        self.s = surface
        self.image = pygame.image.load(os.path.join("../images", "base.png"))
        self.speed = 3

    def draw_base(self):
        self.s.blit(self.image, (self.x, self.y))

    def move_base(self):
        self.x -= self.speed

        if self.x <= 0:
            self.x = self.s.get_width()

    def get_base_rect(self):
        return self.s.blit(self.image, (self.x, self.y))
