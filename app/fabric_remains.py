import os
import sys

import dotenv
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem
import pymysql
from app.ui.fabric_remains_ui_form import Ui_Form


dotenv.load_dotenv()


class FabricRemainsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.db = pymysql.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE")
        )
        self.cursor = self.db.cursor()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.load_materials()
        self.ui.comboBox.currentIndexChanged.connect(self.update_table)
        self.ui.radioButton.toggled.connect(self.update_table)

        self.update_table()

    def load_materials(self):
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

    def update_table(self):
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

        remains = self.cursor.fetchall()

        self.ui.tableWidget.setRowCount(len(remains))
        self.ui.tableWidget.setColumnCount(len(remains[0]))
        self.ui.tableWidget.setHorizontalHeaderLabels(
            [
                "Ткань", "Количество рулонов", "Высота (м)",
                "Ширина (м)", "Количество в м2", "Дата появления",
                "Стоимость",
            ]
        )

        for row, remain in enumerate(remains):
            for col, data in enumerate(remain):
                self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(data)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FabricRemainsWindow()
    window.show()
    sys.exit(app.exec())
