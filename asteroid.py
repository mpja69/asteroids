import random
import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand = random.uniform(20,50)
        v1 = self.velocity.rotate(rand)
        v2 = self.velocity.rotate(-rand)
        radius = self.radius - ASTEROID_MIN_RADIUS
        p = self.position
        a1 = Asteroid(p.x, p.y, radius)
        a2 = Asteroid(p.x, p.y, radius)
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2




