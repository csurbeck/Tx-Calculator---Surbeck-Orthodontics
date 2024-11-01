from PyQt6.QtWidgets import QWidget, QComboBox, QVBoxLayout
from PyQt6.QtCore import pyqtSignal, pyqtSlot
from global_vars import GlobalVariables


class TxLengthSelectionBox(QWidget):

    initial_options = ["Select Treatment Length", "Select Treatment Plan First"]
    phase_I_options = ["Select Treatment Length", "4 months", "5 months", "6 months", "7 months", "8 months",
                       "9 months", "10 months", "11 months", "12 months", "13 months", "14 months", "15 months",
                       "16 months"]
    limited_options = ["Select Treatment Length", "3 months", "4 months", "5 months", "6 months", "7 months",
                       "8 months", "9 months", "10 months", "11 months", "12 months", "13 months", "14 months",
                       "15 months", "16 months"]
    full_tx_options = ["Select Treatment Length", "6 months", "7 months", "8 months", "9 months", "10 months",
                       "11 months", "12 months", "13 months", "14 months", "15 months", "16 months", "17 months",
                       "18 months", "19 months", "20 months", "21 months", "22 months", "23 months", "24 months"]

    def __init__(self):
        super(TxLengthSelectionBox, self).__init__()

        self.tx_length = QComboBox()
        self.tx_length.addItems(self.initial_options)
        self.tx_length.currentTextChanged.connect(self.tx_length_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.tx_length)
        self.setLayout(layout)

    # updates global tx length variable to the current selection made by the user
    def tx_length_changed(self, s):
        GlobalVariables.tx_length = s

    # Sets combo box options to correspond to selected treatment plan
    @pyqtSlot()
    def change_length_selection(self):
        self.tx_length.clear()

        if GlobalVariables.tx_plan == "Phase I – One Arch" or GlobalVariables.tx_plan == "Phase I – Two Arches":
            self.tx_length.addItems(self.phase_I_options)
        elif GlobalVariables.tx_plan == "Limited Treatment":
            self.tx_length.addItems(self.limited_options)
        else:
            self.tx_length.addItems(self.full_tx_options)

    # Resets tx_length ComboBox selection and global variable value when 'reset' button is clicked
    @pyqtSlot()
    def tx_length_reset(self):
        GlobalVariables.tx_length = None
        self.tx_length.setCurrentText("Select Treatment Length")

        self.tx_length.clear()
        self.tx_length.addItems(self.initial_options)

