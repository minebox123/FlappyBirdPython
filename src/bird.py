import pygame
import os
import math


class Bird:
    """
    Flappy bird
    """

    def __init__(self, x, y, surface):
        self.x = x
        self.y = y
        self.s = surface
        self.vel = 2
        self.gravity = 2
        self.strength = 17
        self.bird_mid_pos = pygame.image.load(os.path.join("../images", "yellowbird-midflap.png"))
        self.bird_up_pas = pygame.image.load(os.path.join("../images", "yellowbird-upflap.png"))
        self.bird_down_pos = pygame.image.load(os.path.join("../images", "yellowbird-downflap.png"))

    def draw(self):
        self.s.blit(self.bird_mid_pos, (self.x, self.y))

    def move_down(self):
        ground = self.s.get_rect().height - 112
        # bird_height = self.bird_mid_pos.get_rect().height
        # bird_down = pygame.transform.rotate(self.bird_down_pos, -30)
        # self.s.blit(bird_down, (self.x, self.y))
        # move bird down

        self.vel += self.gravity
        self.y += self.vel

    def move_up(self):
        # bird_height = self.bird_mid_pos.get_rect().height

        # bird_up = pygame.transform.rotate(self.bird_up_pas, 30)
        # self.s.blit(bird_up, (self.x, self.y))

        self.vel = -self.strength

    def get_bird_rect(self):
        return self.s.blit(self.bird_down_pos, (self.x, self.y))
