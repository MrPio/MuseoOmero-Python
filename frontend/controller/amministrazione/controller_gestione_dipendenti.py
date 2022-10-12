#######################################################
# 
# ControllerGestioneDipendenti.py
# Python implementation of the Class ControllerGestioneDipendenti
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.uic import loadUi

from backend.high_level.museo import Museo
from frontend.controller.amministrazione.widget.controller_widget_dipendente import ControllerWidgetDipendente
from frontend.controller.controller import Controller
from frontend.ui.location import UI_DIR
from frontend.view.amministrazione.vista_gestione_dipendenti import VistaGestioneDipendenti
from frontend.view.amministrazione.widget.widget_dipendente import WidgetDipendente


class ControllerGestioneDipendenti(Controller):

    def __gotoPrevious(self) -> None:
        pass

    def __init__(self, view: VistaGestioneDipendenti, previous: Controller, model: Museo):
        super().__init__(view)
        self.view: VistaGestioneDipendenti = view
        self.previous=previous
        self.model=model

        # self.er=WidgetDipendente(self.view.scrollAreaWidgetContents)
        # self.er2 = WidgetDipendente(self.view.scrollAreaWidgetContents)
        # self.er2.getNomeLabel().setText('secondo')
        # self.er3 = WidgetDipendente(self.view.scrollAreaWidgetContents)
        # self.er4 =WidgetDipendente(self.view.scrollAreaWidgetContents)
        # self.er5 =WidgetDipendente(self.view.scrollAreaWidgetContents)
        btn=[QPushButton('sss') for _ in range(50)]
        for i in range(50):
            self.view.verticalLayout.addWidget(btn[i])

        #for widget in self.__renderizzaDiendenti():

    def __gotoVistaAssumi(self) -> None:
        pass

    def connettiEventi(self) -> None:
        pass

    def __renderizzaDipendenti(self) -> list[ControllerWidgetDipendente]:
        pass