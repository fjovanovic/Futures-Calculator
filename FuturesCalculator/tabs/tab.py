from typing import Tuple
from textwrap import dedent

from PySide6.QtWidgets import QWidget, QMessageBox


class Tab(QWidget):
    trade_direction: str = 'Long'
    long_style_sheet: str
    short_style_sheet: str
    non_active_style_sheet: str


    def __init__(self):
        super().__init__()
        self.long_style_sheet = dedent('''
            background-color: rgb(46, 194, 126);
            border: 1px solid #000000;
        ''')
        self.short_style_sheet = dedent(f'''
            background-color: rgb(246, 97, 81);
            border: 1px solid #000000;
        ''')


    def get_background_color(self) -> Tuple[int, int, int]:
        bg_color = self.tab.palette().color(self.tab.backgroundRole())
        red = bg_color.red()
        green = bg_color.green()
        blue = bg_color.blue()

        return (red, green, blue)


    def set_non_active_style_sheet(self) -> None:
        (red, green, blue) = self.get_background_color()
        
        self.non_active_style_sheet = dedent(f'''
            background-color: rgb({red}, {green}, {blue});
            border: 1px solid #000000;
        ''')


    def bad_input(self, message: str) -> None:
        alert = QMessageBox()
        alert.setIcon(QMessageBox.Warning)
        alert.setText(message)
        alert.setWindowTitle('Alert error message box')
        alert.exec()
