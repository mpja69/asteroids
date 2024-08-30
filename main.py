import pygame
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player  = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        # User Input
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return

        # Update
        player.update(dt)

        # Draw
        screen.fill(0)
        player.draw(screen)
        pygame.display.flip()

        # FPS 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()


