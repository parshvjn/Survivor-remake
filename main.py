import pygame, sys
from consts import *
from scripts.entity import *
from scripts.utils import *
from scripts.tilemap import TileMap

# TODO: add resolution options (using pygame Surface); additionally use pygame Surface properties to add visual effects
# ? maybe add the trees/etc as offgrid data too using the y-sort camera for them
# ** credit Kenney for the tileset(assets)

class Game:
    def __init__(self):
        pygame.init()

        #window
        self.screen = pygame.display.set_mode((WINW, WINH))
        self.window = pygame.Surface((1280, 720))
        # self.window = pygame.Surface((WINW, WINH))
        pygame.display.set_caption("Survivor.io Remake")

        # run-vars
        self.clock = pygame.time.Clock()
        self.running = True

        #player
        self.movement = [False, False, False, False]
        self.player = Player((100, 100), (32, 50))

        #camera
        self.scroll = [0, 0]

        # images
        self.assets = {
            'ground/city': load_images('ground/city', scaleFactor=3),
            'ground/city-road': load_images('ground/city-road', scaleFactor=3)
        }

        #tilemap
        self.tilemap = TileMap(self, 48)
        
        #game loop
        self.main()
    
    def main(self):
        while self.running:
            self.window.fill((0, 0, 0))

            #camera
            self.scroll[0] += (self.player.rect().centerx - self.window.get_width() / 2 - self.scroll[0])/30
            self.scroll[1] += (self.player.rect().centery - self.window.get_height() / 2 - self.scroll[1])/30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            #tilemap
            self.tilemap.render(self.window, offset=render_scroll)

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
            

            self.screen.blit(pygame.transform.scale(self.window, (WINW, WINH)), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    Game()