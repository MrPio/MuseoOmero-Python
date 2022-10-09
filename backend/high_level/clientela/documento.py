#######################################################
# 
# Documento.py
# Python implementation of the Class Documento
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
# 
#######################################################
from datetime import datetime

from backend.high_level.clientela.qr_code import QRCode

import abc

from backend.high_level.clientela.subscriber import Subscriber
from backend.low_level.pagamenti.pagamento import Pagamento
from backend.low_level.sicurezza.qr_code_encoding import QRCodeEncoding


class Documento(abc.ABC):

    def __init__(self,pagamento:Pagamento,dataRilascio : datetime = None):
        self.pagamento=pagamento
        self.data_rilascio=dataRilascio
        self.pagato=False
        self.qr_code=QRCode(QRCodeEncoding())
        self.date_convalida:list[datetime]=[]
        self.subscribers:list[Subscriber]=[]

    @abc.abstractmethod
    def calcolaCosto(self) -> float:
        pass

    @abc.abstractmethod
    def convalida(self) -> bool:
        pass

    def stampa(self) -> None:
        pass

    def acquista(self) -> bool:
        self.pagato= self.pagamento.paga(self.calcolaCosto())
        return self.pagato


    def subscribe(self,subscriber : Subscriber) -> None:
        self.subscribers.append(subscriber)

    def unsubscribe(self,subscriber : Subscriber) -> None:
        self.subscribers.remove(subscriber)

    def notify(self) -> None:
        for subscriber in self.subscribers:
            subscriber.update()