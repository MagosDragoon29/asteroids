import pygame
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