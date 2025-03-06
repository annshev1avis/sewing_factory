import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

from ui.main_window_ui_form import Ui_Form
from fabric_remains import FabricRemainsWindow
from write_offs import WriteOffsWindow


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное окно")

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.fabric_remains_button.clicked.connect(
            self.show_fabric_remains_window
        )
        self.ui.unuseful_write_offs_button.clicked.connect(
            self.show_unuseful_write_offs_window
        )

        self.fabric_remains_window = None
        self.write_offs_window = None

    def show_fabric_remains_window(self):
        if self.fabric_remains_window is None:
            self.fabric_remains_window = FabricRemainsWindow()
        self.fabric_remains_window.show()

    def show_unuseful_write_offs_window(self):
        if self.write_offs_window is None:
            self.write_offs_window = WriteOffsWindow()
        self.write_offs_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    presentation = MainWindow()
    presentation.show()
    sys.exit(app.exec())
