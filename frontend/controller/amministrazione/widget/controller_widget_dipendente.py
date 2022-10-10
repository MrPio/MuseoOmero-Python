#######################################################
# 
# ControllerWidgetDipendente.py
# Python implementation of the Class ControllerWidgetDipendente
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.personale.posto_lavoro import PostoLavoro
from frontend.controller.amministrazione.widget.strategy_widget_dipendente.strategy_widget_dipendente import \
    StrategyWidgetDipendente
from frontend.controller.controller import Controller
from frontend.view.amministrazione.widget.widget_posto_lavoro import WidgetPostoLavoro


class ControllerWidgetDipendente(Controller):

    def __init__(self, view: WidgetPostoLavoro, model: PostoLavoro, parent: Controller,
                 strategy: StrategyWidgetDipendente):
        super().__init__(view)

    def __onAssegnaPostoClicked(self) -> None:
        pass

    def __onRimuoviClicked(self) -> None:
        pass

    def __gotoVistaModificaPostoLavoro(self) -> None:
        pass

    def connettiEventi(self) -> None:
        pass

    def initializeUi(self):
        pass