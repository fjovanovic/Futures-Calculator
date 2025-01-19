from PySide6.QtCore import Slot
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (
    QWidget,
    QFrame,
    QSlider,
    QStyle,
    QLineEdit
)

from .tab import Tab


class LiquidationPrice(Tab):
    tab: QWidget


    def __init__(self, tab: QWidget):
        super().__init__()
        self.tab = tab

        self.tab.findChild(QFrame, 'liqLongFrame').mousePressEvent = self.long_frame_pressed
        self.tab.findChild(QFrame, 'liqShortFrame').mousePressEvent = self.short_frame_pressed
        self.tab.findChild(QSlider, 'liqLeverageSlider').mousePressEvent = self.leverage_slider_pressed
        self.tab.findChild(QSlider, 'liqLeverageSlider').mouseMoveEvent = self.leverage_slider_moved
        self.tab.findChild(QLineEdit, 'liqLeverage').textChanged.connect(self.leverage_input_changed)
        self.tab.findChild(QLineEdit, 'liqLeverage').editingFinished.connect(self.leverage_input_finished)


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


    @Slot(QMouseEvent)
    def leverage_slider_pressed(self, event: QMouseEvent) -> None:
        width = self.tab.findChild(QSlider, 'liqLeverageSlider').width()
        slider_min = self.tab.findChild(QSlider, 'liqLeverageSlider').minimum()
        slider_max = self.tab.findChild(QSlider, 'liqLeverageSlider').maximum()

        val = QStyle.sliderValueFromPosition(slider_min, slider_max, event.x(), width)
        self.tab.findChild(QSlider, 'liqLeverageSlider').setValue(val)

        self.update_leverage_input(val)


    @Slot(QMouseEvent)
    def leverage_slider_moved(self, event: QMouseEvent) -> None:
        self.leverage_slider_pressed(event)


    @Slot(str)
    def leverage_input_changed(self, val: str) -> None:
        try:
            val = int(val)
            if val < 1 or val > 125:
                self.tab.findChild(QLineEdit, 'liqLeverage').setText('1')
                self.bad_input('Leverage must be between 1 and 125')
                return

            self.tab.findChild(QSlider, 'liqLeverageSlider').setValue(val)
        except:
            pass


    @Slot()
    def leverage_input_finished(self) -> None:
        try:
            int(self.tab.findChild(QLineEdit, 'liqLeverage').text())
        except:
            self.tab.findChild(QLineEdit, 'liqLeverage').setText('1')


    @Slot(int)
    def update_leverage_input(self, val: int) -> None:
        self.tab.findChild(QLineEdit, 'liqLeverage').setText(str(val))
