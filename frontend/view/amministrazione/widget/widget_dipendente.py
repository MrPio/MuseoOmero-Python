#######################################################
# 
# WidgetDipendente.py
# Python implementation of the Class WidgetDipendente
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:02
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

from frontend.ui.location import UI_DIR
from frontend.view.my_main_window import MyMainWindow
from frontend.view.my_widget import MyWidget


class WidgetDipendente(MyWidget):
    def __init__(self,parent):
        super().__init__(UI_DIR + '/dipendenteWidget.ui',parent)

    def getNomeLabel(self) -> QLabel:
        return self.nomeLabel

    def getIcon(self) -> QLabel:
        return self.iconLabel

    def getLicenziaButton(self) -> QPushButton:
        return self.licenziaButton

    def getPromuoviButton(self) -> QPushButton:
        return self.promuoviButton
