import pygame

class Particle:
    def __init__(self, pos, radius, color, screen, gravity = False, gravity_strength = 0) -> None:
        self.pos : pygame.Vector2 = pygame.Vector2(pos[0], pos[1])
        self.radius : int = radius
        self.color : str | int  = color
        self.gravity: bool = gravity
        self.gravity_strength : int = gravity_strength
        self.screen : pygame.display= screen
    

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)

    def update(self, other):
        if self.gravity:
            if self.pos.y > self.screen.get_surface().get_height():
                self.pos[1] -= self.gravity_strength
        
