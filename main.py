import pygame
import particle
import random


class Game:
    def __init__(self) -> None:
        self.width = 800
        self.height = 1200

        pygame.init()  
        pygame.display.set_caption('Particle Simulation')
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.particles : list = []
    
    def main(self):
        running = True
        while running:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if len(self.particles) < 10:
                self.particles.append(particle((random.randint(0, self.width), random.randint(0, self.height)), 25, "red"))

            for particle in self.particles:
                particle.draw()

            pygame.display.flip()

game = Game()
game.main()