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


class TakeProfitStopLoss(Tab):
    tab: QWidget


    def __init__(self, tab: QWidget):
        super().__init__()
        self.tab = tab
        self.set_non_active_style_sheet()
        self.set_short_frame_default_bg('tpslShortFrame')

        self.tab.findChild(QFrame, 'tpslLongFrame').mousePressEvent = self.long_frame_pressed
        self.tab.findChild(QFrame, 'tpslShortFrame').mousePressEvent = self.short_frame_pressed
        self.tab.findChild(QSlider, 'tpslLeverageSlider').mousePressEvent = self.leverage_slider_pressed
        self.tab.findChild(QSlider, 'tpslLeverageSlider').mouseMoveEvent = self.leverage_slider_moved
        self.tab.findChild(QLineEdit, 'tpslLeverage').textChanged.connect(self.leverage_input_changed)
        self.tab.findChild(QLineEdit, 'tpslLeverage').editingFinished.connect(self.leverage_input_finished)
        self.tab.findChild(QPushButton, 'tpslCalculateBtn').clicked.connect(self.calculate_pnl)


    @Slot(QMouseEvent)
    def long_frame_pressed(self, event: QMouseEvent) -> None:
        self.trade_direction = 'Long'
        self.tab.findChild(QFrame, 'tpslLongFrame').setStyleSheet(self.long_style_sheet)
        (red, green, blue) = self.get_background_color()
        self.tab.findChild(QFrame, 'tpslShortFrame').setStyleSheet(self.non_active_style_sheet)


    @Slot(QMouseEvent)
    def short_frame_pressed(self, event: QMouseEvent) -> None:
        self.trade_direction = 'Short'
        self.tab.findChild(QFrame, 'tpslShortFrame').setStyleSheet(self.short_style_sheet)
        (red, green, blue) = self.get_background_color()
        self.tab.findChild(QFrame, 'tpslLongFrame').setStyleSheet(self.non_active_style_sheet)


    @Slot(QMouseEvent)
    def leverage_slider_pressed(self, event: QMouseEvent) -> None:
        width = self.tab.findChild(QSlider, 'tpslLeverageSlider').width()
        slider_min = self.tab.findChild(QSlider, 'tpslLeverageSlider').minimum()
        slider_max = self.tab.findChild(QSlider, 'tpslLeverageSlider').maximum()

        val = QStyle.sliderValueFromPosition(slider_min, slider_max, event.x(), width)
        self.tab.findChild(QSlider, 'tpslLeverageSlider').setValue(val)

        self.update_leverage_input(val)


    @Slot(QMouseEvent)
    def leverage_slider_moved(self, event: QMouseEvent) -> None:
        self.leverage_slider_pressed(event)


    @Slot(str)
    def leverage_input_changed(self, val: str) -> None:
        try:
            val = int(val)
            if val < 1 or val > 125:
                self.tab.findChild(QLineEdit, 'tpslLeverage').setText('1')
                self.bad_input('Leverage must be between 1 and 125')
                return

            self.tab.findChild(QSlider, 'tpslLeverageSlider').setValue(val)
        except:
            pass


    @Slot()
    def leverage_input_finished(self) -> None:
        try:
            int(self.tab.findChild(QLineEdit, 'tpslLeverage').text())
        except:
            self.tab.findChild(QLineEdit, 'tpslLeverage').setText('1')


    @Slot(int)
    def update_leverage_input(self, val: int) -> None:
        self.tab.findChild(QLineEdit, 'tpslLeverage').setText(str(val))


    @Slot()
    def calculate_pnl(self) -> None:
        try:
            entry_price = float(self.tab.findChild(QLineEdit, 'tpslEntryPrice').text())
            leverage = float(self.tab.findChild(QLineEdit, 'tpslLeverage').text())
            take_profit_perc = float(self.tab.findChild(QLineEdit, 'tpslTakeProfit').text())
            stop_loss_perc = float(self.tab.findChild(QLineEdit, 'tpslStopLoss').text())
        except:
            self.bad_input('Entry price, leverage, take profit or stop loss percentage are either wrong or not filled')
            return

        if self.trade_direction == 'Long':
            take_profit = entry_price + (entry_price * take_profit_perc / 100 * 1 / leverage)
            stop_loss = entry_price - (entry_price * stop_loss_perc / 100 * 1 / leverage)
        else:
            take_profit = entry_price - (entry_price * take_profit_perc / 100 * 1 / leverage)
            stop_loss = entry_price + (entry_price * stop_loss_perc / 100 * 1 / leverage)

        self.tab.findChild(QLineEdit, 'tpslTakeProfitPrice').setText(f'{take_profit:,.2f}')
        self.tab.findChild(QLineEdit, 'tpslStopLossPrice').setText(f'{stop_loss:,.2f}')
