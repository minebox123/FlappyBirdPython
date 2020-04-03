import pygame
import os


class Bird:
    """
    Flappy bird
    """

    def __init__(self, x, y, surface):
        self.x = x
        self.y = y
        self.s = surface
        self.vel = 1
        self.gravity = 9.8
        self.bird_mid_pos = pygame.image.load(os.path.join("../images", "yellowbird-midflap.png"))
        self.bird_up_pas = pygame.image.load(os.path.join("../images", "yellowbird-upflap.png"))

    def draw(self):
        self.s.blit(self.bird_mid_pos, (self.x, self.y))

    def move_down(self):
        ground = self.s.get_rect().height - 112
        bird_height = self.bird_mid_pos.get_rect().height
        # move bird down

        # if (self.y + bird_height >= ground):
        #     self.vel = -self.vel

        self.y += self.vel * self.gravity

        print(self.y)

    def move_up(self):
        bird_height = self.bird_mid_pos.get_rect().height

        self.s.blit(self.bird_up_pas, (self.x, self.y))
        self.y -= self.vel * bird_height
