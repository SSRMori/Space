import pygame


class Music:
    def __init__(self):
        pygame.init()
        self.filename = "Music/Ahxello - Infinity.mp3"
        self.volume = 0.3
        self.isPlay = False
        pygame.mixer.music.load(self.filename)
        pygame.mixer.music.set_volume(self.volume)

    def play(self):
        pygame.mixer.music.play(0, 0)
        self.isPlay = True

    def check_play(self):
        self.isPlay = pygame.mixer.music.get_busy()
        if not self.isPlay:
            self.play()

    def pause(self):
        pygame.mixer.music.pause()
        self.isPlay = False

    def continue_play(self):
        pygame.mixer.music.unpause()
        self.isPlay = True

    def stop(self):
        pygame.mixer.music.stop()
        self.isPlay = False

    def replay(self):
        pygame.mixer.music.rewind()
        self.play()
        self.isPlay = True
