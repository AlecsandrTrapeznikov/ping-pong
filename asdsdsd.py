from pygame import*

window = display.set_mode((600,600))

fps = time.Clock()
game = True
class GameSprite(sprite.Sprite):  
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):  
        super().__init__()  
        self.image = transform.scale(image.load(player_image), (size_x, size_y))  
        self.speed = player_speed
        self.rect = self.image.get_rect()  
        self.rect.x =  player_x
        self.rect.y =  player_y
    def reset (self):  
        window.blit(self.image, (self.rect.x, self.rect.y))  

ball=GameSprite('мяч.png',300, 300, 80, 50, 5)
platform2 = GameSprite('platform.png',20, 10, 80, 150, 5)
platform1 = GameSprite('platform.png',550, 10, 80, 150, 5)
x2=1
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
        platform2.rect.y -=  platform2.speed
    elif keys[K_s]:
        platform2.rect.y +=  platform2.speed
    ball.rect.x += x2
    
    if sprite.collide_rect(ball, platform1):
        x2 = -2
    if sprite.collide_rect(ball, platform2):
       x2 =2
        
    window.fill((255,141,24))

    ball.reset()
    platform1.reset()
    platform2.reset()
    fps.tick(60)
    display.update()
    window.blit(img2, (x1,y1))

    display.update()
