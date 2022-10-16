#######################################################
# 
# VistaMostra.py
# Python implementation of the Class VistaMostra
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:02
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QLabel, QGridLayout

from frontend.ui.location import UI_DIR
from frontend.view.my_main_window import MyMainWindow


class VistaMostra(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/VistaMostra.ui')

    def getPreviousButton(self) -> QPushButton:
        return self.previousButton

    def getTitoloLabel(self) -> QLabel:
        return self.titoloLabel_2

    def getPeriodoStoricoLabel(self) -> QLabel:
        return self.periodoStoricoLabel

    def getListaOpereGridLayout(self) -> QGridLayout:
        return self.listaOpereGridLayout

    def getEliminaButton(self) -> QPushButton:
        return self.eliminaButton
