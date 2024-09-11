import pygame
import random
from constants import *
from circleshape import CircleShape

white = (255, 255, 255)


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        if hasattr(self, 'containers'):
            self.add(self.containers)
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, white, self.position, self.radius, width=2)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(-180, 180)
        new_v1 = self.velocity.rotate(angle)
        new_v2 = self.velocity.rotate(-angle)
        new_v1 *= 1.2
        new_v2 *= 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child_1 = Asteroid(self.position.x, self.position.y, new_radius)
        child_2 = Asteroid(self.position.x, self.position.y, new_radius)
        child_1.velocity = new_v1
        child_2.velocity = new_v2
        child_1.add(self.containers)
        child_2.add(self.containers)

        
