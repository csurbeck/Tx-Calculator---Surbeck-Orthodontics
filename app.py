import sys
import math

from PyQt6 import QtCore
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import (QApplication)
from widgets.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()

    with open('styles.qss', 'r') as f:
        style = f.read()
        # Set the stylesheet of the application
        app.setStyleSheet(style)

    sys.exit(app.exec())
