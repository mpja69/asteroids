import pygame
from constants import *


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # User Input
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return

        # Update
        # Draw
        screen.fill(0)
        pygame.display.flip()

if __name__ == "__main__":
    main()


