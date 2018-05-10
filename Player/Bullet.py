import pygame
import time
from Assists.Position import Position


class Bullet:
    def __init__(self, screen, ship_position, ship):
        pygame.init()
        self.screen = screen
        self.startTime = time.time()
        self.speed = 120
        self.color = (255, 255, 0)
        self.font = pygame.font.Font(None, 20)
        self.bullet = self.font.render("^", True, self.color)
        self.ship = ship
        self.ship_position = ship_position
        self.position = Position()
        self.position.X = self.ship_position.X - self.bullet.get_rect().width / 2
        self.position.Y = self.ship_position.Y - self.ship.get_rect().height / 2

    def draw(self):
        self.position.Y -= self.speed * (time.time() - self.startTime)
        self.screen.blit(self.bullet, (self.position.X, self.position.Y))
        self.startTime = time.time()

    def is_not_valid(self):
        if self.position.Y <= 0:
            return True
        else:
            return False

    def pause(self):
        self.screen.blit(self.bullet, (self.position.X, self.position.Y))
        self.startTime = time.time()
