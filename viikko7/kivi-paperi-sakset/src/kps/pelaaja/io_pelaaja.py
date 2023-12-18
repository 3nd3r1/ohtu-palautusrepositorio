from kps.pelaaja import Pelaaja

from kps.tuomari import Siirto


class IOPelaaja(Pelaaja):
    def __init__(self, nimi: str):
        self.nimi = nimi
        super().__init__()

    def hae_siirto(self):
        siirto_str = input(f"Pelaajan {self.nimi} siirto:")
        match siirto_str:
            case "k":
                return Siirto.KIVI
            case "p":
                return Siirto.PAPERI
            case "s":
                return Siirto.SAKSET
            case _:
                return None
