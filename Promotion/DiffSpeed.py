import time


class Speed:
    def __init__(self):
        self.speed = 0
        self.accelerate = 0
        self.friction = 0.08
        self.startTime = 0
        self.maxSpeed = 10

    def add_positive_acc(self):
        self.accelerate += 0.2

    def add_negative_acc(self):
        self.accelerate -= 0.2

    def release_positive_acc(self):
        self.accelerate -= 0.2

    def release_negative_acc(self):
        self.accelerate += 0.2

    def cal_speed(self):
        if self.startTime == 0 and self.accelerate != 0:
            self.friction = self.friction * -1 * abs(self.accelerate) / self.accelerate
            self.startTime = time.time()
        elif self.startTime != 0 or (self.speed != 0 and self.accelerate == 0):
            self.set_friction()
            self.speed += (self.accelerate + self.friction) * (time.time() - self.startTime)
            self.startTime = time.time()
            if int(self.speed * 100) == 0 and self.accelerate == 0:
                self.renew()
        return self.speed

    def speed_pause(self):
        self.startTime = time.time()

    def set_friction(self):
        if self.speed == 0:
            self.friction = 0.08
        else:
            self.friction = -1 * abs(self.speed) / self.speed * abs(self.friction)

    def renew(self):
        self.startTime = 0
        self.speed = 0
