#######################################################
# 
# AggiungiTurnoGuida.py
# Python implementation of the Class AggiungiTurnoGuida
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
from datetime import datetime

from PyQt5.QtGui import QPixmap

from backend.high_level.gestione_interna.enum.reparto_museo import RepartoMuseo
from backend.high_level.gestione_interna.turno_guida import TurnoGuida
from frontend.controller.amministrazione.controller_modifica_turno_guida import ControllerModificaTurnoGuida
from frontend.controller.amministrazione.widget.strategy_aggiungi_alla_lista.strategy_aggiungi_alla_lista import \
    StrategyAggiungiAllaLista
from frontend.ui.location import UI_DIR
from frontend.view.reception.vista_modifica_turno_guida import VistaModificaTurnoGuida


class AggiungiTurnoGuida(StrategyAggiungiAllaLista):
    def __init__(self):
        self.controller: 'ControllerWidgetAggiungiAllaLista' = None

    def onClicked(self) -> None:
        date: datetime = self.controller.parent.date
        date = datetime(date.year, date.month, date.day, datetime.now().hour, datetime.now().minute)
        self.controller.next = ControllerModificaTurnoGuida(
            view=VistaModificaTurnoGuida(),
            previous=self.controller.parent,
            model=TurnoGuida(
                dataInizio=date,
                dataFine=date,
                reparto=RepartoMuseo.MUSEO_APERTO,
                capienza=1
            ),
        )
        self.controller.next.showView()
        self.controller.parent.disableView()

    def getIcon(self) -> QPixmap:
        return QPixmap(":/icons/add_circle_FILL1_wght600_GRAD200_opsz48_risultato.png")

    def initializeUi(self) -> None:
        self.controller.view.aggiungiAllaListaWidget.setStyleSheet(
            open(UI_DIR + '/css/dottedBorderThick.css', 'r').read())
