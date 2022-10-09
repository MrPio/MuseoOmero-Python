#######################################################
# 
# Biglietto.py
# Python implementation of the Class Biglietto
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
from datetime import datetime

from backend.high_level.clientela.documento import Documento
from backend.high_level.clientela.enum.tariffa import Tariffa
from backend.high_level.gestione_interna.enum.reparto_museo import RepartoMuseo
from backend.high_level.gestione_interna.turno_guida import TurnoGuida
from backend.high_level.personale.operatore_al_pubblico import OperatoreAlPubblico
from backend.low_level.pagamenti.nexi_api import NexiApi


class Biglietto(Documento):
    def __init__(self, dataRilascio: datetime = None, reparto: RepartoMuseo = RepartoMuseo.MUSEO_APERTO,
                 tariffa: Tariffa = Tariffa.INTERO, turno: TurnoGuida = None):
        super().__init__(NexiApi(), dataRilascio)
        self.reparto_museo = reparto
        self.tariffa = tariffa
        self.guida = turno

    def calcolaCosto(self) -> float:
        if self.reparto_museo == RepartoMuseo.MUSEO_APERTO:
            return 0.00
        else:
            return self.tariffa.cost + (5.00 if self.__hasGuida() else 0.00)

    def convalida(self) -> bool:
        self.date_convalida.append(datetime.now())
        return self.pagato and (datetime.now() - self.data_rilascio).total_seconds() < 3600 * 24

    def __hasGuida(self) -> bool:
        return self.guida is None
