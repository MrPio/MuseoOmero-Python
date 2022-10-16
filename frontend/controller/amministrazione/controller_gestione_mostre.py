#######################################################
#
# ControllerGestioneMostre.py
# Python implementation of the Class ControllerGestioneMostre
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
#
#######################################################
import datetime

import winotify

from backend.high_level.gestione_interna.enum.periodo_storico import PeriodoStorico
from backend.high_level.gestione_interna.mostra import Mostra
from backend.high_level.museo import Museo
from frontend.controller.amministrazione.controller_allestisci_mostra import ControllerAllestisciMostra
from frontend.controller.amministrazione.controller_mostra import ControllerMostra
from frontend.controller.controller import Controller
from frontend.ui.location import UI_DIR
from frontend.view.amministrazione.vista_allestisci_mostra import VistaAllestisciMostra
from frontend.view.amministrazione.vista_gestione_mostre import VistaGestioneMostre
from frontend.view.amministrazione.vista_mostra import VistaMostra


class ControllerGestioneMostre(Controller):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.initializeUi()
        self.previous.enableView()

    def __init__(self, view: VistaGestioneMostre, previous: Controller, model: Museo):
        super().__init__(view)
        self.view: VistaGestioneMostre = view
        self.previous = previous
        self.model = model
        self.connettiEventi()

    def __gotoVistaMostra(self) -> None:
        mostra_attuale = None
        for mostra in Museo.getInstance().mostre:
            if mostra.isInCorso():
                mostra_attuale = mostra
        if mostra_attuale is None:
            winotify.Notification(
                app_id='Museo Omero',
                title='Nessuna mostra in corso',
                msg='Al momento non è in corso alcuna mostra!',
                icon=UI_DIR + '/ico/museum_white.ico',
                duration='short',
            ).show()
        else:
            self.next = ControllerMostra(
                view=VistaMostra(),
                previous=self,
                model=mostra_attuale,
            )
            self.next.showView()
            self.disableView()

    def __gotoVistaAllestisciMostra(self) -> None:
        mostra_attuale = None
        for mostra in Museo.getInstance().mostre:
            if mostra.isInCorso():
                mostra_attuale = mostra
        if mostra_attuale is None:
            self.next = ControllerAllestisciMostra(
                view=VistaAllestisciMostra(),
                previous=self,
                model=Mostra(
                    dataInizio=datetime.datetime.now(),
                    dataFine=datetime.datetime.now(),
                    titolo='',
                    descrizione='nuova mostra',
                    tema=PeriodoStorico.PREISTORIA,
                ),
            )
            self.next.showView()
            self.disableView()
        else:
            winotify.Notification(
                app_id='Museo Omero',
                title='Mostra in corso',
                msg='Al momento è già in corso una mostra, aspetta che termini o rimuovila per allestirne un\'altra',
                icon=UI_DIR + '/ico/museum_white.ico',
                duration='short',
            ).show()

    def connettiEventi(self) -> None:
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()
        self.view.getVisualizzaMostraAttualeButton().mouseReleaseEvent = lambda _: self.__gotoVistaMostra()
        self.view.getAllestisciNuovaMostraButton().mouseReleaseEvent = lambda _: self.__gotoVistaAllestisciMostra()
