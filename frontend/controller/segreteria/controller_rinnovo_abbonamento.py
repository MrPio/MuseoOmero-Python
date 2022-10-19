#######################################################
# 
# ControllerRinnovoAbbonamento.py
# Python implementation of the Class ControllerRinnovoAbbonamento
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.clientela.abbonamento import Abbonamento
from backend.high_level.clientela.enum.tipo_abbonamento import TipoAbbonamento
from frontend.controller.controller import Controller
from frontend.controller.segreteria.controller_convalida import ControllerConvalida
from frontend.controller.segreteria.controller_vista_abbonamento import ControllerVistaAbbonamento
from frontend.controller.segreteria.strategy_convalida.strategy_ricerca_abbonamento import StrategyRicercaAbbonamento
from frontend.view.segreteria.vista_abbonamento import VistaAbbonamento
from frontend.view.segreteria.vista_convalida import VistaConvalida
from frontend.view.segreteria.vista_rinnovo_abbonamento import VistaRinnovoAbbonamento


class ControllerRinnovoAbbonamento(Controller):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.initializeUi()
        self.previous.enableView()

    def __init__(self, view: VistaRinnovoAbbonamento, previous: Controller, model: Abbonamento | None = None):
        super().__init__(view)
        self.view: VistaRinnovoAbbonamento = view
        self.previous = previous
        self.model = model
        self.initializeUi()

    def __onConfermaClicked(self) -> None:
        self.model.rinnova(TipoAbbonamento[self.view.getDurataComboBox().currentText().upper()])
        self.closeView()
        self.previous.enableView()

    def __gotoVistaConvalida(self) -> None:
        self.next = ControllerConvalida(
            view=VistaConvalida(),
            previous=self,
            strategy=StrategyRicercaAbbonamento(),
        )
        self.next.connettiEventi()
        self.next.showView()
        self.disableView()

    def __gotoVistaAbbonamento(self) -> None:
        self.next = ControllerVistaAbbonamento(
            view=VistaAbbonamento(),
            previous=self,
            model=Abbonamento(),
        )
        self.next.connettiEventi()
        self.next.showView()
        self.disableView()

    def __onDurataChanged(self) -> None:
        self.view.getImportoTotaleLabel().setText(
            str(TipoAbbonamento[self.view.getDurataComboBox().currentText().upper()].cost))

    def connettiEventi(self) -> None:
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()
        self.view.getConfermaButton().clicked.connect(self.__onConfermaClicked)
        self.view.getDurataComboBox().currentTextChanged.connect(self.__onDurataChanged)

    def initializeUi(self) -> None:
        self.view.getQrCodeImage()
        #TODO inizializzare Qr-Code nella label
        pass
