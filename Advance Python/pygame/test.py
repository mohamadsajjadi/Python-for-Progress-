import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])

while True:
    for event in pygame.event.get():
        print(type(event))
        if event.type == pygame.QUIT:
            exit()
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.display.flip()
