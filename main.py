import pygame

value=

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PI = 3.141592653
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Cicada's Cool Game")
done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
  #  pygame.draw.rect(screen, RED, [55,50,20,25])
   # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    pygame.display.flip()
    clock.tick(60)



pygame.quit()