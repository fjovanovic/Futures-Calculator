from PySide6.QtCore import Slot
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (
    QWidget,
    QFrame
)

from .tab import Tab


class LiquidationPrice(Tab):
    tab: QWidget

    def __init__(self, tab: QWidget):
        super().__init__()
        self.tab = tab

        self.tab.findChild(QFrame, 'liqLongFrame').mousePressEvent = self.long_frame_pressed
        self.tab.findChild(QFrame, 'liqShortFrame').mousePressEvent = self.short_frame_pressed


    @Slot(QMouseEvent)
    def long_frame_pressed(self, event: QMouseEvent) -> None:
        self.trade_direction = 'Long'
        self.tab.findChild(QFrame, 'liqLongFrame').setStyleSheet('background-color: rgb(46, 194, 126);')
        (red, green, blue) = self.get_background_color()
        self.tab.findChild(QFrame, 'liqShortFrame').setStyleSheet(f'background-color: rgb({red}, {green}, {blue});')


    @Slot(QMouseEvent)
    def short_frame_pressed(self, event: QMouseEvent) -> None:
        self.trade_direction = 'Short'
        self.tab.findChild(QFrame, 'liqShortFrame').setStyleSheet('background-color: rgb(246, 97, 81);')
        (red, green, blue) = self.get_background_color()
        self.tab.findChild(QFrame, 'liqLongFrame').setStyleSheet(f'background-color: rgb({red}, {green}, {blue});')
