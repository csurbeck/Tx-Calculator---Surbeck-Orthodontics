from PyQt6.QtWidgets import QWidget, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import pyqtSignal, pyqtSlot
from global_vars import GlobalVariables
from logic.calculator import calculate_cost


class CalculateSection(QWidget):
    reset_clicked = pyqtSignal()

    def __init__(self):
        super(CalculateSection, self).__init__()

        self.button = QPushButton("Calculate Treatment Cost")
        self.button.setFixedSize(450, 70)
        self.button.setObjectName("calculate_button")
        self.label = QLabel(f"Treatment Cost: ${GlobalVariables.cost}")
        self.button.clicked.connect(self.calculate_tx_cost)

        self.reset_button = QPushButton("Reset")
        self.reset_button.setFixedSize(60, 30)
        self.reset_button.setObjectName("reset_button")
        self.reset_button.clicked.connect(self.reset)

        layout = QVBoxLayout()
        sub_layout = QHBoxLayout()
        layout.addWidget(self.button)
        sub_layout.addWidget(self.label)
        sub_layout.addWidget(self.reset_button)
        layout.addLayout(sub_layout)

        self.setLayout(layout)

    # $477 up-charge for clear brackets
    def calculate_tx_cost(self):
        if (GlobalVariables.tx_plan is None or GlobalVariables.tx_material is None or GlobalVariables.tx_length is None
                or GlobalVariables.records == ""):
            self.label.setText(f"Please select all treatment details before calculation.")
            self.label.setStyleSheet("""
                        font-size: 20px;
                    """)
        else:
            calculate_cost()
            GlobalVariables.cost = "{:.2f}".format(GlobalVariables.cost)
            self.label.setText(f"Treatment Cost: ${str(GlobalVariables.cost)}")

    def reset(self):
        self.reset_clicked.emit()

        GlobalVariables.cost = 0
        self.label.setText(f"Treatment Cost: ${str(GlobalVariables.cost)}")

