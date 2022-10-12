#######################################################
# 
# VistaGestioneMostre.py
# Python implementation of the Class VistaGestioneMostre
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton
from frontend.view.my_main_window import MyMainWindow


class VistaGestioneMostre(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/GestisciMostre')

    def getPreviousButton(self) -> QPushButton:
        return self.previousButton

    def getVisualizzaMostraAttualeButton(self) -> QPushButton:
        return self.visualizzaMostraAttualeButton

    def getAllestisciNuovaMostraButton(self) -> QPushButton:
        return self.allestisciNuovaMostraButton