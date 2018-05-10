import pygame
import time
from Assists.pauseText import PauseText


class GameOver:
    def __init__(self, screen, ship):
        pygame.init()
        self.screen = screen
        self.ship = ship
        self.startTime = time.time()
        self.colorValue = 0
        self.color = (self.colorValue, self.colorValue, self.colorValue)
        self.big_font = pygame.font.Font(None, 80)
        self.game_over = self.big_font.render("Game Over", True, self.color)
        self.small_font = pygame.font.Font(None, 40)
        self.scoreText = "You've got %d points." % self.ship.score
        self.score = self.small_font.render(self.scoreText, True, self.color)
        self.endText = PauseText(self.screen)
        self.endText.text = "Press ESC to quit"
        self.first = False
        self.second = False

    def set_big_color(self):
        self.colorValue = (time.time() - self.startTime) * 255
        if self.colorValue < 255:
            self.color = (self.colorValue, self.colorValue, self.colorValue)
        else:
            self.color = (255, 255, 255)
        self.game_over = self.big_font.render("Game Over", True, self.color)

    def set_small_color(self):
        self.colorValue = (time.time() - self.startTime - 1) * 255
        if self.colorValue < 255:
            self.color = (self.colorValue, self.colorValue, self.colorValue)
        else:
            self.color = (255, 255, 255)
            self.second = True
        self.score = self.small_font.render(self.scoreText, True, self.color)

    def draw(self):
        self.set_big_color()
        self.screen.blit(
            self.game_over,
            (self.screen.get_rect().width / 2 - self.game_over.get_rect().width / 2,
             self.screen.get_rect().height / 4 * 1 - self.game_over.get_rect().height / 2)
        )
        if time.time() - self.startTime >= 1:
            self.set_small_color()
            self.screen.blit(
                self.score,
                (self.screen.get_rect().width / 2 - self.score.get_rect().width / 2,
                 self.screen.get_rect().height / 2 - self.score.get_rect().height / 2)
            )
        if time.time() - self.startTime >= 2:
            self.endText.show_pause_text(
                self.screen.get_rect().width / 2,
                self.screen.get_rect().height / 3 * 2
            )
