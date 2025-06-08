import pygame, sys
from consts import *
from scripts.entity import *

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINW, WINH))
        pygame.display.set_caption("Survivor.io Remake")
        self.clock = pygame.time.Clock()
        self.running = True

        #player
        self.movement = [False, False, False, False]
        self.player = Player((100, 100), (50, 50))

        #camera
        self.scroll = [0, 0]
        
        #game loop
        self.main()
    
    def main(self):
        while self.running:
            self.window.fill((0, 0, 0))

            #camera
            self.scroll[0] += (self.player.rect().centerx - self.window.get_width() / 2 - self.scroll[0])/30
            self.scroll[1] += (self.player.rect().centery - self.window.get_height() / 2 - self.scroll[1])/30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            #player
            self.player.update((self.movement[1]-self.movement[0], self.movement[3]-self.movement[2]))
            self.player.render(self.window, offset=render_scroll)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.movement[2] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = True
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pygame.K_UP:
                        self.movement[2] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = False
            
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    Game()