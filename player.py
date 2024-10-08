import pygame
from pygame.transform import rotate
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_COOLDOWN, SHOT_RADIUS, SHOT_SPEED
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x,y)
        self.rotation = 0
        self.timer = 0


    # The points in the triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def move(self, dt):
        v = pygame.Vector2(0,1)
        v = v.rotate(self.rotation)
        v *= PLAYER_SPEED * dt
        self.position += v


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt


    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()


    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def shoot(self):

        if self.timer > 0:
            return
        self.timer = SHOT_COOLDOWN
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        p = self.position + forward * self.radius
        shot = Shot(p.x, p.y, SHOT_RADIUS)
        shot.velocity = forward * SHOT_SPEED
        
