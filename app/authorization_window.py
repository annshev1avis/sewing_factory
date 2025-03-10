import os
import sys

import dotenv
import pymysql
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication

from app.db import Database

from app.ui.authorization_ui_form import Ui_Form


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
    def __init__(self, allowed_roles, db_for_other_windows):
        """
        :param allowed_roles: список с id разрешенных ролей
        :param db_for_other_windows: объект Database, который используется при создании дочерних окон
        """
        super().__init__()

        self.allowed_roles = allowed_roles
        self.db_for_other_windows = db_for_other_windows

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

        if user[1] == 1:  # менеджер
            from app.main_window_manager import MainWindowManager
            self.main_window = MainWindowManager(self.db_for_other_windows)
            self.main_window.show()
        elif user[1] == 2:  # директор
            from app.main_window_director import MainWindowDirector
            self.main_window = MainWindowDirector(self.db_for_other_windows)
            self.main_window.show()

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

    db = Database()
    authorization = AuthorizationWindow(
        allowed_roles=[1, 2],
        db_for_other_windows=db
    )
    authorization.show()
    sys.exit(app.exec())
