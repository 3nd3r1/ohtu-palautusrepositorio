from abc import ABC, abstractmethod

from kps.tuomari import Siirto


class Pelaaja(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def hae_siirto(self) -> Siirto | None:
        pass

    def muista_edellinen_siirto(self, siirto: Siirto):
        pass
