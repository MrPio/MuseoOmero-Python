#######################################################
# 
# StrategyConvalidaAbbonamento.py
# Python implementation of the Class StrategyConvalidaAbbonamento
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
from frontend.controller.segreteria.strategy_convalida.strategy_convalida import StrategyConvalida


class StrategyConvalidaAbbonamento(StrategyConvalida):
    def initializeUi(self,c : 'ControllerConvalida') -> None:
        c.view.getHeaderLabel().setText('CompraBiglietto ➜ ConvalidaAbbonamento')

    def finalizza(self,c : 'ControllerConvalida') -> None:
        # TODO
        pass