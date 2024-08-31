import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


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
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player  = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Shot.containers = (updatable, drawable, shots)

    dt = 0
    while True:
        # User Input
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return

        # Update
        updatable.update(dt)

        # Collision
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game Over!")
                return
            for shot in shots:
                if shot.is_colliding(asteroid):
                    asteroid.split()
                    shot.kill()


        # Draw
        screen.fill("black")
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        # FPS 60
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()


