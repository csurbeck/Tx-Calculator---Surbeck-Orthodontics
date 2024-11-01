from PyQt6.QtWidgets import QWidget, QComboBox, QVBoxLayout, QHBoxLayout, QRadioButton
from PyQt6.QtCore import pyqtSignal, pyqtSlot
from global_vars import GlobalVariables


class RecordsRadioButtons(QWidget):
    def __init__(self, *args, **kwargs):
        super(RecordsRadioButtons, self).__init__(*args, **kwargs)

        layout = QHBoxLayout()

        # radio buttons for record options
        self.no_records = QRadioButton('No Records', self)
        self.no_records.toggled.connect(self.update_records)

        self.yes_records = QRadioButton('Records', self)
        self.yes_records.toggled.connect(self.update_records)

        layout.addWidget(self.no_records)
        layout.addWidget(self.yes_records)

        self.setLayout(layout)

    def update_records(self):
        if self.no_records.isChecked():
            GlobalVariables.records = "No Records"
        elif self.yes_records.isChecked():
            GlobalVariables.records = "Records"

    @pyqtSlot()
    def reset_records(self):
        GlobalVariables.records = ""
        for radioButton in [self.no_records, self.yes_records]:
            radioButton.setAutoExclusive(False)
            radioButton.setChecked(False)
            radioButton.setAutoExclusive(True)
