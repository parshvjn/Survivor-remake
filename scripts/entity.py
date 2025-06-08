import pygame

class PhsyicsEntity:
    def __init__(self, eType, pos, size, speed = 1):
        self.type = eType
        self.pos = list(pos)
        self.size = size
        self.vel = [0, 0]
        self.speed = speed
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def update(self, movement = (0, 0)):
        f_move = ((movement[0]*self.speed) + self.vel[0], (movement[1]*self.speed) + self.vel[1])
        self.pos[0] += f_move[0]
        self.pos[1] += f_move[1]

    def render(self, surf, offset=(0, 0)):
        pygame.draw.rect(surf, (255,255,255), (self.pos[0] - offset[0], self.pos[1] - offset[1], self.size[0], self.size[1]))

class Player(PhsyicsEntity):
    def __init__(self, pos, size):
        super().__init__("player", pos, size, speed=5)
    
    def udpate(self, movement = (0, 0)):
        super().update(movement)
    
    def render(self, surf, offset=(0, 0)):
        super().render(surf, offset=offset)