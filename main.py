import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player  = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()
    dt = 0
    while True:
        # User Input
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return

        # Update
        updatable.update(dt)

        # Draw
        screen.fill(0)
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        # FPS 60
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()


