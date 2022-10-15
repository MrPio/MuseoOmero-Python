#######################################################
# 
# StrategyTurniGuide.py
# Python implementation of the Interface StrategyTurniGuide
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
import abc
class StrategyTurniGuide(abc.ABC):
    @abc.abstractmethod
    def initializeUi(self,c : 'ControllerTurniGuide') -> None:
        pass

    @abc.abstractmethod
    def initializeWidgetUi(self,c : 'ControllerWidgetTurnoGuida') -> None:
        pass