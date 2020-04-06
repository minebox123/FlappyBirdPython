import pygame
import os


class Score:
    """
    Counts and shows the current player's scores
    """

    def __init__(self, surface):
        self.img_dist = "../images"

        self.scores = 0
        self.s = surface

    def show_scores(self):
        images = (
            pygame.image.load(os.path.join(self.img_dist, "0.png")),
            pygame.image.load(os.path.join(self.img_dist, "1.png")),
            pygame.image.load(os.path.join(self.img_dist, "2.png")),
            pygame.image.load(os.path.join(self.img_dist, "3.png")),
            pygame.image.load(os.path.join(self.img_dist, "4.png")),
            pygame.image.load(os.path.join(self.img_dist, "5.png")),
            pygame.image.load(os.path.join(self.img_dist, "6.png")),
            pygame.image.load(os.path.join(self.img_dist, "7.png")),
            pygame.image.load(os.path.join(self.img_dist, "8.png")),
            pygame.image.load(os.path.join(self.img_dist, "9.png")),
        )

        digits = [int(x) for x in list(str(self.scores))]
        x = 130
        for digit in digits:
            self.s.blit(images[digit], (x, 50))
            x += images[digit].get_width()

    def add_score(self):
        self.scores += 1
