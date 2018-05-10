import pygame


class Info:
    def __init__(self, screen, ship):
        pygame.init()
        self.font = pygame.font.Font(None, 40)
        self.white = (255, 255, 255)
        self.screen = screen
        self.ship = ship
        self.lifeText = "HP %03d" % (self.ship.life - 1)
        self.life = self.font.render(self.lifeText, True, self.white)
        self.scoreText = "SCORES %03d" % self.ship.score
        self.score = self.font.render(self.scoreText, True, self.white)

    def draw(self):
        self.lifeText = "HP %03d" % (self.ship.life - 1)
        self.life = self.font.render(self.lifeText, True, self.white)
        self.scoreText = "SCORES %03d" % self.ship.score
        self.score = self.font.render(self.scoreText, True, self.white)
        self.screen.blit(self.life, (0, 0))
        self.screen.blit(self.score, (self.screen.get_rect().width - self.score.get_rect().width, 0))
