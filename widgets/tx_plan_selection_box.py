from PyQt6.QtWidgets import QWidget, QComboBox, QVBoxLayout
from PyQt6.QtCore import pyqtSignal, pyqtSlot
from global_vars import GlobalVariables


class TxPlanSelectionBox(QWidget):
    change_tx_length = pyqtSignal()

    def __init__(self):
        super(TxPlanSelectionBox, self).__init__()

        self.tx_plan = QComboBox()
        self.tx_plan.addItems(["Select Treatment Plan",
                               "Phase I – One Arch",
                               "Phase I – Two Arches",
                               "Limited Treatment",
                               "Full Treatment – Child",
                               "Full Treatment – Child, Surgery",
                               "Full Treatment – Adult",
                               "Full Treatment – Adult, Surgery"])
        self.tx_plan.adjustSize()
        self.tx_plan.currentTextChanged.connect(self.tx_plan_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.tx_plan)
        self.setLayout(layout)

    # updates global tx type variable to the current selection made by the user and sends signal to change tx length
    # in combo box
    def tx_plan_changed(self, s):
        GlobalVariables.tx_plan = s
        self.change_tx_length.emit()

    # Resets tx_plan ComboBox selection and global variable value when 'reset' button is clicked
    @pyqtSlot()
    def tx_plan_reset(self):
        GlobalVariables.tx_plan = None
        self.tx_plan.setCurrentText("Select Treatment Plan")
