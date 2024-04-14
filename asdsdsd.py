from pygame import*

window = display.set_mode((600,600))

fps = time.Clock()
game = True
img = Surface((20, 150))
img2 = Surface((20, 150))
x = 20
y = 10
x1 = 560
y1 = 10

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    window.fill((255,255,255))
    window.blit(img, (x,y))
    window.blit(img2, (x1,y1))

    display.update()
