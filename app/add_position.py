from PyQt6 import QtWidgets
from app.db import Database
from app.ui.add_position_ui_form import Ui_Form
from app.authorization_window import CustomMessageBox


class AddPositionWindow(QtWidgets.QWidget):
    def __init__(self, db):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = db
        self.cursor = self.db.cursor

        self.ui.pushButton_add.clicked.connect(self.add_position)

        self.load_positions()

    def load_positions(self):
        self.ui.listWidget_positions.clear()

        roles = [y for (x, y) in self.db.get_roles()]

        for role in roles:
            self.ui.listWidget_positions.addItem(role)

    def add_position(self):
        position_name = self.ui.lineEdit_position_name.text()

        if not position_name:
            self.show_error_message("Пожалуйста, введите название должности.")

            return

        self.db.add_role(position_name)

        self.load_positions()

        QtWidgets.QMessageBox.information(self, "Успех", "Должность успешно добавлена.")
        self.ui.lineEdit_position_name.clear()

    def show_error_message(self, message):
        msg = CustomMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg.setWindowTitle("Ошибка")
        msg.setText(message)
        msg.exec()


if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    db = Database()
    presentation = AddPositionWindow(db)
    presentation.show()

    sys.exit(app.exec())