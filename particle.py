import pygame


class Particle:
    def __init__(self, pos, radius, color, screen, vision, gravity = False, gravity_strength = 0) -> None:
        self.pos : pygame.Vector2 = pos
        self.radius : int = radius
        self.color : str | int  = color
        self.gravity: bool = gravity
        self.gravity_strength : int = gravity_strength
        self.screen : pygame.display= screen
        self.acceleration = 0.01
        self.velocity_y = 1
        self.velocity = pygame.Vector2(0, 0)
        self.vision = vision
    

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)

    def update(self, other, dt):
        self.pos += self.velocity * dt

        if self.gravity:
            if self.pos.y < self.screen.get_height():
                self.pos.y += self.gravity_strength * dt * self.velocity_y
                self.velocity_y += self.acceleration
            else:
                self.velocity_y = 0
        
        if self.pos.distance_to(other.pos) < self.vision:
            pass
            
        
