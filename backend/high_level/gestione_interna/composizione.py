#######################################################
# 
# Composizione.py
# Python implementation of the Class Composizione
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
import TipoOpera

class Composizione:
    def __init__(self, altezzaCm: float, larghezzaCm: float,
                 profonditaCm: float, pesoGr: float, tipo: TipoOpera):
        self.tipo_opera = tipo
        self.altezza_cm = altezzaCm
        self.larghezza_cm = larghezzaCm
        self.profondita_cm = profonditaCm
        self.peso_gr = pesoGr

    def calcolaArea(self) -> float:
        pass

    def calcolaVolume(self) -> float:
        """
        Metodo per il calcolo del volume dell'opera.\n
        :return: il valore <b2>float</b2> del volume.
        """
        return self.calcolaArea() * self.profondita_cm


