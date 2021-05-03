import pygame
from pygame.sprite import Sprite

class Pocisk(Sprite):
    def __init__(self,gra):
        super().__init__()
        self.ekran = gra.screen
        self.ustawienia = gra.ustawienia
        self.kolor = self.ustawienia.pocisk_kolor


        self.prostokat = pygame.Rect(0,0, self.ustawienia.pocisk_szerokosc,
                                     self.ustawienia.pocisk_dlugosc)
        self.prostokat.midbottom = gra.ship.rect.midtop

        self.y = float( self.prostokat.y)

    def update(self):
        self.y -= self.ustawienia.pocisk_szybkosc
        self.prostokat.y = self.y

    def draw_pocisk(self):
        pygame.draw.rect(self.ekran, self.kolor, self.prostokat)