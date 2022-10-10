#######################################################
# 
# Controller.py
# Python implementation of the Class Controller
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:58
# Original author: ValerioMorelli
# 
#######################################################
import abc

from PyQt5.QtWidgets import QWidget

from frontend.view.my_main_window import MyMainWindow


class Controller(abc.ABC):

    def __init__(self, view: MyMainWindow|QWidget) -> None:
        self.view = view

    def initializeUi(self) -> None:
        """
        Questo metodo inizializza la vista mostrando le informazione contenute nel model
        """
        pass

    @abc.abstractmethod
    def connettiEventi(self) -> None:
        """
        Questo metodo assegna gli eventi di interazione dell'utente con i rispettivi metodi
        """
        pass

    def showView(self) -> None:
        self.view.show()

    def hideView(self) -> None:
        self.view.hide()

    def closeView(self) -> None:
        self.view.close()

    def disableView(self) -> None:
        self.view.setEnabled(False)

    def enableView(self) -> None:
        self.view.setEnabled(True)
