import pygame, sys
from consts import *

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINW, WINH))
        pygame.display.set_caption("Survivor.io Remake")
        self.clock = pygame.time.Clock()
        self.running = True
        self.main()
    
    def main(self):
        while self.running:
            self.window.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
            
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    Game()