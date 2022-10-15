#######################################################
# 
# StrategyConvalidaBiglietto.py
# Python implementation of the Class StrategyConvalidaBiglietto
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:01
# Original author: ValerioMorelli
# 
#######################################################
from frontend.controller.segreteria.strategy_convalida.strategy_convalida import StrategyConvalida


class StrategyConvalidaBiglietto(StrategyConvalida):
    def initializeUi(self,c : 'ControllerConvalida') -> None:
        c.view.getHeaderLabel().setText('HomeReception ➜ ConvalidaBiglietto')

    def finalizza(self,c : 'ControllerConvalida') -> None:
        # TODO
        pass
