from kps.pelaaja import Pelaaja

from kps.tuomari import Siirto


class TekoalyPelaaja(Pelaaja):
    def __init__(self):
        self._siirto = 0

    def _selvita_siirto(self):
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

        if self._siirto == 0:
            return Siirto.KIVI
        if self._siirto == 1:
            return Siirto.PAPERI
        return Siirto.SAKSET

    def hae_siirto(self):
        siirto = self._selvita_siirto()
        print(f"Tietokone valitsi: {str(siirto)}")
        return siirto
