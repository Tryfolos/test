#A test project that experiments with embedding resource files/data inside the exe and reading from it succesfully.
import pygame
import sys

pygame.init()

window = pygame.display.set_mode((1600, 900))

while True:
    for f in pygame.event.get():
        if f.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    pygame.display.flip()