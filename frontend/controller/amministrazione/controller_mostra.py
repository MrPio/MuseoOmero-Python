#######################################################
# 
# ControllerMostra.py
# Python implementation of the Class ControllerMostra
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.gestione_interna.mostra import Mostra
from backend.high_level.gestione_interna.opera import Opera
from frontend.controller.controller import Controller
from frontend.controller.reception.controller_vista_opera import ControllerVistaOpera
from frontend.view.amministrazione.vista_mostra import VistaMostra
from frontend.view.reception.vista_opera import VistaOpera


class ControllerMostra(Controller):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.initializeUi()
        self.previous.enableView()

    def __init__(self, view: VistaMostra, previous: Controller, model: Mostra):
        super().__init__(view)
        self.view: VistaMostra = view
        self.previous = previous
        self.model = model
        self.initializeUi()
        self.connettiEventi()

    def __gotoVistaOpera(self) -> None:
        self.next = ControllerVistaOpera(
            view=VistaOpera(),
            previous=self,
            model=Opera()
        )
        self.next.connettiEventi()
        self.next.showView()
        self.disableView()

    def connettiEventi(self) -> None:
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()

    def initializeUi(self) -> None:
        self.view.getPeriodoStoricoLabel().setText(self.model.tema.name)
        self.view.getTitoloLabel().setText(self.model.titolo)
        #TODO getListaOpere