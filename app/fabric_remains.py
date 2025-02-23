import sys

from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem
import pymysql
from app.ui.fabric_remains_ui_form import Ui_Form


class FabricRemainsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="sewing_factory"
        )
        self.cursor = self.db.cursor()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.load_materials()
        self.ui.comboBox.currentIndexChanged.connect(self.update_table)
        self.ui.radioButton.toggled.connect(self.update_table)

        self.update_table()

    def load_materials(self):
        query = "SELECT DISTINCT material.name FROM material"
        self.cursor.execute(query)
        materials = self.cursor.fetchall()

        self.ui.comboBox.addItem("Все")
        for material in materials:
            self.ui.comboBox.addItem(material[0])

    def update_table(self):
        material = self.ui.comboBox.currentText()

        self.cursor.execute(f"describe material")
        names = list(i[0] for i in self.cursor.fetchall())[1:]
        
        sort_order = "ASC" if self.ui.radioButton.isChecked() else "DESC"

        if material == "Все":
            query = f"""
                SELECT m.name, wo.width, wo.length,
                wo.quantity, wo.timestamp
                FROM write_off wo
                JOIN material m ON wo.material_id = m.id
                join material_category cat on m.id_category = cat.id
                WHERE wo.can_be_used = true and cat.name = "Ткань"
                order by wo.quantity {sort_order}
            """
            self.cursor.execute(query)
        else:
            query = f"""
                SELECT m.name, wo.width, wo.length,
                wo.quantity, wo.timestamp
                FROM write_off wo
                JOIN material m ON wo.material_id = m.id
                join material_category cat on m.id_category = cat.id
                WHERE wo.can_be_used = true and cat.name = "Ткань"   
                and m.name = "{material}"
                order by wo.quantity {sort_order}
            """
            self.cursor.execute(query)

        remains = self.cursor.fetchall()

        self.ui.tableWidget.setRowCount(len(remains))
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Материал", "Причина", "Количество"])

        for row, remain in enumerate(remains):
            for col, data in enumerate(remain):
                self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(data)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FabricRemainsWindow()
    window.show()
    sys.exit(app.exec())
