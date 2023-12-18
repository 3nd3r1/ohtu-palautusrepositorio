from kps.tuomari import Tuomari
from kps.pelaaja import Pelaaja


class KiviPaperiSakset:
    def __init__(self, pelaaja1: Pelaaja, pelaaja2: Pelaaja):
        self._pelaaja1 = pelaaja1
        self._pelaaja2 = pelaaja2

    def pelaa(self):
        tuomari = Tuomari()

        while True:
            print()
            ekan_siirto = self._pelaaja1.hae_siirto()
            tokan_siirto = self._pelaaja2.hae_siirto()

            if not ekan_siirto or not tokan_siirto:
                break

            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            self._pelaaja1.muista_edellinen_siirto(tokan_siirto)
            self._pelaaja2.muista_edellinen_siirto(ekan_siirto)

        print()
        print("Kiitos!")
        print(tuomari)
        print()
