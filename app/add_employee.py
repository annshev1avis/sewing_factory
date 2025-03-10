from PyQt6 import QtWidgets
from app.db import Database
from app.ui.add_employee_ui_form import Ui_Form
from authorization_window import CustomMessageBox


class AddEmployeeWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = Database()
        self.cursor = self.db.cursor

        self.load_roles()

        self.ui.pushButton_add.clicked.connect(self.add_employee)

    def load_roles(self):
        roles = self.db.get_positions()
        for role in roles:
            self.ui.comboBox_role.addItem(role[1], role[0])

    def generate_login(self, role_name):
        login = role_name.lower() + 'log'
        return login

    def generate_password(self, role_name):
        password = role_name.lower() + 'pass'
        return password

    def add_employee(self):
        try:
            surname = self.ui.lineEdit_surname.text()
            name = self.ui.lineEdit_name.text()
            patronymic = self.ui.lineEdit_patronymic.text()
            role_id = self.ui.comboBox_role.currentData()  # Получаем ID роли

            if not surname or not name or not patronymic:
                self.show_error_message("Пожалуйста, заполните обязательные поля.")

                return

            role_name = self.ui.comboBox_role.currentText()
            login = self.generate_login(role_name)
            password = self.generate_password(role_name)

            self.db.add_worker(surname, name, patronymic, login, password, role_id)

            QtWidgets.QMessageBox.information(
                self,
                "Успех",
                f"Сотрудник успешно добавлен.\nЛогин: {login}\nПароль: {password}"
            )
        except Exception as e:
            print(e)

        self.ui.lineEdit_surname.clear()
        self.ui.lineEdit_name.clear()
        self.ui.lineEdit_patronymic.clear()

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
    presentation = AddEmployeeWindow()
    presentation.show()
    sys.exit(app.exec())
