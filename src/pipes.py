import pygame
import os
import random

from settings import Settings


class Pipes:

    def __init__(self, surface, top_height, bottom_height, distance=0):
        self.pipe = pygame.image.load(os.path.join("../images", "pipe-green.png"))
        self.s = surface
        self.pipe_height = self.pipe.get_height()
        self.topX = self.s.get_width()
        self.topY = 0 - 65
        self.bottomX = self.s.get_width()
        # self.bottomY = self.s.get_height() - ground_height
        self.bottomY = self.s.get_height() - self.pipe_height - 112 + 65  # 112 is base height
        self.speed = 2
        self.distance = distance
        self.top_height = top_height
        self.bottom_height = bottom_height
        self.top = 0
        self.bottom = 0
        self.score_line = 0

    def move_pipes(self):
        self.topX -= self.speed
        self.bottomX -= self.speed

    def draw_pipes(self, bird):
        top_pipe = pygame.transform.rotate(self.pipe, 180)
        top_pipe = pygame.transform.flip(top_pipe, True, False)
        top_pipe = self.s.blit(top_pipe, (self.topX + self.distance, self.topY + self.top_height))
        bottom_pipe = self.s.blit(self.pipe, (self.bottomX + self.distance, self.bottomY + self.bottom_height))

        score_line = pygame.draw.line(self.s, (255, 255, 255), (top_pipe.x + top_pipe.width, top_pipe.y + top_pipe.height), (bottom_pipe.x + bottom_pipe.width, bottom_pipe.y), 0)

        self.top = top_pipe
        self.bottom = bottom_pipe
        self.score_line = score_line

    def get_top_pipe(self):
        return self.top

    def get_bottom_pipe(self):
        return self.bottom

    def get_score_line(self):
        return self.score_line
