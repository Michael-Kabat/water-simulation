import pygame

class Particle:
    def __init__(self, pos, radius, color) -> None:
        self.pos = pos
        self.radius = radius
        self.color = color
    

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
