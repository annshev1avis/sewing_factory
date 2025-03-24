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

        roles = self.db.get_roles()

        for role_id, role_name in roles:
            item_widget = QtWidgets.QWidget()
            layout = QtWidgets.QHBoxLayout()
            label = QtWidgets.QLabel(role_name)
            delete_button = QtWidgets.QPushButton("Удалить")

            delete_button.clicked.connect(lambda _, rid=role_id: self.delete_position(rid))

            layout.addWidget(label)
            layout.addWidget(delete_button)
            layout.setContentsMargins(0, 0, 0, 0)
            item_widget.setLayout(layout)

            list_item = QtWidgets.QListWidgetItem(self.ui.listWidget_positions)
            list_item.setSizeHint(item_widget.sizeHint())

            self.ui.listWidget_positions.addItem(list_item)
            self.ui.listWidget_positions.setItemWidget(list_item, item_widget)

    def add_position(self):
        position_name = self.ui.lineEdit_position_name.text()

        if not position_name:
            self.show_error_message("Пожалуйста, введите название должности.")
            return

        self.db.add_role(position_name)
        self.load_positions()

        QtWidgets.QMessageBox.information(self, "Успех", "Должность успешно добавлена.")
        self.ui.lineEdit_position_name.clear()

    def delete_position(self, role_id):
        confirmation = QtWidgets.QMessageBox.question(
            self, "Подтверждение", "Вы уверены, что хотите удалить эту должность?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )

        if confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
            self.db.delete_role(role_id)
            self.load_positions()

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
