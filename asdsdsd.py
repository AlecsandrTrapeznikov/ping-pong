from pygame import *
from random import randint
font.init()

window = display.set_mode((600, 600))

fps = time.Clock()
game = True


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, player_points):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.points = player_points

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


ball = GameSprite('мяч.png', 300, 300, 80, 50, 5, 0)
platform2 = GameSprite('platform.png', 20, 10, 80, 150, 5, 0)
platform1 = GameSprite('platform.png', 550, 10, 80, 150, 5, 0)
x2 = 1
y2 = 1
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys = key.get_pressed()
    if keys[K_UP]:
        platform1.rect.y -= platform1.speed
    elif keys[K_DOWN]:
        platform1.rect.y += platform1.speed
    if keys[K_w]:
        platform2.rect.y -= platform2.speed
    elif keys[K_s]:
        platform2.rect.y += platform2.speed
    ball.rect.x += x2
    ball.rect.y += y2

    if sprite.collide_rect(ball, platform1):
        x2 = -2
        y2 = -y2 * (randint(1, 10))
    if sprite.collide_rect(ball, platform2):
        x2 = 2
        y2 = -y2 * (randint(1, 10))
    if ball.rect.x > 620:
        ball.rect.x = 300
        ball.rect.y = 300
    if ball.rect.y > 620:
        ball.rect.x = 300
        ball.rect.y = 300
    if ball.rect.x < 0:
        ball.rect.x = 300
        ball.rect.y = 300
    if ball.rect.y == 0:
        ball.rect.x = 300
        ball.rect.y = 300
    if ball.rect.x > 600 and ball.rect.y < 600:
        platform1.points += 1
    if ball.rect.x < 0 and ball.rect.y < 600:
        platform2.points += 1
    window.fill((255, 141, 24))

    ball.reset()
    platform1.reset()
    platform2.reset()
    fps.tick(60)
    display.update()
