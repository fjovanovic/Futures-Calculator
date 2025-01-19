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


class Pnl(Tab):
    tab: QWidget


    def __init__(self, tab: QWidget):
        super().__init__()
        self.tab = tab

        self.tab.findChild(QFrame, 'pnlLongFrame').mousePressEvent = self.long_frame_pressed
        self.tab.findChild(QFrame, 'pnlShortFrame').mousePressEvent = self.short_frame_pressed
        self.tab.findChild(QSlider, 'pnlLeverageSlider').mousePressEvent = self.leverage_slider_pressed
        self.tab.findChild(QSlider, 'pnlLeverageSlider').mouseMoveEvent = self.leverage_slider_moved
        self.tab.findChild(QLineEdit, 'pnlLeverage').textChanged.connect(self.leverage_input_changed)
        self.tab.findChild(QLineEdit, 'pnlLeverage').editingFinished.connect(self.leverage_input_finished)
        self.tab.findChild(QPushButton, 'pnlCalculateBtn').clicked.connect(self.calculate_pnl)


    @Slot(QMouseEvent)
    def long_frame_pressed(self, event: QMouseEvent) -> None:
        self.trade_direction = 'Long'
        self.tab.findChild(QFrame, 'pnlLongFrame').setStyleSheet('background-color: rgb(46, 194, 126);')
        (red, green, blue) = self.get_background_color()
        self.tab.findChild(QFrame, 'pnlShortFrame').setStyleSheet(f'background-color: rgb({red}, {green}, {blue});')


    @Slot(QMouseEvent)
    def short_frame_pressed(self, event: QMouseEvent) -> None:
        self.trade_direction = 'Short'
        self.tab.findChild(QFrame, 'pnlShortFrame').setStyleSheet('background-color: rgb(246, 97, 81);')
        (red, green, blue) = self.get_background_color()
        self.tab.findChild(QFrame, 'pnlLongFrame').setStyleSheet(f'background-color: rgb({red}, {green}, {blue});')


    @Slot(QMouseEvent)
    def leverage_slider_pressed(self, event: QMouseEvent) -> None:
        width = self.tab.findChild(QSlider, 'pnlLeverageSlider').width()
        slider_min = self.tab.findChild(QSlider, 'pnlLeverageSlider').minimum()
        slider_max = self.tab.findChild(QSlider, 'pnlLeverageSlider').maximum()

        val = QStyle.sliderValueFromPosition(slider_min, slider_max, event.x(), width)
        self.tab.findChild(QSlider, 'pnlLeverageSlider').setValue(val)

        self.update_leverage_input(val)


    @Slot(QMouseEvent)
    def leverage_slider_moved(self, event: QMouseEvent) -> None:
        self.leverage_slider_pressed(event)


    @Slot(str)
    def leverage_input_changed(self, val: str) -> None:
        try:
            val = int(val)
            if val < 1 or val > 125:
                self.tab.findChild(QLineEdit, 'pnlLeverage').setText('1')
                self.bad_input('Leverage must be between 1 and 125')
                return

            self.tab.findChild(QSlider, 'pnlLeverageSlider').setValue(val)
        except:
            pass


    @Slot()
    def leverage_input_finished(self) -> None:
        try:
            int(self.tab.findChild(QLineEdit, 'pnlLeverage').text())
        except:
            self.tab.findChild(QLineEdit, 'pnlLeverage').setText('1')


    @Slot(int)
    def update_leverage_input(self, val: int) -> None:
        self.tab.findChild(QLineEdit, 'pnlLeverage').setText(str(val))


    @Slot()
    def calculate_pnl(self) -> None:
        try:
            entry_price = float(self.tab.findChild(QLineEdit, 'pnlEntryPrice').text())
            exit_price = float(self.tab.findChild(QLineEdit, 'pnlExitPrice').text())
            leverage = float(self.tab.findChild(QLineEdit, 'pnlLeverage').text())
            quantity = float(self.tab.findChild(QLineEdit, 'pnlQuantity').text())
        except:
            self.bad_input('Entry price, exit price, quantity or leverage are either wrong or not filled')
            return

        initial_margin = entry_price / leverage
        if self.trade_direction == 'Long':
            roi = (exit_price - entry_price) / entry_price * 100 * leverage
        else:
            roi = (entry_price - exit_price) / entry_price * 100 * leverage
        pnl = (roi / 100) * quantity


        self.tab.findChild(QLineEdit, 'pnlInitialMargin').setText(f'{initial_margin:,.2f} USDT')
        self.tab.findChild(QLineEdit, 'pnlPnl').setText(f'{pnl:,.2f} USDT')
        self.tab.findChild(QLineEdit, 'pnlRoi').setText(f'{roi:,.2f} %')
