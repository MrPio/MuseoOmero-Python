#######################################################
#
# ControllerWidgetTurnoGuida.py
# Python implementation of the Class ControllerWidgetOpera
# Generated by Enterprise Architect
# Created on:      07-ott-2022 17:39:59
# Original author: ValerioMorelli
#
#######################################################
import time
from types import NoneType

from PyQt5.QtGui import QPixmap, QImage

from backend.high_level.gestione_interna.opera import Opera
from frontend.controller.controller import Controller
from frontend.controller.reception.controller_vista_opera import ControllerVistaOpera
from frontend.view.reception.vista_opera import VistaOpera
from frontend.view.reception.widget.widget_opera import WidgetOpera


class ControllerWidgetOpera(Controller):

    def __init__(self, view: WidgetOpera, parent: Controller, model: Opera):
        super().__init__(view)
        self.view: WidgetOpera = view
        self.parent = parent
        self.model = model
        self.hold_start = None
        self.initializeUi()
        self.connettiEventi()

    def __startTimer(self):
        self.hold_start = time.time_ns()

    def __onOperaClicked(self) -> None:
        if time.time_ns() - self.hold_start > 200 * 1000000:
            self.__gotoVistaOpera()

    def __gotoVistaOpera(self):
        self.next = ControllerVistaOpera(
            view=VistaOpera(),
            previous=self.parent,
            model=self.model,
        )
        self.parent.disableView()
        self.next.showView()

    def connettiEventi(self) -> None:
        self.view.getOperaLabel().mousePressEvent = lambda _: self.__startTimer()
        self.view.getOperaLabel().mouseReleaseEvent = lambda _: self.__onOperaClicked()

    def initializeUi(self) -> None:
        if type(self.model.immagine) is not NoneType:
            image = QImage(self.model.immagine.tobytes('raw', 'RGBA'), self.model.immagine.size[0],
                           self.model.immagine.size[1], QImage.Format_RGBA8888)
            self.view.getOperaLabel().setPixmap(QPixmap.fromImage(image))
            self.view.getOperaLabel().setMargin(4)
