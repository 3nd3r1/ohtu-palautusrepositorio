
from kps.tehdas import luo_peli, PeliTyyppi


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        peli = None

        match vastaus:
            case "a":
                peli = luo_peli(PeliTyyppi.PELAAJA_VS_PELAAJA)
            case "b":
                peli = luo_peli(PeliTyyppi.PELAAJA_VS_TEKOALY)
            case "c":
                peli = luo_peli(PeliTyyppi.PELAAJA_VS_PAREMPI_TEKOALY)
            case _:
                break

        if peli:
            peli.pelaa()


if __name__ == "__main__":
    main()
