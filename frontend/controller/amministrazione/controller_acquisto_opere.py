#######################################################
# 
# ControllerAcquistoOpere.py
# Python implementation of the Class ControllerAcquistoOpere
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.museo import Museo
from frontend.controller.controller import Controller
from frontend.controller.reception.controller_aggiungi_opera import ControllerAggiungiOpera
from frontend.controller.reception.controller_ricerca_opera import ControllerRicercaOpera
from frontend.controller.reception.strategy_aggiungi_opera.strategy_aggiungi_opera import StrategyAggiungiOpera
from frontend.controller.reception.strategy_ricerca_opera.strategy_ricerca_opera import StrategyRicercaOpera
from frontend.view.amministrazione.vista_acquisto_opere import VistaAcquistoOpere
from frontend.view.amministrazione.vista_gestione_mostre import VistaGestioneMostre
from frontend.view.reception.vista_aggiungi_opera import VistaAggiungiOpera
from frontend.view.reception.vista_ricerca_opera import VistaRicercaOpera


class ControllerAcquistoOpere(Controller):

    def __gotoPrevious(self) -> None:
        pass

    def __init__(self,view : VistaGestioneMostre, previous : Controller, model : Museo):
        pass

    def __gotoVistaAggiungiOpera(self) -> None:
        pass

    def __gotoVistaRicercaOpera(self) -> None:
        pass

    def connettiEventi(self) -> None:
        pass