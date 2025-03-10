import matplotlib.pyplot as plt
from PyQt6 import QtWidgets

from app.db import Database
from app.ui.write_offs_ui_form import Ui_Form


class WriteOffsWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Остатки ткани")

        self.db = Database()
        self.cursor = self.db.cursor

        self.configure_table_headers()
        self.configure_material_combobox()
        self.configure_reason_combobox()

        self.ui.material_combobox.currentTextChanged.connect(self.update_table)
        self.ui.reason_combobox.currentTextChanged.connect(self.update_table)
        self.ui.graph_pushbutton.clicked.connect(self.draw_plots)

        self.update_table()

    def configure_table_headers(self):
        headers = [
            "Материал", "Ширина (м)", "Длина (м)",
            "Количество (рулон/шт)", "Причина", "Дата",
            "Стоимость (руб.)",
        ]
        self.ui.materials_table.setColumnCount(len(headers))
        self.ui.materials_table.setHorizontalHeaderLabels(
            headers
        )

    def configure_material_combobox(self):
        self.ui.material_combobox.addItem('Все')
        self.ui.material_combobox.addItems(self.db.get_materials())

    def configure_reason_combobox(self):
        self.ui.reason_combobox.addItem('Все')
        self.ui.reason_combobox.addItems(self.db.get_reasons())

    def get_filtered_write_offs(self):
        selected_material = self.ui.material_combobox.currentText()
        selected_reason = self.ui.reason_combobox.currentText()

        data = self.db.get_write_offs(
            material=selected_material if selected_material else None,
            reason=selected_reason if selected_reason else None
        )

        return data

    def add_total_cost_line(self, data):
        total_remains_cost = sum([r[-1] for r in data])
        self.ui.materials_table.setItem(
            self.ui.materials_table.rowCount() - 1,
            self.ui.materials_table.columnCount() - 2,
            QtWidgets.QTableWidgetItem("Итого:"),
        )
        self.ui.materials_table.setItem(
            self.ui.materials_table.rowCount() - 1,
            self.ui.materials_table.columnCount() - 1,
            QtWidgets.QTableWidgetItem(str(total_remains_cost))
        )

    def adjust_column_size(self):
        self.ui.materials_table.resizeColumnsToContents()
        header = self.ui.materials_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    def update_table(self):
        self.ui.materials_table.clearContents()

        data = self.get_filtered_write_offs()

        self.ui.materials_table.setRowCount(len(data) + 1)
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                self.ui.materials_table.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))
        self.add_total_cost_line(data)

        self.adjust_column_size()
        self.ui.materials_table.setSortingEnabled(True)

    def get_materials_grouped_data(self):
        data = self.get_filtered_write_offs()
        material_index = 0
        materials = [data[i][material_index] for i in range(len(data))]
        amounts = [
            data[i][1] * data[i][2] * data[i][3] if data[i][1] and data[i][2] else data[i][3]
            for i in range(len(data))
        ]

        grouped_data = dict.fromkeys(set(materials), 0)
        for i in range(len(materials)):
            grouped_data[materials[i]] += amounts[i]

        return grouped_data

    def get_reasons_grouped_data(self):
        data = self.get_filtered_write_offs()
        reasons = [data[i][4] for i in range(len(data))]
        amounts = [
            data[i][1] * data[i][2] * data[i][3] if data[i][1] and data[i][2] else data[i][3]
            for i in range(len(data))
        ]

        grouped_data = dict.fromkeys(set(reasons), 0)
        for i in range(len(reasons)):
            grouped_data[reasons[i]] += amounts[i]

        return grouped_data

    def draw_plots(self):
        fig, ax = plt.subplots(1, 2, figsize=(10, 6))

        ax[0].set_title('Списания по материалам')
        materials_data = self.get_materials_grouped_data()
        ax[0].pie(
            materials_data.values(),
            labels=materials_data.keys(),
            autopct='%1.1f%%',
            startangle=140
        )

        ax[1].set_title('Списания по причинам')
        reasons_data = self.get_reasons_grouped_data()
        ax[1].pie(
            reasons_data.values(),
            labels=reasons_data.keys(),
            autopct='%1.1f%%',
            startangle=140
        )

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = WriteOffsWindow()
    form.show()
    sys.exit(app.exec())
