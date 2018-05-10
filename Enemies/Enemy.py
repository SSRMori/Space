import pygame
import time
import random
from Assists.Position import Position


class Enemy:
    def __init__(self, screen, player):
        pygame.init()
        self.screen = screen
        self.color = (255, 0, 255)
        self.font = pygame.font.Font(None, 30)
        self.ship = self.font.render("o", True, self.color)
        self.speed = 50
        self.position = Position()
        self.position.Y = - self.ship.get_rect().height / 2
        self.position.X = random.randint(
            self.ship.get_rect().width / 2,
            self.screen.get_rect().width - self.ship.get_rect().width
        )
        self.startTime = time.time()
        self.player = player
        self.shotTime = time.time()

    def draw(self):
        self.position.Y += self.speed * (time.time() - self.startTime)
        self.screen.blit(
            self.ship,
            (self.position.X - self.ship.get_rect().width / 2, self.position.Y - self.ship.get_rect().height / 2)
        )
        self.startTime = time.time()

    def pause(self):
        self.screen.blit(
            self.ship,
            (self.position.X - self.ship.get_rect().width / 2, self.position.Y - self.ship.get_rect().height / 2)
        )
        self.startTime = time.time()

    def check_valid(self):
        if self.position.Y >= self.screen.get_rect().height + self.ship.get_rect().height / 2:
            return False
        else:
            return True

    def check_crash(self, bullet):
        if bullet.position.Y <= self.position.Y + self.ship.get_rect().height / 2 + 3:
            if bullet.position.Y >= self.position.Y - self.ship.get_rect().height / 2 - 3:
                if bullet.position.X <= self.position.X + self.ship.get_rect().width / 2 + 3:
                    if bullet.position.X >= self.position.X - self.ship.get_rect().width / 2 - 3:
                        return True
        else:
            return False

    def will_shot(self):
        return self.player.get_position().X - 0.5 <= self.position.X <= self.player.get_position().X + 0.5

    def is_crash_with_player(self):
        left = self.player.get_position().X - self.player.ship_width / 2 - self.ship.get_rect().width / 2 - 1
        right = self.player.get_position().X + self.player.ship_width / 2 + self.ship.get_rect().width / 2 + 1
        up = self.player.get_position().Y - self.player.ship_height / 2 - self.ship.get_rect().width / 2 - 1
        down = self.player.get_position().Y + self.player.ship_height / 2 + self.ship.get_rect().height / 2 + 1
        if left <= self.position.X <= right:
            if up <= self.position.Y <= down:
                return True
            else:
                return False

    def get_position(self):
        return self.position

    def is_permitted_to_shot(self):
        if time.time() - self.shotTime >= 1:
            self.shotTime = time.time()
            return True
        else:
            return False
