#######################################################
# 
# ControllerAggiungiOpera.py
# Python implementation of the Class ControllerAggiungiOpera
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.gestione_interna.opera import Opera
from backend.high_level.personale.richiesta_donazione import RichiestaDonazione
from frontend.controller.controller import Controller
from frontend.controller.reception.strategy_aggiungi_opera.strategy_aggiungi_opera import StrategyAggiungiOpera
from frontend.view.reception.vista_aggiungi_opera import VistaAggiungiOpera


class ControllerAggiungiOpera(Controller):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.enableView()

    def __init__(self, view: VistaAggiungiOpera, previous: Controller,model:Opera, strategy: StrategyAggiungiOpera):
        super().__init__(view)
        self.view: VistaAggiungiOpera = view
        self.previous = previous
        self.model = model
        self.strategy: StrategyAggiungiOpera = strategy

    def __onAggiungiUbicazioneClicked(self) -> None:
        pass

    def __onDropZoneDropped(self) -> None:
        pass

    def __onDropZoneClicked(self) -> None:
        pass

    def __onConfermaClicked(self) -> None:
        # self.strategy.onConfermaClicked()
        pass

    def connettiEventi(self) -> None:
        pass

    def getRichiestaDonazione(self) -> RichiestaDonazione:
        pass

    def getOpera(self) -> Opera:
        pass
