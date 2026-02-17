import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape): 
    def __init__ (self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return 
        else:
            log_event("asteroid_split")
        random_angle1 = random.uniform(20, 50)
        random_angle2 = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(random_angle1)
        new_velocity_2 = self.velocity.rotate(random_angle2)
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = pygame.Vector2(new_velocity_1)*1.2
        new_asteroid_2.velocity = pygame.Vector2(new_velocity_2)*1.2



    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity*dt #Moves at constant speed ini a straight line

    