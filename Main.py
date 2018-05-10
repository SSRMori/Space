import pygame
import sys
import time
from Environment.Stars import Stars
from Assists.pauseText import PauseText
from Player.Ship import Ship
from Assists.Music import Music
from Enemies.Enemy import Enemy
from Enemies.Enemy_Bullet import EBullet
from Assists.Info import Info
from Assists.GameOver import GameOver


pygame.init()
Game_Title = "SPACE"
screen_width = 400
screen_height = 400
screen_background = (0, 0, 0)
screen_icon = pygame.image.load("Icon/space-shuttle.jpg")
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SPACE")
pygame.display.set_icon(screen_icon)
Title = pygame.font.Font(None, 80).render(Game_Title, True, (255, 255, 255))
isStart = False
background_music = Music()
ship = Ship(screen)
pause = PauseText(screen)
isPause = False
stars = []
starNum = 20
for i in range(0, starNum):
    stars.append(Stars(screen))
info = Info(screen, ship)

while not isStart:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            isStart = True
    screen.fill(screen_background)
    screen.blit(
        Title,
        (screen_width / 2 - Title.get_rect().width / 2, screen_height / 12 * 5 - Title.get_rect().height / 2)
    )
    pause.show_pause_text(screen_width / 2, screen_height / 3 * 2)
    pygame.display.update()
pause.stop_pause()

enemies = []
enemy_time = time.time()
enemy_bullets = []
background_music.play()
while ship.check_alive():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                for star in stars:
                    star.pause()
                    isPause = True
                background_music.pause()
                while isPause:
                    for eventP in pygame.event.get():
                        if eventP.type == pygame.KEYDOWN:
                            isPause = False
                        elif eventP.type == pygame.QUIT:
                            sys.exit()
                    screen.fill(screen_background)
                    for star in stars:
                        star.pause_draw()
                    info.draw()
                    ship.ship_pause()
                    for i in range(0, len(enemies)):
                        enemies[i].pause()
                    for i in range(0, len(enemy_bullets)):
                        enemy_bullets[i].pause()
                    pause.show_pause_text(screen_width / 2, screen_height / 2)
                    pygame.display.update()
                pause.stop_pause()
                ship.speedX.speed = 0
                ship.speedY.speed = 0
                background_music.continue_play()
            if event.key == pygame.K_j:
                ship.shot()
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                ship.speedX.add_negative_acc()
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                ship.speedX.add_positive_acc()
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                ship.speedY.add_negative_acc()
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                ship.speedY.add_positive_acc()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                ship.speedX.release_negative_acc()
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                ship.speedX.release_positive_acc()
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                ship.speedY.release_negative_acc()
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                ship.speedY.release_positive_acc()
    if time.time() - enemy_time > 1:
        enemies.append(Enemy(screen, ship))
        enemy_time = time.time()
    screen.fill(screen_background)

    for star in stars:
        star.draw()
    ship.move()

    info.draw()

    for i in range(len(enemies) - 1, -1, -1):
        enemies[i].draw()
        if enemies[i].will_shot() and enemies[i].is_permitted_to_shot():
            enemy_bullets.append(EBullet(screen, enemies[i]))
        if not enemies[i].check_valid():
            enemies.pop(i)
            ship.score_minus()
            break
        if enemies[i].is_crash_with_player():
            enemies.pop(i)
            ship.life -= 1
            ship.score_plus()
        else:
            for j in range(len(ship.bullets) - 1, -1, -1):
                if enemies[i].check_crash(ship.bullets[j]):
                    enemies.pop(i)
                    ship.bullets.pop(j)
                    ship.score_plus()
                    break

    for i in range(len(enemy_bullets) - 1, -1, -1):
        enemy_bullets[i].draw()
        if ship.check_crash(enemy_bullets[i]) or enemy_bullets[i].is_not_valid():
            enemy_bullets.pop(i)

    pygame.display.update()
    background_music.check_play()
time.sleep(1)
print("Your score is " + str(ship.score))
endText = GameOver(screen, ship)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    screen.fill(screen_background)
    endText.draw()
    pygame.display.update()
