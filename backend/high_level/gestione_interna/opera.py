#######################################################
# 
# Opera.py
# Python implementation of the Class Opera
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
from PIL.Image import Image

from backend.high_level.gestione_interna.composizione import Composizione
from backend.high_level.gestione_interna.enum.periodo_storico import PeriodoStorico
from backend.high_level.gestione_interna.enum.reparto_museo import RepartoMuseo
from backend.high_level.gestione_interna.ubicazione import Ubicazione
from backend.low_level.pagamenti.pagamento import Pagamento


class Opera:

    def __init__(self, autore: str, titolo: str,
                 descrizione: str, immagine: Image, periodo: PeriodoStorico,
                 reparto: RepartoMuseo, costo: float = 0, composizione: Composizione = None,
                 ubicazione: Ubicazione = None):
        self.autore = autore
        self.titolo = titolo
        self.descrizione = descrizione
        self.immagine = immagine
        self.periodo = periodo
        self.reparto = reparto
        self.costo = costo
        self.composizione = composizione
        self.ubicazione = ubicazione
        self.venduta=False

    def vendi(self, pagamento: Pagamento) -> bool:
        if not self.isVendibile():
            return False
        return pagamento.paga(costo=self.costo)

    def isVendibile(self):
        return self.reparto == RepartoMuseo.MOSTRA
