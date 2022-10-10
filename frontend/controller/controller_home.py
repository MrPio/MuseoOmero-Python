#######################################################
# 
# ControllerHome.py
# Python implementation of the Class ControllerHome
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from backend.high_level.museo import Museo
from backend.low_level.sicurezza.sha256_hashing import SHA256Hashing
from frontend.controller.controller import Controller
from frontend.controller.controller_login import ControllerLogin
from frontend.view.vista_home import VistaHome
from frontend.view.vista_login import VistaLogin


class ControllerHome(Controller):
    def __init__(self, view: VistaHome):
        super().__init__(view)
        self.view: VistaHome = view


    def __gotoLogin(self, reparto) -> None:
        controller = ControllerLogin(
            view=VistaLogin(),
            model=Museo.getInstance(),
            home=self,
            repartoScelto=reparto,
            hashing=SHA256Hashing(),
        )
        controller.connettiEventi()
        controller.showView()
        self.disableView()

    def __onReceptionClicked(self) -> None:
        self.__gotoLogin('reception')

    def __onSegreteriaClicked(self) -> None:
        self.__gotoLogin('segreteria')

    def __onAmministrazioneClicked(self) -> None:
        self.__gotoLogin('amministrazione')

    def connettiEventi(self) -> None:
        self.view.getReceptionButton().mousePressEvent = lambda _: self.__onReceptionClicked()
        self.view.getSegreteriaButton().mousePressEvent = lambda _: self.__onSegreteriaClicked()
        self.view.getAmministrazioneButton().mousePressEvent = lambda _: self.__onAmministrazioneClicked()
