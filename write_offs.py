from PyQt6 import QtCore, QtGui, QtWidgets
from db import Database

from write_offs_ui_form import Ui_Form


class WriteOffsWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = Database()
        self.cursor = self.db.cursor

        headers = [
                "Материал", "Ширина", "Длина",
                "Количество", "Причина", "Дата",
        ]
        self.ui.materials_table.setRowCount(0)
        self.ui.materials_table.setColumnCount(len(headers))
        self.ui.materials_table.setHorizontalHeaderLabels(
            headers
        )

        self.ui.material_combobox.addItem('Все')
        self.ui.reason_combobox.addItem('Все')
        self.ui.material_combobox.addItems(self.db.get_materials())
        self.ui.reason_combobox.addItems(self.db.get_reasons())

        self.ui.material_combobox.currentTextChanged.connect(self.update_table)
        self.ui.reason_combobox.currentTextChanged.connect(self.update_table)

        self.update_table()

    def update_table(self):
        self.ui.materials_table.clearContents()
        self.ui.materials_table.setRowCount(0)

        selected_material = self.ui.material_combobox.currentText()
        selected_reason = self.ui.reason_combobox.currentText()

        if not selected_material and not selected_reason:
            return

        data = self.db.get_write_offs(
            material=selected_material if selected_material else None,
            reason=selected_reason if selected_reason else None
        )

        if data:
            self.ui.materials_table.setRowCount(len(data))

            for row_num, row_data in enumerate(data):
                for col_num, col_data in enumerate(row_data):
                    self.ui.materials_table.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))

            self.ui.materials_table.resizeColumnsToContents()
            header = self.ui.materials_table.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = WriteOffsWindow()
    form.show()
    sys.exit(app.exec())
