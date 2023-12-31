from kps.pelaaja import Pelaaja

from kps.tuomari import Siirto


class ParempiTekoalyPelaaja(Pelaaja):
    def __init__(self, muistin_koko):
        self._muisti = [None] * muistin_koko
        self._vapaa_muisti_indeksi = 0

    def _selvita_siirto(self):
        if self._vapaa_muisti_indeksi in (0, 1):
            return Siirto.KIVI

        viimeisin_siirto = self._muisti[self._vapaa_muisti_indeksi - 1]

        k = 0
        p = 0
        s = 0

        for i in range(0, self._vapaa_muisti_indeksi - 1):
            if viimeisin_siirto == self._muisti[i]:
                seuraava = self._muisti[i + 1]

                if seuraava == Siirto.KIVI:
                    k = k + 1
                elif seuraava == Siirto.PAPERI:
                    p = p + 1
                else:
                    s = s + 1

        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        if k > p or k > s:
            return Siirto.PAPERI
        if p > k or p > s:
            return Siirto.SAKSET
        return Siirto.KIVI

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!

    def hae_siirto(self):
        siirto = self._selvita_siirto()
        print(f"Tietokone valitsi: {str(siirto)}")
        return siirto

    def muista_edellinen_siirto(self, siirto):
        # jos muisti täyttyy, unohdetaan viimeinen alkio
        if self._vapaa_muisti_indeksi == len(self._muisti):
            for i in range(1, len(self._muisti)):
                self._muisti[i - 1] = self._muisti[i]

            self._vapaa_muisti_indeksi = self._vapaa_muisti_indeksi - 1

        self._muisti[self._vapaa_muisti_indeksi] = siirto
        self._vapaa_muisti_indeksi = self._vapaa_muisti_indeksi + 1
