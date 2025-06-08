import pygame, random

class TileMap:
    def __init__(self, tile_size):
        self.tile_size = tile_size
        # self.map_data = {f'{random.randint(-100, 100)};{random.randint(-100, 100)}':100 for x in range(0, 1000)}
        self.map_data = {f'{random.randint(-100, 100)};{random.randint(-100, 100)}':100 for x in range(0, 100000)}
        self.offgrid_data  = []
        # {"9;12": {"type": "grass", "variant": 2, "pos": [9, 12]}
    
    def render(self, surf, offset=(0, 0)):
        for x in range(offset[0] // self.tile_size, (offset[0]+ surf.get_width()) // self.tile_size + 1): 
                for y in range(offset[1] // self.tile_size, (offset[1]+ surf.get_height()) // self.tile_size + 1):
                    loc = str(x) + ';' + str(y) 
                    if loc in self.map_data:
                        # tile = self.map_data[loc]
                        pygame.draw.rect(surf, (93, 93, 93), (x * self.tile_size - offset[0], y * self.tile_size - offset[1], self.tile_size, self.tile_size))
        
        print(offset[0] // self.tile_size, (offset[0]+ surf.get_width()) // self.tile_size + 1)