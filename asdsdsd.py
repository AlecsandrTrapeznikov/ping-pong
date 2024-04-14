from pygame import*

window = display.set_mode((600,600))
fps = time.Clock()
game = True
img = Surface(20, 100)

while game:
  for e in event.get():
      if e.type == QUIT:
          game = False

  display.update()
