import pygame
BLACK = (0, 0, 0)
pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('platformer game')
clock = pygame.time.Clock()

running =True
while running:
    clock.tick(60)

    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pass

    screen.fill(BLACK)
    pygame.display.flip()


pygame.quit()