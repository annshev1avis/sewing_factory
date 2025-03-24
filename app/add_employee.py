from PyQt6 import QtWidgets
from app.db import Database
from app.ui.add_employee_ui_form import Ui_Form
from app.authorization_window import CustomMessageBox


class AddEmployeeWindow(QtWidgets.QWidget):
    def __init__(self, db):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = db
        self.current_employee_id = None  # ID редактируемого сотрудника

        self.load_roles()
        self.load_employees()

        self.ui.pushButton_add.clicked.connect(self.save_employee)

    def load_roles(self):
        roles = self.db.get_roles()
        for role in roles:
            self.ui.comboBox_role.addItem(role[1], role[0])

    def load_employees(self):
        self.ui.listWidget_employees.clear()
        employees = self.db.get_employees()

        for emp_id, surname, name, patronymic, role_name in employees:
            item_widget = QtWidgets.QWidget()
            layout = QtWidgets.QHBoxLayout()
            label = QtWidgets.QLabel(f"{surname} {name} {patronymic} ({role_name})")
            edit_button = QtWidgets.QPushButton("Изменить")
            delete_button = QtWidgets.QPushButton("Удалить")

            edit_button.clicked.connect(lambda _, eid=emp_id: self.edit_employee(eid))
            delete_button.clicked.connect(lambda _, eid=emp_id: self.delete_employee(eid))

            layout.addWidget(label)
            layout.addWidget(edit_button)
            layout.addWidget(delete_button)
            layout.setContentsMargins(0, 0, 0, 0)
            item_widget.setLayout(layout)

            list_item = QtWidgets.QListWidgetItem(self.ui.listWidget_employees)
            list_item.setSizeHint(item_widget.sizeHint())
            self.ui.listWidget_employees.addItem(list_item)
            self.ui.listWidget_employees.setItemWidget(list_item, item_widget)

    def generate_login(self, role_name):
        return role_name.lower() + 'log'

    def generate_password(self, role_name):
        return role_name.lower() + 'pass'

    def save_employee(self):
        try:
            surname = self.ui.lineEdit_surname.text()
            name = self.ui.lineEdit_name.text()
            patronymic = self.ui.lineEdit_patronymic.text()
            role_id = self.ui.comboBox_role.currentData()
            role_name = self.ui.comboBox_role.currentText()

            if not surname or not name or not patronymic:
                self.show_error_message("Пожалуйста, заполните обязательные поля.")
                return

            if self.current_employee_id:
                self.db.update_worker(self.current_employee_id, surname, name, patronymic, role_id)
                QtWidgets.QMessageBox.information(self, "Успех", "Данные сотрудника обновлены.")
            else:
                login = self.generate_login(role_name)
                password = self.generate_password(role_name)
                self.db.add_worker(surname, name, patronymic, login, password, role_id)
                QtWidgets.QMessageBox.information(
                    self,
                    "Успех",
                    f"Сотрудник успешно добавлен.\nЛогин: {login}\nПароль: {password}"
                )

            self.current_employee_id = None  # Сброс после сохранения
            self.ui.pushButton_add.setText("Добавить")
            self.clear_input_fields()
            self.load_employees()
        except Exception as e:
            print(e)

    def edit_employee(self, emp_id):
        employee = self.db.get_worker_by_id(emp_id)
        if employee:
            self.current_employee_id, surname, name, patronymic, role_id = employee
            self.ui.lineEdit_surname.setText(surname)
            self.ui.lineEdit_name.setText(name)
            self.ui.lineEdit_patronymic.setText(patronymic)
            self.ui.comboBox_role.setCurrentIndex(self.ui.comboBox_role.findData(role_id))
            self.ui.pushButton_add.setText("Сохранить")

    def delete_employee(self, emp_id):
        confirmation = QtWidgets.QMessageBox.question(
            self, "Подтверждение", "Вы уверены, что хотите удалить этого сотрудника?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )

        if confirmation == QtWidgets.QMessageBox.StandardButton.Yes:
            self.db.delete_worker(emp_id)
            self.load_employees()

    def clear_input_fields(self):
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

    db = Database()
    presentation = AddEmployeeWindow(db)
    presentation.show()

    sys.exit(app.exec())
