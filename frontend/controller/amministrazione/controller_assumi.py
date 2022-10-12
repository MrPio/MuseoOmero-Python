#######################################################
# 
# ControllerAssumi.py
# Python implementation of the Class ControllerAssumi
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
from datetime import datetime

from PyQt5.QtGui import QPixmap

from backend.high_level.clientela.enum.sesso import Sesso
from backend.high_level.museo import Museo
from backend.high_level.personale.amministratore import Amministratore
from backend.high_level.personale.amministrazione import Amministrazione
from backend.high_level.personale.dipendente import Dipendente
from backend.high_level.personale.operatore_al_pubblico import OperatoreAlPubblico
from backend.high_level.personale.posto_lavoro import PostoLavoro
from backend.high_level.personale.reception import Reception
from backend.high_level.personale.segretario import Segretario
from backend.high_level.personale.segreteria import Segreteria
from frontend.controller.amministrazione.widget.controller_widget_posto_lavoro import ControllerWidgetPostoLavoro
from frontend.controller.amministrazione.widget.strategy_widget_dipendente.strategy_widget_assegna_posto import \
    StrategyWidgetAssegnaPosto
from frontend.controller.controller import Controller
from frontend.view.amministrazione.vista_assumi import VistaAssumi
from frontend.view.amministrazione.widget.widget_posto_lavoro import WidgetPostoLavoro


class ControllerAssumi(Controller):

    def __gotoPrevious(self) -> None:
        self.closeView()
        self.previous.enableView()

    def __init__(self, view: VistaAssumi, previous: Controller, model: Museo):
        super().__init__(view)
        self.view: VistaAssumi = view
        self.previous = previous
        self.model = model
        self.lavoro_scelto: PostoLavoro | None = None

    def __onConfermaClicked(self) -> None:
        try:
            datetime.strptime(self.view.getDataNascitaLineEdit().text(), '%d/%m/%Y')
        except Exception as e:
            print(e)
            return
        birth = datetime.strptime(self.view.getDataNascitaLineEdit().text(), '%d/%m/%Y')

        if len(self.view.getNomeLineEdit().text()) > 0 and \
                len(self.view.getCognomeLineEdit().text()) > 0 and \
                (datetime.today() - birth).days > 365 * 10:

            nuovo_dip = Dipendente(
                nome=self.view.getNomeLineEdit().text(),
                cognome=self.view.getCognomeLineEdit().text(),
                dataNascita=birth,
                lavoro=self.lavoro_scelto,
                sesso=Sesso[self.view.getSessoComboBox().currentText().upper().strip()],
                email='',
            )
            if self.lavoro_scelto is not None:
                self.lavoro_scelto.assumi(nuovo_dip)
            self.model.dipendenti.append(nuovo_dip)

            self.closeView()
            self.previous.enableView()
            self.previous.initializeUi()

    def connettiEventi(self) -> None:
        self.view.getPreviousButton().mouseReleaseEvent = lambda _: self.__gotoPrevious()
        self.view.getConfermaButton().clicked.connect(self.__onConfermaClicked)
        self.view.getImpiegoComboBox().currentTextChanged.connect(self.initializeUi)

    def __renderizzaPostiLavoro(self) -> list[ControllerWidgetPostoLavoro]:
        result = []
        for posto_lavoro in self.model.posti_lavoro:
            new_widget = WidgetPostoLavoro(self.view.scrollAreaWidgetContents)

            result.append(ControllerWidgetPostoLavoro(
                view=new_widget,
                model=posto_lavoro,
                parent=self,
                strategy=StrategyWidgetAssegnaPosto(),
            ))
        return result

    def initializeUi(self) -> None:
        self.posti_lavoro = self.__renderizzaPostiLavoro()
        selected = self.view.getImpiegoComboBox().currentText()
        matches = {
            'Operatore': Reception,
            'Segretario': Segreteria,
            'Amministratore': Amministrazione,
        }
        if not selected in matches.keys():
            raise 'ControllerAssumi -> chiave posto lavoro [{}] non trovata'.format(selected)
        # rimuovo tutti i widget
        for i in reversed(range(self.view.verticalLayout.count())):
            self.view.verticalLayout.itemAt(i).widget().setParent(None)

        for controller in self.posti_lavoro:
            if type(controller.model) == matches[selected]:
                self.view.verticalLayout.addWidget(controller.view.widget)
