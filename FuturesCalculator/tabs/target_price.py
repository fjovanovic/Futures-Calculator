from PySide6.QtCore import Slot
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (
    QWidget,
    QFrame,
    QSlider,
    QStyle,
    QLineEdit,
    QPushButton
)

from .tab import Tab


class TargetPrice(Tab):
    tab: QWidget


    def __init__(self, tab: QWidget):
        super().__init__()
        self.tab = tab
        self.set_non_active_style_sheet()
        self.set_short_frame_default_bg('targetShortFrame')

        self.tab.findChild(QFrame, 'targetLongFrame').mousePressEvent = self.long_frame_pressed
        self.tab.findChild(QFrame, 'targetShortFrame').mousePressEvent = self.short_frame_pressed
        self.tab.findChild(QSlider, 'targetLeverageSlider').mousePressEvent = self.leverage_slider_pressed
        self.tab.findChild(QSlider, 'targetLeverageSlider').mouseMoveEvent = self.leverage_slider_moved
        self.tab.findChild(QLineEdit, 'targetLeverage').textChanged.connect(self.leverage_input_changed)
        self.tab.findChild(QLineEdit, 'targetLeverage').editingFinished.connect(self.leverage_input_finished)
        self.tab.findChild(QPushButton, 'targetCalculateBtn').clicked.connect(self.calculate_target_price)


    @Slot(QMouseEvent)
    def long_frame_pressed(self, event: QMouseEvent) -> None:
        self.trade_direction = 'Long'
        self.tab.findChild(QFrame, 'targetLongFrame').setStyleSheet(self.long_style_sheet)
        self.tab.findChild(QFrame, 'targetShortFrame').setStyleSheet(self.non_active_style_sheet)


    @Slot(QMouseEvent)
    def short_frame_pressed(self, event: QMouseEvent) -> None:
        self.trade_direction = 'Short'
        self.tab.findChild(QFrame, 'targetShortFrame').setStyleSheet(self.short_style_sheet)
        self.tab.findChild(QFrame, 'targetLongFrame').setStyleSheet(self.non_active_style_sheet)


    @Slot(QMouseEvent)
    def leverage_slider_pressed(self, event: QMouseEvent) -> None:
        width = self.tab.findChild(QSlider, 'targetLeverageSlider').width()
        slider_min = self.tab.findChild(QSlider, 'targetLeverageSlider').minimum()
        slider_max = self.tab.findChild(QSlider, 'targetLeverageSlider').maximum()

        val = QStyle.sliderValueFromPosition(slider_min, slider_max, event.x(), width)
        self.tab.findChild(QSlider, 'targetLeverageSlider').setValue(val)

        self.update_leverage_input(val)


    @Slot(QMouseEvent)
    def leverage_slider_moved(self, event: QMouseEvent) -> None:
        self.leverage_slider_pressed(event)


    @Slot(str)
    def leverage_input_changed(self, val: str) -> None:
        try:
            val = int(val)
            if val < 1 or val > 125:
                self.tab.findChild(QLineEdit, 'targetLeverage').setText('1')
                self.bad_input('Leverage must be between 1 and 125')
                return

            self.tab.findChild(QSlider, 'targetLeverageSlider').setValue(val)
        except:
            pass


    @Slot()
    def leverage_input_finished(self) -> None:
        try:
            int(self.tab.findChild(QLineEdit, 'targetLeverage').text())
        except:
            self.tab.findChild(QLineEdit, 'targetLeverage').setText('1')


    @Slot(int)
    def update_leverage_input(self, val: int) -> None:
        self.tab.findChild(QLineEdit, 'targetLeverage').setText(str(val))


    @Slot()
    def calculate_target_price(self) -> None:
        try:
            entry_price = float(self.tab.findChild(QLineEdit, 'targetEntryPrice').text())
            leverage = float(self.tab.findChild(QLineEdit, 'targetLeverage').text())
            roi = float(self.tab.findChild(QLineEdit, 'targetRoi').text())
            if roi < 0:
                raise Exception
        except:
            self.bad_input('Entry price, leverage or ROI are either wrong or not filled')
            return

        if self.trade_direction == 'Long':
            target_price = entry_price + (entry_price * roi / 100 * 1 / leverage)
        else:
            target_price = entry_price - (entry_price * roi / 100 * 1 / leverage)

        self.tab.findChild(QLineEdit, 'targetTargetPrice').setText(f'{target_price:,.2f} USDT')
