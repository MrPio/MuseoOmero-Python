#######################################################
# 
# ControllerAcquistoBiglietto.py
# Python implementation of the Class ControllerAcquistoBiglietto
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
import os
import tempfile

from backend.high_level.clientela.biglietto import Biglietto
from backend.high_level.clientela.enum.tariffa import Tariffa
from backend.high_level.clientela.subscriber import Subscriber
from backend.high_level.clientela.visitatore import Visitatore
from backend.high_level.gestione_interna.enum.reparto_museo import RepartoMuseo
from backend.high_level.museo import Museo
from frontend.controller.controller import Controller
from frontend.controller.reception.controller_inserisci_dati_cliente import ControllerInserisciDatiCliente
from frontend.controller.reception.controller_turni_guide import ControllerTurniGuide
from frontend.controller.reception.strategy_turni_guide.strategy_ricerca_turni_guide import StrategyRicercaTurniGuide
from frontend.controller.segreteria.controller_convalida import ControllerConvalida
from frontend.controller.segreteria.strategy_convalida.strategy_ricerca_abbonamento import StrategyRicercaAbbonamento
from frontend.view.reception.vista_acquisto_biglietto import VistaAcquistoBiglietto
from frontend.view.reception.vista_inserisci_dati_cliente import VistaInserisciDatiCliente
from frontend.view.reception.vista_turni_guide import VistaTurniGuide
from frontend.view.segreteria.vista_convalida import VistaConvalida


class ControllerAcquistoBiglietto(Controller, Subscriber):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.enableView()

    def __init__(self, view: VistaAcquistoBiglietto, previous: Controller, model: Biglietto):
        super().__init__(view)
        self.view: VistaAcquistoBiglietto = view
        self.previous = previous
        self.model = model
        self.model.subscribe(self)
        self.previous.disableView()
        self.connettiEventi()
        self.showView()
        self.initializeUi()

    def __gotoVistaTurniGuide(self) -> None:
        self.next = ControllerTurniGuide(
            view=VistaTurniGuide(),
            previous=self,
            model=Museo.getInstance(),
            strategy=StrategyRicercaTurniGuide(),
        )

    def __gotoVistaConvalida(self) -> None:
        self.next = ControllerConvalida(
            view=VistaConvalida(),
            previous=self,
            strategy=StrategyRicercaAbbonamento(),
        )

    def __gotoVistaInserisciDatiCliente(self) -> None:
        if not self.model.acquista():
            self.notifica('Attenzione', 'Si è verificato un errore nel pagamento, si prega di riprovare...')
            return
        if self.model.abbonamento is None:
            self.next = ControllerInserisciDatiCliente(
                view=VistaInserisciDatiCliente(),
                previous=self,
                model=Visitatore(),
            )
            self.closeView()
        else:
            self.notifica('Biglietto Acquistato', f'Biglietto acquistato con successo! \r\n'
                                                  f' ID --> {self.model.qr_code.id}')
            path = tempfile.gettempdir() + '/qrcode.jpg'
            self.model.qr_code.getImage().convert('RGB').save(path)
            os.startfile(path)
            self.previous.enableView()
            self.closeView()

    def __onTariffaBoxChanged(self) -> None:
        self.model.tariffa=Tariffa[self.view.getTariffaComboBox().currentText().upper()]
        self.initializeUi()

    def __onTipoBigliettoChanged(self) -> None:
        self.model.reparto=\
            RepartoMuseo[self.view.getTipoBigliettoComboBox().currentText().upper().replace(' ', '_')]

    def connettiEventi(self) -> None:
        super().connettiEventi()
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()
        self.view.getCercaGuidaButton().clicked.connect(self.__gotoVistaTurniGuide)
        self.view.getVerificaAbbonamentoButton().clicked.connect(self.__gotoVistaConvalida)
        self.view.getConfermaButton().clicked.connect(self.__gotoVistaInserisciDatiCliente)
        self.view.getTariffaComboBox().currentTextChanged.connect(self.__onTariffaBoxChanged)
        self.view.getTipoBigliettoComboBox().currentTextChanged.connect(self.__onTipoBigliettoChanged)

    def initializeUi(self) -> None:
        if self.model.tariffa is not None:
            self.view.getTariffaComboBox().setCurrentIndex(self.model.tariffa.index)
        self.update()

    def update(self) -> None:
        self.view.getCostoLabel().setText(f'€ {self.model.calcolaCosto()}')
