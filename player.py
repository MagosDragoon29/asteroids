import pygame
from circleshape import CircleShape
from constants import *


white = (255, 255, 255)


class Player(CircleShape):
    def __init__(self, x, y, radius):
        
        super().__init__(x, y, radius)
        if hasattr(self, 'containers'):
            self.add(self.containers)
        self.rotation = 0
        self.shot_timer = 0

        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, white, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE] and self.shot_timer <= 0:
            self.shoot(dt)
            self.shot_timer = PLAYER_SHOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        bullet = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0,1)
        rotated_forward = forward.rotate(self.rotation)
        bullet.velocity = rotated_forward * PLAYER_SHOOT_SPEED
        
        





class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        if hasattr(self, 'containers'):
            self.add(self.containers)
    
    def draw(self, screen):
        pygame.draw.circle(screen, white, self.position, self.radius, width=2)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += (self.velocity * dt)

