#######################################################
# 
# VistaAllestisciMostra.py
# Python implementation of the Class VistaAllestisciMostra
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox
from frontend.view.my_main_window import MyMainWindow


class VistaAllestisciMostra(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/VistaAllestisciMostra.ui')

    def getPreviousButton(self) -> QPushButton:
        return self.previousButton

    def getTitoloLineEdit(self) -> QLineEdit:
        return self.titoloLineEdit

    def getPeriodoStoricoComboBox(self) -> QComboBox:
        return self.periodoStoricoComboBox

    def getDurataSpinBox(self) -> QSpinBox:
        return self.durataSpinBox

    def getListaOpere(self) -> list[QLabel]:
        pass

    def getConfermaButton(self) -> QPushButton:
        return self.confermaButton