from circleshape import CircleShape
from constants import SHOOT_RADIUS, SHOOT_SPEED
import pygame

class Shoot(CircleShape):
    print("shoot!")
    def __init__(self, x, y, rotation, radius=None):
        super().__init__(x, y, radius=radius)
        self.radius = SHOOT_RADIUS
        self.rotation = rotation
        self.forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity = self.forward * SHOOT_SPEED

        

    def draw(self,screen):
       pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self,dt):
        self.position += self.velocity * dt

        
        
