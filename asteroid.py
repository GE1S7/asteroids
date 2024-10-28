from circleshape import *
from constants import PLAYER_SPEED, ASTEROID_MIN_RADIUS 
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self,screen):
       
       pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 17
        else:
            angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
