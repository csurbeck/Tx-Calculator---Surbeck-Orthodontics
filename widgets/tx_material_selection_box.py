from PyQt6.QtWidgets import QWidget, QComboBox, QVBoxLayout
from PyQt6.QtCore import pyqtSignal, pyqtSlot
from global_vars import GlobalVariables


class TxMaterialSelectionBox(QWidget):

    def __init__(self):
        super(TxMaterialSelectionBox, self).__init__()

        self.tx_material = QComboBox()
        self.tx_material.addItems(["Select Treatment Material",
                                   "Metal Brackets",
                                   "Clear Brackets",
                                   "Invisalign"])
        self.tx_material.currentTextChanged.connect(self.tx_material_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.tx_material)
        self.setLayout(layout)

    # updates global tx material variable to the current selection made by the user
    def tx_material_changed(self, s):
        GlobalVariables.tx_material = s

    # Resets tx_material ComboBox selection and global variable value when 'reset' button is clicked
    @pyqtSlot()
    def tx_material_reset(self):
        GlobalVariables.tx_material = None
        self.tx_material.setCurrentText("Select Treatment Material")