from enum import Enum


class Siirto(Enum):
    KIVI = 0
    PAPERI = 1
    SAKSET = 2

    def __str__(self):
        match self:
            case Siirto.KIVI:
                return "kivi"
            case Siirto.PAPERI:
                return "paperi"
            case Siirto.SAKSET:
                return "sakset"

# Luokka pitää kirjaa ensimmäisen ja toisen pelaajan pisteistä sekä tasapelien määrästä.


class Tuomari:
    def __init__(self):
        self.ekan_pisteet = 0
        self.tokan_pisteet = 0
        self.tasapelit = 0

    def kirjaa_siirto(self, ekan_siirto: Siirto, tokan_siirto: Siirto):
        if self._tasapeli(ekan_siirto, tokan_siirto):
            self.tasapelit = self.tasapelit + 1
        elif self._eka_voittaa(ekan_siirto, tokan_siirto):
            self.ekan_pisteet = self.ekan_pisteet + 1
        else:
            self.tokan_pisteet = self.tokan_pisteet + 1

    def __str__(self):
        return (f"Pelitilanne: "
                f"{self.ekan_pisteet} - {self.tokan_pisteet}\n"
                f"Tasapelit: {self.tasapelit}")

    # sisäinen metodi, jolla tarkastetaan tuliko tasapeli
    def _tasapeli(self, eka, toka):
        if eka == toka:
            return True

        return False

    # sisäinen metodi joka tarkastaa voittaako eka pelaaja tokan
    def _eka_voittaa(self, eka, toka):
        if eka == Siirto.KIVI and toka == Siirto.SAKSET:
            return True
        if eka == Siirto.PAPERI and toka == Siirto.KIVI:
            return True
        if eka == Siirto.SAKSET and toka == Siirto.PAPERI:
            return True

        return False
