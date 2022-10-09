#######################################################
# 
# Amministrazione.py
# Python implementation of the Class Amministrazione
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
import random

from backend.high_level.personale.amministratore import Amministratore
from backend.high_level.personale.dipendente import Dipendente
from backend.high_level.personale.posto_lavoro import PostoLavoro


class Amministrazione(PostoLavoro):

    def __init__(self, piano: int, numPostazioni: int, descrizione: str = ""):
        super().__init__(piano, numPostazioni, descrizione)

    def assumi(self, dipendente: Dipendente) -> bool:
        lavoro = Amministratore(
            contratto='contratto a tempo indeterminato',
            stipendio=max(800.0, random.gauss(2400, 200)),
            numPostazione=len(self.lavori) + 1,
            fondatore=False
        )
        if esito := dipendente.assumi(lavoro=lavoro):
            self.lavori.append(lavoro)
        return esito