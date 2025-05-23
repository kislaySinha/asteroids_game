from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        if(self.radius <= ASTEROID_MIN_RADIUS):
            self.kill()
        else:
            
            angle= random.uniform(20,50)
            vector1=self.velocity.rotate(angle)
            vector2=self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            mini_asteroid1 = Asteroid(self.position.x, self.position.y,new_radius)
            mini_asteroid2 = Asteroid(self.position.x, self.position.y,new_radius)
            mini_asteroid1.velocity = vector1 * 1.2
            mini_asteroid2.velocity = vector2 * 1.2
            self.kill()
