import pygame, random

AUTOTILE_TYPES = {'ground/city'}
AUTOTILE_MAP = {
    tuple(sorted([(0, 1), (1, 0), (1,1)])): 0,
    tuple(sorted([(0, 1), (1, 0), (1,1), (-1, 0), (-1, 1)])): 1,
    tuple(sorted([(-1, 0), (-1, 1), (0, 1)])): 2,
    tuple(sorted([(0, -1), (1, -1), (1, 0), (1, 1), (0, 1)])): 3,
    tuple(sorted([(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (-1, 1)])): 4,
    tuple(sorted([(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)])): 5,
    tuple(sorted([(0, -1), (1, -1), (1, 0)])): 6,
    tuple(sorted([(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0)])): 7,
    tuple(sorted([(-1, 0), (-1, -1), (0, -1)])): 8
}

#! loading screen for while the tile loading occurs

class TileMap:
    def __init__(self, game, tile_size):
        self.game = game
        self.tile_size = tile_size
        # self.map_data = {f'{x};{y}': {'type': 'ground/city','variant': random.randint(0, 8),'pos': [x, y]} for x, y in ((random.randint(-100, 100), random.randint(-100, 100)) for _ in range(0, 100000))}
        
        ### ! remove and change after autotile
        self.map_data = {}
        square_size = 20  # 3x3 tiles per square
        gap = 4         # 1 tile gap between squares
        num_squares = 10  # number of big squares in each direction

        for sx in range(-num_squares, num_squares):
            for sy in range(-num_squares, num_squares):
                base_x = sx * (square_size + gap)
                base_y = sy * (square_size + gap)
                for dx in range(square_size):
                    for dy in range(square_size):
                        x = base_x + dx
                        y = base_y + dy
                        loc = f'{x};{y}'
                        self.map_data[loc] = {
                            'type': 'ground/city',
                            'variant': random.randint(0, 8),
                            'pos': [x, y]
                        }
        ### !
        self.autotile()

        self.offgrid_data  = []
        # {"9;12": {"type": "grass", "variant": 2, "pos": [9, 12]}
    
    def autotile(self):
        for loc in self.map_data:
            tile = self.map_data[loc]
            neighbors = set()
            for shift in [(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                check_loc = str(tile['pos'][0] + shift[0]) + ';' + str(tile['pos'][1] + shift[1])
                if check_loc in self.map_data:
                    if self.map_data[check_loc]['type'] == tile['type']:
                        neighbors.add(shift)
            neighbors = tuple(sorted(neighbors))
            # print(neighbors)
            if (tile['type'] in AUTOTILE_TYPES and (neighbors in AUTOTILE_MAP)):
                tile['variant'] = AUTOTILE_MAP[neighbors]
                # print(tile)
    
    def render(self, surf, offset=(0, 0)):
        for x in range(offset[0] // self.tile_size, (offset[0]+ surf.get_width()) // self.tile_size + 1): 
                for y in range(offset[1] // self.tile_size, (offset[1]+ surf.get_height()) // self.tile_size + 1):
                    loc = str(x) + ';' + str(y) 
                    if loc in self.map_data:
                        tile = self.map_data[loc]
                        # print(tile)
                        surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))
                        
        
        # print(offset[0] // self.tile_size, (offset[0]+ surf.get_width()) // self.tile_size + 1)