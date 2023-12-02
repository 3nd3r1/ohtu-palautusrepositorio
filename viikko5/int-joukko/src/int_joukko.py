OLETUS_KAPASITEETTI = 5
OLETUS_KASVATUS = 5


class VirheellinenKapasiteetti(Exception):
    """ Virheellinen kapasiteetti """


class VirheellinenKasvatuskoko(Exception):
    """ Virheellinen kasvatuskoko """


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = OLETUS_KAPASITEETTI
        elif isinstance(kapasiteetti, int) and kapasiteetti >= 0:
            self.kapasiteetti = kapasiteetti
        else:
            raise VirheellinenKapasiteetti("Virheellinen kapasiteetti")

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUS_KASVATUS
        elif isinstance(kasvatuskoko, int) and kasvatuskoko >= 0:
            self.kasvatuskoko = kasvatuskoko
        else:
            raise VirheellinenKasvatuskoko("Virheellinen kasvatuskoko")

        self._lista = self._luo_lista(self.kapasiteetti)
        self._alkioiden_lukumaara = 0

    def _kasvata(self):
        vanha_lista = self._lista

        self.kapasiteetti += self.kasvatuskoko
        self._lista = self._luo_lista(self.kapasiteetti)

        self._kopioi_lista(vanha_lista, self._lista)

    def _kopioi_lista(self, lista_a, lista_b):
        for index in range(0, len(lista_a)):
            lista_b[index] = lista_a[index]

    def _siirra_vasemmalle(self, index):
        while index < self._alkioiden_lukumaara:
            self._lista[index] = self._lista[index + 1]
            index += 1

    def kuuluu(self, alkio):
        for index in range(0, self._alkioiden_lukumaara):
            if alkio == self._lista[index]:
                return True

        return False

    def lisaa(self, alkio):
        if not self.kuuluu(alkio):
            self._lista[self._alkioiden_lukumaara] = alkio
            self._alkioiden_lukumaara += 1

            if self._alkioiden_lukumaara == self.kapasiteetti:
                self._kasvata()

            return True
        return False

    def poista(self, alkio):
        if self.kuuluu(alkio):
            for index in range(0, self._alkioiden_lukumaara):
                if alkio == self._lista[index]:
                    self._lista[index] = 0
                    self._siirra_vasemmalle(index)
                    self._alkioiden_lukumaara -= 1
                    return True

        return False

    def mahtavuus(self):
        return self._alkioiden_lukumaara

    def to_int_list(self):
        taulu = self._luo_lista(self._alkioiden_lukumaara)

        for index in range(0, len(taulu)):
            taulu[index] = self._lista[index]

        return taulu

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        yhdiste = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()

        for index in range(0, len(a_taulu)):
            yhdiste.lisaa(a_taulu[index])

        for index in range(0, len(b_taulu)):
            yhdiste.lisaa(b_taulu[index])

        return yhdiste

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        leikkaus = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()

        for index_a in range(0, len(a_taulu)):
            for index_b in range(0, len(b_taulu)):
                if a_taulu[index_a] == b_taulu[index_b]:
                    leikkaus.lisaa(b_taulu[index_b])

        return leikkaus

    @staticmethod
    def erotus(joukko_a, joukko_b):
        erotus = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()

        for index in range(0, len(a_taulu)):
            erotus.lisaa(a_taulu[index])

        for index in range(0, len(b_taulu)):
            erotus.poista(b_taulu[index])

        return erotus

    def __str__(self):
        return "{"+', '.join([str(alkio) for alkio in self.to_int_list()])+"}"
