#######################################################
# 
# ControllerYesNo.py
# Python implementation of the Class ControllerYesNo
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################

from frontend.controller.controller import Controller
from frontend.view.vista_yes_no import VistaYesNo


class ControllerYesNo(Controller):
    def __init__(self, view: VistaYesNo, previous: Controller, onConfermaCliked: 'function'):
        super().__init__(view)
        self.view: VistaYesNo = view
        self.previous: Controller = previous
        self.onConfermaCliked = onConfermaCliked
        self.connettiEventi()

    def __onAnnullaClicked(self) -> None:
        self.closeView()
        self.previous.enableView()

    def __onConfermaClicked(self) -> None:
        self.closeView()
        self.previous.enableView()
        self.onConfermaCliked()

    def connettiEventi(self) -> None:
        self.view.getConfermaButton().mouseReleaseEvent =  lambda _: self.__onConfermaClicked()
        self.view.getAnnullaButton().mouseReleaseEvent = lambda _: self.__onAnnullaClicked()

