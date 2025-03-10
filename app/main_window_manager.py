import sys

from PyQt6.QtWidgets import QApplication, QWidget

from app.db import Database
from app.ui.main_window_manager_ui_form import Ui_Form
from app.fabric_remains import FabricRemainsWindow
from app.write_offs import WriteOffsWindow


class MainWindowManager(QWidget):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Главное окно")

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.fabric_remains_window = FabricRemainsWindow(db)
        self.write_offs_window = WriteOffsWindow(db)

        self.ui.fabric_remains_button.clicked.connect(
            self.show_fabric_remains_window
        )
        self.ui.unuseful_write_offs_button.clicked.connect(
            self.show_unuseful_write_offs_window
        )

    def show_fabric_remains_window(self):
        self.fabric_remains_window.show()

    def show_unuseful_write_offs_window(self):
        self.write_offs_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    db = Database()
    presentation = MainWindowManager(db)
    presentation.show()
    sys.exit(app.exec())
