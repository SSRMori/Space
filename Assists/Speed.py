import time


class Speed:
    def __init__(self):
        self.speed = 0
        self.startTime = 0
        self.maxSpeed = 10

    def add_positive_acc(self):
        self.speed += 0.15

    def add_negative_acc(self):
        self.speed -= 0.15

    def release_positive_acc(self):
        self.speed -= 0.15

    def release_negative_acc(self):
        self.speed += 0.15

    def cal_speed(self):
        return self.speed

    def speed_pause(self):
        self.startTime = time.time()

