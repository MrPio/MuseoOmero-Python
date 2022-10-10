#######################################################
# 
# ControllerTurniGuide.py
# Python implementation of the Class ControllerTurniGuide
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
import Museo
from frontend.controller.controller import Controller
from frontend.view import VistaTurniGuide
import StrategyTurniGuide
from frontend.controller.controller import ControllerWidgetTurnoGuida
from frontend.controller.controller import ControllerWidgetAggiungiAllaLista

class ControllerTurniGuide(Controller):
    m_ControllerWidgetTurnoGuida= ControllerWidgetTurnoGuida()

    m_ControllerWidgetAggiungiAllaLista= ControllerWidgetAggiungiAllaLista()

    m_StrategyTurniGuide= StrategyTurniGuide()

    m_VistaTurniGuide= VistaTurniGuide()

    def gotoPrevious(self) -> None:
        pass

    def __init__(self,view : VistaTurniGuide, previous : Controller, model : Museo,strategy:StrategyTurniGuide):
        pass

    def gotoVistaModificaTurnoGuida(self) -> None:
        pass

    def __onFrecciaSinistraClicked(self) -> None:
        pass

    def __onFrecciaDestraClicked(self) -> None:
        pass

    def connettiEventi(self) -> None:
        pass

    def __renderizzaTurniGuida(self) -> ControllerWidgetTurnoGuida []:
        pass

    def initializeUi(strategy : StrategyTurniGuide) -> None:
        pass