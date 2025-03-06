import os
import sys

import dotenv
import pymysql
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication

from main_window import MainWindow
from ui.authorization_ui_form import Ui_Form


dotenv.load_dotenv()


class CustomMessageBox(QtWidgets.QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QMessageBox {
                background-color: rgb(181, 213, 202);
                font-family: "MS Shell Dlg 2";
                font-size: 12pt;
                color: rgb(0, 0, 0);
            }
            QMessageBox QLabel {
                color: rgb(0, 0, 0);
                font-size: 12pt;
            }
            QMessageBox QPushButton {
                background-color: rgb(224, 169, 175);
                border: none;
                border-radius: 6px;
                font-size: 12pt;
                color: rgb(0, 0, 0);
                padding: 5px 10px;
                min-width: 80px;
            }
            QMessageBox QPushButton:hover {
                background-color: rgb(200, 150, 155);
            }
        """)


class AuthorizationWindow(QtWidgets.QWidget):
    def __init__(self, allowed_roles, main_window_class):
        """
        :param allowed_roles: список с id разрешенных ролей
        :param main_window_class: ссылка на КЛАСС окна,
        которое должно открываться после авторизации
        """
        super().__init__()

        self.allowed_roles = allowed_roles
        self.main_window_class = main_window_class

        self.setWindowTitle("Авторизация")
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.connection = pymysql.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE")
        )
        self.cursor = self.connection.cursor()

        self.ui.pushButton_login.clicked.connect(self.authorize)

    def get_worker_from_db(self, username, password):
        """
        Возвращает логин и id роли сотрудника, если он есть в БД,
        иначе None
        :return: (логин, id)
        """
        query = "SELECT login, id_role FROM worker WHERE login = %s AND password = %s"
        self.cursor.execute(query, (username, password))

        return self.cursor.fetchone()

    def authorize(self):
        """
        Проверяет наличие пользователя в базе и
        открывает ему окна модуля, если его роль входит в self.allowed_roles
        :return:
        """

        username = self.ui.lineEdit_username.text()
        password = self.ui.lineEdit_password.text()

        if not username or not password:
            self.show_error_message("Пожалуйста, заполните все поля.")
            return

        user = self.get_worker_from_db(username, password)

        if not user:
            self.show_error_message("Неверный логин или пароль.")
            return

        if user[1] not in self.allowed_roles:
            self.show_error_message("Неподходящая роль для входа в данный модуль.")
            return

        self.write_offs = self.main_window_class()
        self.write_offs.show()
        self.close()

    def show_error_message(self, message):
        msg = CustomMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg.setWindowTitle("Ошибка")
        msg.setText(message)
        msg.exec()

    def closeEvent(self, event):
        self.cursor.close()
        self.connection.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # подставить данные своего модуля
    authorization = AuthorizationWindow(
        allowed_roles=[1, 2],
        main_window_class=MainWindow,
    )
    authorization.show()
    sys.exit(app.exec())
