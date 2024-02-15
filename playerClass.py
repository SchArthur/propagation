import pygame

class Player:

    def __init__(self, position : list, color : pygame.color, screen : pygame.display, speed : int, keys : dict):
        self.p = pygame.Vector2(position[0], position[1])
        self.c = color
        self.s = screen
        self.sp = speed
        self.k = keys
        self.dt = 1000

    def draw(self, tilesize):
        pygame.draw.rect(self.s, self.c, (self.p.y*tilesize, self.p.x*tilesize, tilesize, tilesize))

    def getKeys(self):
        self.k = self.keyboard.get()
        self.doMovement()

    def doMovement(self):
        if self.dt >= 1000/self.sp and (self.k["vertical"][0] != 0 or self.k["horizontal"][0] != 0):
            self.dt = 0
            self.p.x += self.k["vertical"][0]
            self.p.y += self.k["horizontal"][0]
        
    