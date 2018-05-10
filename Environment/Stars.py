import pygame
import random
import time
from Assists.Position import Position
from Promotion.DiffSpeed import Speed


class Stars:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.white = (255, 255, 255)
        self.starFont = pygame.font.Font(None, 20)
        self.star = self.starFont.render("*", True, self.white)
        self.speed = Speed()
        self.speed.speed = 100
        self.startTime = 0
        self.position = Position()
        self.position.X = random.randint(0, self.screen.get_rect().width)
        self.position.Y = random.randint(0, self.screen.get_rect().height)

    def draw(self):
        if self.startTime != 0:
            self.position.Y += (time.time() - self.startTime) * self.speed.speed
        self.startTime = time.time()
        self.screen.blit(self.star, (self.position.X, self.position.Y))
        if self.position.Y >= self.screen.get_rect().height:
            self.redraw()

    def redraw(self):
        self.position.X = random.randint(0, self.screen.get_rect().width)
        self.position.Y = 0
        self.startTime = time.time()
        self.screen.blit(self.star, (self.position.X, self.position.Y))

    def pause(self):
        self.startTime = 0

    def pause_draw(self):
        self.screen.blit(self.star, (self.position.X, self.position.Y))
