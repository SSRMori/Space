import pygame
from Assists.Position import Position
from Assists.Speed import Speed
from Player.Bullet import Bullet


class Ship:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.speedX = Speed()
        self.speedY = Speed()
        self.color = (190, 190, 190)
        self.font = pygame.font.Font(None, 30)
        self.ship = self.font.render("A", True, self.color)
        self.ship_width = self.ship.get_rect().width
        self.ship_height = self.ship.get_rect().height
        self.position = Position()
        self.position.X = self.screen.get_rect().width / 2
        self.position.Y = self.screen.get_rect().height / 8 * 7
        self.bullets = []
        self.life = 4
        self.score = 0

    def move(self):
        self.position.X += self.speedX.cal_speed()
        self.position.Y += self.speedY.cal_speed()
        self.get_valid_position()
        self.screen.blit(
            self.ship,
            (self.position.X - self.ship_width / 2, self.position.Y - self.ship_height / 2)
        )
        for i in range(len(self.bullets) - 1, -1, -1):
            if self.bullets[i].is_not_valid():
                self.bullets.pop(i)
            else:
                self.bullets[i].draw()
        print("Speed.X = " + str(self.speedX.speed))
        print("Speed.Y = " + str(self.speedY.speed))

    def get_valid_position(self):
        if self.position.X < self.ship_width / 2:
            self.position.X = self.ship_width / 2
        elif self.position.X > self.screen.get_rect().width - self.ship_width / 2:
            self.position.X = self.screen.get_rect().width - self.ship_width / 2
        if self.position.Y < self.ship_height / 2:
            self.position.Y = self.ship_height / 2
        elif self.position.Y > self.screen.get_rect().height - self.ship_height / 2:
            self.position.Y = self.screen.get_rect().height - self.ship_height / 2

    def ship_pause(self):
        self.speedX.speed_pause()
        self.speedY.speed_pause()
        self.screen.blit(
            self.ship,
            (self.position.X - self.ship_width / 2, self.position.Y - self.ship_height / 2)
        )
        for bullet in self.bullets:
            bullet.pause()

    def shot(self):
        self.bullets.append(Bullet(self.screen, self.position, self.ship))

    def get_position(self):
        return self.position

    def check_crash(self, e_bullet):
        left = self.position.X - self.ship_width / 2 - 1
        right = self.position.X + self.ship_width / 2 + 1
        up = self.position.Y - self.ship_height / 2 - 1
        down = self.position.Y + self.ship_height / 2 + 1
        if left <= e_bullet.position.X <= right:
            if up <= e_bullet.position.Y <= down:
                self.life -= 1
                return True
        else:
            return False

    def check_alive(self):
        if self.life <= 0:
            return False
        else:
            return True

    def score_plus(self):
        self.score += 2

    def score_minus(self):
        self.score -= 1
        if self.score < 0:
            self.score = 0
