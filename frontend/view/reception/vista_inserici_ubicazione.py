#######################################################
# 
# VistaInsericiUbicazione.py
# Python implementation of the Class VistaInsericiUbicazione
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSpinBox

from frontend.ui.location import UI_DIR
from frontend.view.my_main_window import MyMainWindow


class VistaInsericiUbicazione(MyMainWindow):

    def getPianoLineEdit(self) -> QLineEdit:
        pass

    def getNumeroMagazzinoLineEdit(self) -> QLineEdit:
        pass

    def getScaffaleLineEdit(self) -> QLineEdit:
        pass

    def getPosizioneSpinBox(self) -> QSpinBox:
        return self.posizioneSpinBox

    def getConfermaButton(self) -> QPushButton:
        pass