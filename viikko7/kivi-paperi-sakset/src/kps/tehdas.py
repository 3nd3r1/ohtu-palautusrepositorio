from enum import Enum

from kps.kivi_paperi_sakset import KiviPaperiSakset
from kps.pelaaja import IOPelaaja, TekoalyPelaaja, ParempiTekoalyPelaaja


class PeliTyyppi(Enum):
    PELAAJA_VS_PELAAJA = 1
    PELAAJA_VS_TEKOALY = 2
    PELAAJA_VS_PAREMPI_TEKOALY = 3


def luo_peli(tyyppi: PeliTyyppi) -> KiviPaperiSakset:
    match tyyppi:
        case PeliTyyppi.PELAAJA_VS_PELAAJA:
            return KiviPaperiSakset(IOPelaaja("1"), IOPelaaja("2"))
        case PeliTyyppi.PELAAJA_VS_TEKOALY:
            return KiviPaperiSakset(IOPelaaja("1"), TekoalyPelaaja())
        case PeliTyyppi.PELAAJA_VS_PAREMPI_TEKOALY:
            return KiviPaperiSakset(IOPelaaja("1"), ParempiTekoalyPelaaja(10))
