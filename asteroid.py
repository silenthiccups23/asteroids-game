import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
        pygame.draw.circle(screen, "white", self,position, self.radius, LINE_WIDTH)
        
