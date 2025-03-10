import sys

import dotenv
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView

from app.db import Database
from app.ui.fabric_remains_ui_form import Ui_Form

dotenv.load_dotenv()


class FabricRemainsWindow(QWidget):
    def __init__(self, db):
        super().__init__()

        self.db = db

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Списанные материалы")

        self.fill_material_combobox()
        self.configure_table_headers()
        self.ui.comboBox.currentIndexChanged.connect(self.update_table)
        self.ui.radioButton.toggled.connect(self.update_table)

        self.update_table()

    def configure_table_headers(self):
        """
        Задаёт количество и подписи столбцов
        :return:
        """
        headers = [
            "Ткань", "Количество рулонов", "Высота (cм)",
            "Ширина (cм)", "Количество (м^2)", "Дата появления",
            "Стоимость (руб)",
        ]
        self.ui.tableWidget.setColumnCount(len(headers))
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

    def fill_material_combobox(self):
        """
        Загружает в комбобокс "Материал" кнопку для каждого отдельного
        материала и для всех сразу
        :return:
        """
        materials = self.db.get_textile_materials()

        self.ui.comboBox.addItem("Все")
        for material in materials:
            self.ui.comboBox.addItem(material)

    def get_usable_write_offs(self):
        """
        Возвращает список строк из таблицы "wite_off", который
        отфильтрован и отсортирован согласно комбобоксам
        :return: двумерный кортеж
        """
        material = self.ui.comboBox.currentText()
        sort_order = "ASC" if self.ui.radioButton.isChecked() else "DESC"

        return self.db.get_usable_write_offs(material, sort_order)

    def add_total_cost_line(self, remains):
        total_remains_cost = sum([r[-1] for r in remains])
        self.ui.tableWidget.setItem(
            self.ui.tableWidget.rowCount() - 1,
            self.ui.tableWidget.columnCount() - 2,
            QTableWidgetItem("Итого:"),
        )
        self.ui.tableWidget.setItem(
            self.ui.tableWidget.rowCount() - 1,
            self.ui.tableWidget.columnCount() - 1,
            QTableWidgetItem(str(total_remains_cost))
        )

    def adjust_column_size(self):
        self.ui.tableWidget.resizeColumnsToContents()
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def update_table(self):
        self.ui.tableWidget.clearContents()

        remains = self.get_usable_write_offs()

        self.ui.tableWidget.setRowCount(len(remains) + 1)

        for row, remain in enumerate(remains):
            for col, data in enumerate(remain):
                self.ui.tableWidget.setItem(
                    row,
                    col,
                    QTableWidgetItem(str(data)),
                )
        self.add_total_cost_line(remains)

        self.adjust_column_size()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    db = Database()
    window = FabricRemainsWindow(db)
    window.show()

    sys.exit(app.exec())
