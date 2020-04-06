import pygame
import sys
import os
import random

from settings import Settings
from bird import Bird
from base import Base
from pipes import Pipes
from score import Score


class Game:
    """
    Creates a setup class for the game
    """

    def __init__(self):
        self.s = Settings()
        self.window = pygame.display.set_mode((self.s.window_width, self.s.window_height))
        self.fps = pygame.time.Clock()
        self.background = pygame.image.load(os.path.join("../images", "background-day.png"))
        # 10 is width of the bird (approximately)

        self.bird = Bird(self.s.window_width / 2 - 10, self.s.window_height // 2, self.window)
        self.base = Base(0, self.s.window_height - self.s.base_height, self.window)
        self.score = Score(self.window)
        # self.pipes = Pipes(self.base.get_base_rect().height, self.window)
        self.pipes = []
        self.distance = 0

        self.start_game = False
        self.game_over = False

    def play(self):
        run = True
        self.create_pipes()

        while run:
            self.fps.tick(30)

            # bird
            if not self.start_game:
                self.bird.draw()
                self.stop_game()
            else:
                self.flappy_bird()
                for pipes in self.pipes:
                    pipes.draw_pipes(self.bird.get_bird_rect())
                    pipes.move_pipes()
                    self.collision_detection(self.bird.get_bird_rect(), pipes.get_top_pipe(), pipes.get_bottom_pipe(), pipes.get_score_line())

            if self.game_over:
                self.game_over_func()

            # handles user's interaction
            self.user_events()

            # user scores
            self.score.show_scores()

            # handles background move
            self.move_ground()

            self.display_settings()

    def display_settings(self):
        pygame.display.update()
        self.window.blit(self.background, (0, 0))

    def user_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.game_over:
                    self.start_game = True
                    self.bird.move_up()

    def flappy_bird(self):
        self.bird.move_down()
        self.score.show_scores()

    def move_ground(self):
        self.base.draw_base()

    def create_pipes(self):
        for pipes in range(100):
            random_size = self.s.pipes_sizes[random.randrange(len(self.s.pipes_sizes))]
            self.distance += 200
            self.pipes.append(Pipes(self.window, random_size[0], random_size[1], self.distance))

    def stop_game(self):
        self.start_game = False

    def game_over_func(self):
        game_over_img = pygame.image.load(os.path.join("../images", "gameover.png"))
        self.window.blit(game_over_img, (60, 100))

    def collision_detection(self, bird, top_pipe, bottom_pipe, score_line):
        # Check for pipe-bird collision
        if (bird.x + bird.width >= top_pipe.x and bird.x <= top_pipe.x + top_pipe.width and
                bird.y <= top_pipe.y + top_pipe.height):
            self.game_over = True
            self.stop_game()

        if (bird.x + bird.width >= bottom_pipe.x and bird.x <= bottom_pipe.x + bottom_pipe.width and
                bird.y + bird.height >= bottom_pipe.y):
            self.game_over = True
            self.stop_game()

        if bird.x == score_line.x:
            self.score.add_score()
            # self.score.show_scores()


if __name__ == "__main__":
    game = Game()
    game.play()
