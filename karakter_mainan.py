import pygame
from abc import ABC, abstractmethod
from gambar_mainan import *

class Karakter(ABC):
    playerx = 100
    
    @abstractmethod
    def update(self, user_input):
        pass

class Ptero(Karakter):
    def __init__(self):
        self.x = 100
        self.y = 936 // 2
        self.image = Gambar_Ptero[0]
        self.rect = self.image.get_rect()
        self.ptero_rect = self.rect
        self.ptero_rect.center = [self.x, self.y]
        # tambahin animasi wing flapping 
        self.vel = 0
        self.terbangg = False  
        self.flap = True
        self.ptero_flapping = Gambar_Ptero
        self.index = 0

    def terbang(self):
        if self.terbangg == True:
            self.vel = -15
            self.terbangg = False

    def bergerak(self):
        if self.flap == True:
            self.image = self.ptero_flapping[self.index % 8]
            self.index += 1

    def update(self, user_input):
        if self.index > 5:
            self.index = 0
        # gravity
        if self.flap is True:
            self.bergerak()
            self.vel += 4
        if self.vel > 12:
            self.vel = 12
        if self.rect.bottom < 936:
            self.rect.y += self.vel
        if self.rect.top < 0:
            self.rect.top = 0 
        # jump
        if self.terbangg is False and user_input[pygame.K_SPACE]:
            self.terbangg = True
            self.terbang()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
