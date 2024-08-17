import pygame
import random
from particle import Particle

class Game:
    def __init__(self) -> None:
        self.width = 1200
        self.height = 800
        pygame.init()  
        pygame.display.set_caption('Particle Simulation')
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.particles : list[Particle] = []
    
    def main(self):
        running = True
        while running:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if len(self.particles) < 10:
                self.particles.append(Particle((random.randint(0, self.width), random.randint(0, self.height)), 
                                               25, "red", self.screen, True, 15))

            for particle in self.particles:
                particle.draw()
            
            for i in range(len(self.particles)):
                for j in range(len(self.particles)):
                    self.particles[i].update(self.particles[j])

            pygame.display.flip()

game = Game()
game.main()