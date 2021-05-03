import sys
import pygame

from ustawinia import Ustawienia
from statek import Statek
from pocisk import Pocisk

class InwazjaObcych():
    def __init__(self):
        pygame.init()
        self.ustawienia = Ustawienia()
        self.screen=pygame.display.set_mode((self.ustawienia.screen_szerokosc,self.ustawienia.screen_wysokosc))
        pygame.display.set_caption("Inwazja ziemianiee")
        self.ship = Statek(self)
        self.pociski = pygame.sprite.Group()

    def rusz_gre(self):
        while True:
            self.zdarzenia()
            self.ship.aktualizacja()
            self.aktualizacja_poxiskow()
            self.aktualizacja()

    def zdarzenia(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.sprawdz_klawisz_dol(event)
            elif event.type == pygame.KEYUP:
                self.sprawdz_klawisz_gora(event)

    def sprawdz_klawisz_dol(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.w_ruchu_prawo = True
        elif event.key == pygame.K_LEFT:
            self.ship.w_ruchu_lewo = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def sprawdz_klawisz_gora(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.w_ruchu_prawo = False
        elif event.key == pygame.K_LEFT:
            self.ship.w_ruchu_lewo = False
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def aktualizacja_poxiskow(self):
        self.pociski.update()
        for pocisk in self.pociski.copy():
            if pocisk.prostokat.bottom <= 0:
                self.pociski.remove(pocisk)

    def _fire_bullet(self):
        if len(self.pociski) < self.ustawienia.ilosc_pociskow:
            new_pocisk = Pocisk(self)
            self.pociski.add(new_pocisk)

    def aktualizacja(self):
        # wpisanie koloru tła
        self.screen.fill(self.ustawienia.kolor_tla)
        self.ship.pokaz_mnie()
        for pocisk in self.pociski.sprites():
            pocisk.draw_pocisk()

        pygame.display.flip()


if(__name__ == '__main__'):
    inw = InwazjaObcych()
    inw.rusz_gre()