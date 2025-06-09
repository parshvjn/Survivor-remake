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

AUTOTILE_MAP_CITY_ROAD = {
    tuple([tuple(sorted([(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1)])),  tuple(sorted([(-1, -1), (-2, -1), (-2, -2), (-1, -2)]))]): 7, # corner road with curve top left
    tuple([tuple(sorted([(1, 0), (1,1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)])),  tuple(sorted([(1, -1), (1, -2), (2, -2), (2, -1)]))]): 6, # corner road with curve top right
    tuple([tuple(sorted([(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1)])),  tuple(sorted([(-1, 1), (-2, 1), (-2, 2), (-1, 2)]))]): 5, # corner road with curve bottom left
    tuple([tuple(sorted([(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0)])),  tuple(sorted([(1, 1), (2, 1), (2,2), (1, 2)]))]): 4, # corner road with curve bottom right
    tuple([tuple(sorted([(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)])),  tuple(sorted([(-2, -2), (2, -2), (-2, 2), (2, 2)]))]): 8, # intersection middle
    tuple([tuple(sorted([(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)])),  tuple(sorted([(-2, -2), (-1, -2), (-2, 2), (-1, 2)]))]): 11, # intersection mid left
    tuple([tuple(sorted([(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)])),  tuple(sorted([(2, -2), (1, -2), (1, 2), (2, 2)]))]): 11, # intersection mid right
    tuple([tuple(sorted([(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)])),  tuple(sorted([(-2, -2), (-2, -1), (2, -1), (2, -2)]))]): 2, # intersection mid up
    tuple([tuple(sorted([(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)])),  tuple(sorted([(-2, 2), (-2, 1), (2, 1), (2, 2)]))]): 2, # intersection mid down
    tuple([tuple(sorted([(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)])),  tuple(sorted([(-2, -2), (-1, -2), (0, -2), (1, -2), (-2, 2), (-1, 2), (0, 2), (1, 2)]))]): 1, # middle crosswalk next to right intersection
    tuple([tuple(sorted([(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)])),  tuple(sorted([(2, -2), (-1, -2), (0, -2), (1, -2), (2, 2), (-1, 2), (0, 2), (1, 2)]))]): 1, # middle crosswalk next to left intersection
    tuple([tuple(sorted([(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)])),  tuple(sorted([(-2, -2), (-2, -1), (-2, 0), (-2, 1), (2, -2), (2, -1), (2, 0), (2, 1)]))]): 14, # middle crosswalk next to up intersection
    tuple([tuple(sorted([(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)])),  tuple(sorted([(-2, 2), (-2, -1), (-2, 0), (-2, 1), (2, 2), (2, -1), (2, 0), (2, 1)]))]): 14, # middle crosswalk next to down intersection
    tuple([tuple(sorted([(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)])),  tuple(sorted([(-2, -2), (-2, 2), (2, -2), (-1, -2), (0, -2), (1, -2), (2, 2), (-1, 2), (0, 2), (1, 2)]))]): 11, # middle street horizontal
    tuple([tuple(sorted([(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)])),  tuple(sorted([(-2, -2), (-2, -1), (-2, 0), (-2, 1), (2, -2), (2, -1), (2, 0), (2, 1), (-2, 2), (2, 2)]))]): 2, # middle street vertical
    tuple([tuple(sorted([(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)])),  tuple(sorted([(-2, -2), (-1, -2), (0, -2), (-2, 2), (-1, 2), (0, 2)]))]): 11, # after mid left of intersection (right of crosswalk)
    tuple([tuple(sorted([(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)])),  tuple(sorted([(2, -2), (1, -2), (0, -2), (2, 2), (1, 2), (0, 2)]))]): 11, # after mid right of intersection (left of crosswalk)
    tuple([tuple(sorted([(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0)])),  tuple(sorted([(-1, -1), (0, -1), (1, -1), (-2, -1), (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2), (2, -1)]))]): 10, # up street horizontal
    tuple([tuple(sorted([(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0)])),  tuple(sorted([(-1, 1), (0, 1), (1, 1), (-2, 1), (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2), (2, 1)]))]): 12, # dpwn street horizontal
    tuple([tuple(sorted([(0, -1), (1, -1), (1, 0), (1, 1), (0, 1)])),  tuple(sorted([(-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2)]))]): 16, # left street vertical
    tuple([tuple(sorted([(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)])),  tuple(sorted([(2, -2), (2, -1), (2, 0), (2, 1), (2, 2), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2)]))]): 3, # right street vertical
    tuple([tuple(sorted([(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)])),  tuple(sorted([(-1, -1), (0, -1), (-2, -1), (-2, -2), (-1, -2), (0, -2)]))]): 10,
    tuple([tuple(sorted([(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)])),  tuple(sorted([(1, -1), (0, -1), (2, -1), (2, -2), (1, -2), (0, -2)]))]): 10,
    tuple([tuple(sorted([(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)])),  tuple(sorted([(-1, 1), (0, 1), (-2, 1), (-2, 2), (-1, 2), (0, 2)]))]): 12,
    tuple([tuple(sorted([(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)])),  tuple(sorted([(1, 1), (0, 1), (2, 1), (2, 2), (1, 2), (0, 2)]))]): 12,
    tuple([tuple(sorted([(0, -1), (1, -1), (1, 0), (1,1), (0, 1), (-1, 1)])),  tuple(sorted([(-1, 0), (-1, -1), (-2, 0), (-2, -1), (-2, -2), (-1, -2)]))]): 16,
    tuple([tuple(sorted([(0, 1), (1, 1), (1, 0), (1,-1), (0, -1), (-1, -1)])),  tuple(sorted([(-1, 0), (-1, 1), (-2, 0), (-2, 1), (-2, 2), (-1, 2)]))]): 16,
    tuple([tuple(sorted([(0, -1), (-1, -1), (-1, 0), (-1,1), (0, 1), (1, 1)])),  tuple(sorted([(1, 0), (1, -1), (2, 0), (2, -1), (2, -2), (1, -2)]))]): 3,
    tuple([tuple(sorted([(0, 1), (-1, 1), (-1, 0), (-1,-1), (0, -1), (1, -1)])),  tuple(sorted([(1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (1, 2)]))]): 3,
    tuple([tuple(sorted([(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0)])),  tuple(sorted([(-2, 1), (-2, 2), (-1, 1), (-1, 2), (0, 2), (0, 1), (1, 1), (1,2)]))]): 9,
    tuple([tuple(sorted([(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)])),  tuple(sorted([(2, 1), (2, 2), (1, 1), (1, 2), (0, 2), (0, 1), (-1, 1), (-1,2)]))]): 9,
    tuple([tuple(sorted([(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0)])),  tuple(sorted([(-1, -1), (0, -1), (1, -1), (2, -1), (-1, -2), (0, -2), (1, -2), (2, -2)]))]): 0,
    tuple([tuple(sorted([(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0)])),  tuple(sorted([(-2, -1), (-2, -2), (-1, -1), (-1, -2), (0, -2), (0, -1), (1, -1), (1,-2)]))]): 0,
    tuple([tuple(sorted([(0, -1), (1, -1), (1, 0), (1, 1), (0, 1)])),  tuple(sorted([(-2, -2), (-2, -1), (-2, 0), (-2, 1), (-1, -2), (-1, -1), (-1, 0), (-1, 1)]))]): 13,
    tuple([tuple(sorted([(0, 1), (1, 1), (1, 0), (1, -1), (0, -1)])),  tuple(sorted([(-2, 2), (-2, 1), (-2, 0), (-2, -1), (-1, 2), (-1, 1), (-1, 0), (-1, -1)]))]): 13,
    tuple([tuple(sorted([(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)])),  tuple(sorted([(2, -2), (2, -1), (2, 0), (2, 1), (1, -2), (1, -1), (1, 0), (1, 1)]))]): 15,
    tuple([tuple(sorted([(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)])),  tuple(sorted([(2, 2), (2, 1), (2, 0), (2, -1), (1, 2), (1, 1), (1, 0), (1, -1)]))]): 15,
    tuple([tuple(sorted([(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)])),  tuple(sorted([(-2, 0), (-2, 1), (-2, 2), (2, 2), (2, 1), (2, 0)]))]): 2,
    tuple([tuple(sorted([(1,0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)])),  tuple(sorted([(-2, 0), (-2, -1), (-2, -2) , (2, -2), (2, -1), (2, 0)]))]): 2,
}

# ! since u are doing the generation as the player moves maybe do random sizes of the squares
#! loading screen for while the tile loading occurs
# ! or make it so that everytime it goes outwards then produce more squares and roads and autotile it
#! fix the fact that when you are going diagonally top left or top right and click the other side arrow key it doesn't stop u for the x-axis
# ? the random generation without atuotiling of th ecity-road tiles looks cool too, could add that feature
 # ? maybe add texture to the grey squares as when screen covered by it seems odd

class TileMap:
    def __init__(self, game, tile_size):
        self.game = game
        self.tile_size = tile_size
        # self.map_data = {f'{x};{y}': {'type': 'ground/city','variant': random.randint(0, 8),'pos': [x, y]} for x, y in ((random.randint(-100, 100), random.randint(-100, 100)) for _ in range(0, 100000))}
        
        ### ! remove and change after autotile
        self.map_data = {}
        square_size = 20
        gap = 3
        num_squares = 10

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
        for x in range(-100, 100):
            for y in range(-100, 100):
                loc = f'{x};{y}'
                if loc not in self.map_data:
                    self.map_data[loc] = {
                        'type': 'ground/city-road',
                        # 'variant': random.randint(0, 16),
                        'variant': None,
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
            if tile['type'] != 'ground/city-road':
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
            else:
                neighborsCity = set()
                for shift in [(1,0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    check_loc = str(tile['pos'][0] + shift[0]) + ';' + str(tile['pos'][1] + shift[1])
                    if check_loc in self.map_data:
                        if self.map_data[check_loc]['type'] == tile['type']:
                            neighbors.add(shift)
                for shift in [
                    (1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1),
                    (2, 0), (-2, 0), (0, 2), (0, -2),
                    (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2),
                    (2, 2), (2, -2), (-2, 2), (-2, -2)]:
                    check_loc = str(tile['pos'][0] + shift[0]) + ';' + str(tile['pos'][1] + shift[1])
                    if check_loc in self.map_data:
                        if self.map_data[check_loc]['type'] == 'ground/city':
                            neighborsCity.add(shift)
                neighbors = tuple(sorted(neighbors))
                neighborsCity = tuple(sorted(neighborsCity))
                neighborsTotalCity = tuple([neighbors, neighborsCity])

                # print(neighborsTotalCity)
                if (neighborsTotalCity in AUTOTILE_MAP_CITY_ROAD):
                    tile['variant'] = AUTOTILE_MAP_CITY_ROAD[neighborsTotalCity]
    
    def render(self, surf, offset=(0, 0)):
        for x in range(offset[0] // self.tile_size, (offset[0]+ surf.get_width()) // self.tile_size + 1): 
                for y in range(offset[1] // self.tile_size, (offset[1]+ surf.get_height()) // self.tile_size + 1):
                    loc = str(x) + ';' + str(y) 
                    if loc in self.map_data:
                        tile = self.map_data[loc]
                        # print(tile)
                        surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))
                        
        
        # print(offset[0] // self.tile_size, (offset[0]+ surf.get_width()) // self.tile_size + 1)