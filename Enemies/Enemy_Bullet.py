from Player.Bullet import Bullet


class EBullet(Bullet):
    def __init__(self, screen, enemy):
        Bullet.__init__(self, screen, enemy.get_position(), enemy.ship)
        self.color = (0, 0, 255)
        self.bullet = self.font.render("v", True, self.color)
        self.speed = self.speed * -1
        self.position.X = self.ship_position.X - self.bullet.get_rect().width / 2
        self.position.Y = self.ship_position.Y + self.ship.get_rect().height / 2

    def is_not_valid(self):
        if self.position.Y >= self.screen.get_rect().height + self.bullet.get_rect().height / 2:
            return True
        else:
            return False

