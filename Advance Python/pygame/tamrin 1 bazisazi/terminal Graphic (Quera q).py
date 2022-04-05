import pygame as pygame
import sys as sys

pygame.init()
screen = pygame.display.set_mode((300, 300))
background_color = (255, 255, 255)
COLOR = (0, 0, 0)
screen.fill(background_color)
pygame.display.update()
thickness = 1

while True:
    calculate_list = input().split()
    if calculate_list[1] == 'line':
        pygame.draw.line(screen, COLOR, (int(calculate_list[2]), int(calculate_list[3])),
                         (int(calculate_list[4]), int(calculate_list[5])), thickness)
    elif calculate_list[1] == 'circle':
        pygame.draw.circle(screen, COLOR, (int(calculate_list[2]), int(calculate_list[3])), int(calculate_list[4]),
                           thickness)
    elif calculate_list[1] == 'polygon':
        main = [(int(x), int(y)) for x, y in zip(calculate_list[2::2], calculate_list[3::2])]
        pygame.draw.polygon(screen, COLOR, main,thickness)
        pygame.display.update()

    elif calculate_list[0] == 'change':
        if calculate_list[1] == 'color':
            COLOR = (int(calculate_list[2]), int(calculate_list[3]), int(calculate_list[4]))
        if calculate_list[1] == 'size':
            thickness = int(calculate_list[2])

    elif calculate_list[0] == 'end':
        pygame.image.save(screen, 'draw.png')
        sys.exit()
pygame.display.update()

while True:
    pygame.event.pump()
