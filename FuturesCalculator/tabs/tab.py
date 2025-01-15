from typing import Tuple

from PySide6.QtWidgets import (
    QWidget
)


class Tab(QWidget):
    def __init__(self):
        super().__init__()


    def get_background_color(self) -> Tuple[int, int, int]:
        bg_color = self.tab.palette().color(self.tab.backgroundRole())
        red = bg_color.red()
        green = bg_color.green()
        blue = bg_color.blue()

        return (red, green, blue)
