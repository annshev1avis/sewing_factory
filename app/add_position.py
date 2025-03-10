from PyQt6 import QtWidgets
from app.db import Database
from app.ui.add_position_ui_form import Ui_Form
from authorization_window import CustomMessageBox


class AddPositionWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = Database()
        self.cursor = self.db.cursor

        self.ui.pushButton_add.clicked.connect(self.add_position)

    def add_position(self):
        position_name = self.ui.lineEdit_position_name.text()

        if not position_name:
            self.show_error_message("Пожалуйста, введите название должности.")

            return

        self.db.add_pos(position_name)

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
    presentation = AddPositionWindow()
    presentation.show()
    sys.exit(app.exec())