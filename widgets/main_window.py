import sys
import math

from PyQt6 import QtCore
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QLabel, QWidget, QApplication)
from widgets.tx_plan_selection_box import TxPlanSelectionBox
from widgets.tx_material_selection_box import TxMaterialSelectionBox
from widgets.tx_length_selection_box import TxLengthSelectionBox
from widgets.records_radio_buttons import RecordsRadioButtons
from widgets.calculate_section import CalculateSection


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Surbeck Orthodontics — Tx Calculator")
        self.setMinimumSize(1100, 700)

        # main window layout components
        complete_layout = QVBoxLayout()
        tx_type_layout = QHBoxLayout()
        tx_material_layout = QHBoxLayout()
        tx_length_layout = QHBoxLayout()
        records_layout = QHBoxLayout()

        # tx type selection components
        tx_type_label = QLabel("Treatment Plan: ")
        tx_type_selector = TxPlanSelectionBox()

        # tx material selection components
        tx_material_label = QLabel("Treatment Material: ")
        tx_material_selector = TxMaterialSelectionBox()

        # tx length selection components
        tx_length_label = QLabel("Treatment Length: ")
        tx_length_selector = TxLengthSelectionBox()

        # record selection layout components
        records_buffer = QLabel()
        records_options = RecordsRadioButtons()

        calculate_section = CalculateSection()

        tx_type_layout.addWidget(tx_type_label)
        tx_type_layout.addWidget(tx_type_selector)
        complete_layout.addLayout(tx_type_layout)

        tx_material_layout.addWidget(tx_material_label)
        tx_material_layout.addWidget(tx_material_selector)
        complete_layout.addLayout(tx_material_layout)

        tx_length_layout.addWidget(tx_length_label)
        tx_length_layout.addWidget(tx_length_selector)
        complete_layout.addLayout(tx_length_layout)

        records_layout.addWidget(records_buffer)
        records_layout.addWidget(records_options)
        complete_layout.addLayout(records_layout)

        complete_layout.addWidget(calculate_section)

        calculate_section.reset_clicked.connect(tx_type_selector.tx_plan_reset)
        calculate_section.reset_clicked.connect(tx_material_selector.tx_material_reset)
        calculate_section.reset_clicked.connect(tx_length_selector.tx_length_reset)
        calculate_section.reset_clicked.connect(records_options.reset_records)

        tx_type_selector.change_tx_length.connect(tx_length_selector.change_length_selection)

        self.setLayout(complete_layout)