#######################################################
# 
# ControllerHomeReception.py
# Python implementation of the Class ControllerHomeReception
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.clientela.biglietto import Biglietto
from backend.high_level.gestione_interna.composizione import Composizione
from backend.high_level.gestione_interna.enum.periodo_storico import PeriodoStorico
from backend.high_level.gestione_interna.enum.reparto_museo import RepartoMuseo
from backend.high_level.gestione_interna.enum.tipo_opera import TipoOpera
from backend.high_level.gestione_interna.opera import Opera
from backend.high_level.museo import Museo
from backend.high_level.personale.dipendente import Dipendente
from frontend.controller.controller import Controller
from frontend.controller.controller_account import ControllerAccount
from frontend.controller.reception.controller_acquisto_biglietto import ControllerAcquistoBiglietto
from frontend.controller.reception.controller_aggiungi_opera import ControllerAggiungiOpera
from frontend.controller.reception.controller_ricerca_opera import ControllerRicercaOpera
from frontend.controller.reception.strategy_aggiungi_opera.strategy_ricevi_donazione import StrategyRiceviDonazione
from frontend.controller.reception.strategy_ricerca_opera.strategy_vendi_opera import StrategyVendiOpera
from frontend.controller.segreteria.controller_convalida import ControllerConvalida
from frontend.controller.segreteria.strategy_convalida.strategy_convalida_biglietto import StrategyConvalidaBiglietto
from frontend.view.reception.vista_acquisto_biglietto import VistaAcquistoBiglietto
from frontend.view.reception.vista_aggiungi_opera import VistaAggiungiOpera
from frontend.view.reception.vista_home_reception import VistaHomeReception
from frontend.view.reception.vista_ricerca_opera import VistaRicercaOpera
from frontend.view.segreteria.vista_convalida import VistaConvalida
from frontend.view.vista_account import VistaAccount


class ControllerHomeReception(Controller):
    def __init__(self, view: VistaHomeReception, home: Controller, dipendente: Dipendente):
        super().__init__(view)
        self.view: VistaHomeReception = view
        self.home = home
        self.dipendente = dipendente

    def __gotoVistaAccount(self) -> None:
        self.next = ControllerAccount(
            view=VistaAccount(),
            previous=self,
            home=self.home,
            model=self.dipendente,
        )
        self.next.connettiEventi()
        self.next.showView()
        self.disableView()

    def __gotoVistaAcquistoBiglietto(self) -> None:
        self.next = ControllerAcquistoBiglietto(
            view=VistaAcquistoBiglietto(),
            previous=self,
            model=Biglietto(),
        )
        self.next.connettiEventi()
        self.next.showView()
        self.disableView()

    def __gotoVistaConvalidaBiglietto(self) -> None:
        self.next = ControllerConvalida(
            view=VistaConvalida(),
            previous=self,
            strategy=StrategyConvalidaBiglietto(),
        )
        self.next.connettiEventi()
        self.next.showView()
        self.disableView()

    def __gotoVistaRicercaOpera(self) -> None:
        self.next = ControllerRicercaOpera(
            view=VistaRicercaOpera(),
            previous=self,
            model=Museo.getInstance(),
            strategy=StrategyVendiOpera(),
        )
        self.next.showView()
        self.disableView()

    def __gotoVistaEffettuaDonazione(self) -> None:
        self.next = ControllerAggiungiOpera(
            view=VistaAggiungiOpera(),
            previous=self,
            strategy=StrategyRiceviDonazione(),
        )
        self.next.connettiEventi()
        self.next.showView()
        self.disableView()

    def connettiEventi(self) -> None:
        self.view.getAccountIcon().mouseReleaseEvent = lambda _: self.__gotoVistaAccount()
        self.view.getAcquistoBigliettoButton().mouseReleaseEvent = lambda _: self.__gotoVistaAcquistoBiglietto()
        self.view.getConvalidaBigliettoButton().mouseReleaseEvent = lambda _: self.__gotoVistaConvalidaBiglietto()
        self.view.getVendiOperaButton().mouseReleaseEvent = lambda _: self.__gotoVistaRicercaOpera()
        self.view.getEffettuaDonazioneButton().mouseReleaseEvent = lambda _: self.__gotoVistaEffettuaDonazione()