import time
import pygame


class PauseText:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.font = pygame.font.Font(None, 20)
        self.colorValue = 255
        self.color = (self.colorValue, self.colorValue, self.colorValue)
        self.text = "Press any key to start"
        self.textRender = self.font.render(self.text, True, self.color)
        self.startTime = 0
        self.isLighten = -1

    def set_color(self):
        self.color = (self.colorValue, self.colorValue, self.colorValue)
        self.textRender = self.font.render(self.text, True, self.color)

    def show_pause_text(self, pos_x, pos_y):
        if self.startTime != 0:
            self.colorValue += self.isLighten * (time.time() - self.startTime) * 255
        self.startTime = time.time()
        if self.colorValue >= 255:
            self.colorValue = 255
            self.isLighten *= -1
        elif self.colorValue <= 0:
            self.colorValue = 0
            self.isLighten *= -1
        self.set_color()
        self.screen.blit(
            self.textRender,
            (pos_x - self.textRender.get_rect().width / 2, pos_y - self.textRender.get_rect().height / 2)
            )

    def stop_pause(self):
        self.colorValue = 255
        self.set_color()
        self.startTime = 0
        self.isLighten = -1
