from pygame import*

window = display.set_mode((600,600))

fps = time.Clock()
game = True
img = Surface((20, 150))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((255,255,255))
    window.blit(img, (5,5))

    display.update()
