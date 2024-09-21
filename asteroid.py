from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random
import pygame


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector_a = self.velocity.rotate(random_angle) * 1.2
        vector_b = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_obj_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_obj_a.velocity = vector_a * 1.2
        asteroid_obj_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_obj_b.velocity = vector_b * 1.2
