#######################################################
# 
# VistaHomeReception.py
# Python implementation of the Class VistaHomeReception
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
from PyQt5.QtWidgets import QPushButton, QLabel

from frontend.ui.location import UI_DIR
from frontend.view.my_main_window import MyMainWindow


class VistaHomeReception(MyMainWindow):

    def __init__(self):
        super().__init__(UI_DIR + '/HomeReception.ui')

    def getAccountIcon(self) -> QLabel:
        return self.accountButton

    def getAcquistoBigliettoButton(self) -> QPushButton:
        return self.acquistaBigliettoBigButton

    def getConvalidaBigliettoButton(self) -> QPushButton:
        return self.convalidaBigliettoBigButton

    def getVendiOperaButton(self) -> QPushButton:
        return self.vendiOperaBigButton

    def getEffettuaDonazioneButton(self) -> QPushButton:
        return self.riceviDonazioneBigButton
