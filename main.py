import pygame
import random
from particle import Particle

class Game:
    def __init__(self) -> None:
        self.width = 1280
        self.height = 720
        pygame.init()  
        pygame.display.set_caption('Particle Simulation')
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.particles : list[Particle] = []
        self.clock = pygame.time.Clock()
    
    def main(self):
        dt = 60 / 1000
        running = True
        while running:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill("black")

            if len(self.particles) < 10:
                self.particles.append(Particle(pygame.Vector2(random.randint(0, self.width), random.randint(0, self.height)), 
                                               25, "red", self.screen, 100, True, 10))

            for particle in self.particles:
                particle.draw()
                
            
            for i in range(len(self.particles)):
                for j in range(len(self.particles)):
                    self.particles[i].update(self.particles[j], dt)


            dt = self.clock.tick(60) / 1000
            pygame.display.flip()


game = Game()
game.main()