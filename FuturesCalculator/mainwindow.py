# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from ui_form import Ui_MainWindow

from tabs import (
    Pnl,
    LiquidationPrice,
    TargetPrice,
    TakeProfitStopLoss
)


class MainWindow(QMainWindow):
    pnl_tab: Pnl
    liquidation_price_tab: LiquidationPrice
    target_price_tab: TargetPrice
    tp_sl_tab: TakeProfitStopLoss


    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pnl_tab = Pnl(self.ui.tabWidget.findChild(QWidget, 'tabPnl'))
        self.liquidation_price_tab = LiquidationPrice(self.ui.tabWidget.findChild(QWidget, 'tabLiquidationPrice'))
        self.target_price_tab = TargetPrice(self.ui.tabWidget.findChild(QWidget, 'tabTargetPrice'))
        self.tp_sl_tab = TakeProfitStopLoss(self.ui.tabWidget.findChild(QWidget, 'tabTpSl'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
