import os
import sys

import dotenv
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView
import pymysql
from app.ui.fabric_remains_ui_form import Ui_Form


dotenv.load_dotenv()


class FabricRemainsWindow(QWidget):
    def __init__(self, db_connection):
        super().__init__()

        self.db = db_connection
        self.cursor = self.db.cursor()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

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
            "Ткань", "Количество рулонов", "Высота (м)",
            "Ширина (м)", "Количество в м2", "Дата появления",
            "Стоимость",
        ]
        self.ui.tableWidget.setColumnCount(len(headers))
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

    def fill_material_combobox(self):
        """
        Загружает в комбобокс "Материал" кнопку для каждого отдельного
        материала и для всех сразу
        :return:
        """

        query = """
            select distinct m.name 
            from material m inner join material_category cat on m.id_category = cat.id
            where cat.name = "Ткань" 
        """
        self.cursor.execute(query)
        materials = self.cursor.fetchall()

        self.ui.comboBox.addItem("Все")
        for material in materials:
            self.ui.comboBox.addItem(material[0])

    def get_remains(self):
        """
        Возвращает список строк из таблицы "wite_off", который
        отфильтрован и отсортирован согласно комбобоксам
        :return: двумерный кортеж
        """
        material = self.ui.comboBox.currentText()
        sort_order = "ASC" if self.ui.radioButton.isChecked() else "DESC"

        if material == "Все":
            query = f"""
                        select material_name, quantity, width, length, width * length, 
                        timestamp, purchase_price * quantity
                        from write_off_with_material_data
                        where can_be_used = True
                        order by width * length {sort_order}
                    """
            self.cursor.execute(query)
        else:
            query = f"""
                        select material_name, quantity, width, length, width * length, 
                        timestamp, purchase_price * quantity
                        from write_off_with_material_data
                        where can_be_used = True and material_name = "{material}"
                        order by width * length {sort_order}
                    """
            self.cursor.execute(query)

        return self.cursor.fetchall()

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

        remains = self.get_remains()

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

    db_connection = pymysql.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE")
    )

    window = FabricRemainsWindow(db_connection)
    window.show()
    sys.exit(app.exec())
