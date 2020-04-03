import pygame
import sys
import os

from settings import Settings
from bird import Bird


class Game:
    """
    Creates a setup class for the game
    """

    def __init__(self):
        self.s = Settings()
        self.window = pygame.display.set_mode((self.s.window_width, self.s.window_height))
        self.fps = pygame.time.Clock()
        self.background = pygame.image.load(os.path.join("../images", "background-day.png"))
        self.ground = pygame.image.load(os.path.join("../images", "base.png"))
        # 10 is width of the bird (approximately)
        self.bird = Bird(self.s.window_width / 2 - 10, self.s.window_height // 2, self.window)

    def play(self):
        run = True

        while run:
            self.fps.tick(30)

            # bird
            self.flappy_bird()

            # handles user's interaction
            self.user_events()

            self.display_settings()

    def display_settings(self):
        pygame.display.flip()
        self.window.blit(self.background, (0, 0))
        self.window.blit(self.ground, (0, self.s.window_height - self.s.base_height))
        # self.window.fill((255, 0, 0))

    def user_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.bird.move_up()

    def flappy_bird(self):
        self.bird.draw()
        self.bird.move_down()


if __name__ == "__main__":
    game = Game()
    game.play()
