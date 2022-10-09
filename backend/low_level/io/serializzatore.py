#######################################################
# 
# Serializzatore.py
# Python implementation of the Interface Serializzatore
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:40:00
# Original author: ValerioMorelli
# 
#######################################################
import abc


class Serializzatore(abc.ABC):
    @abc.abstractmethod
    def serializza(self,path,obj: object) -> None:
        pass

    @abc.abstractmethod
    def deserializza(self,path) -> object:
        pass