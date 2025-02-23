"""
Окно, которое будет использоваться для демонстрации модуля,
позволяет удобно перемещаться между основными формами приложения.
После интеграции с другими модулями, этот файл станет бесполезным, и его нужно будет удалить
"""
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

from app.fabric_remains import FabricRemainsWindow
from app.write_offs import WriteOffsWindow

class PresentationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное окно")

        self.fabric_remains_button = QPushButton("Остатки ткани")
        self.fabric_remains_button.clicked.connect(self.show_fabric_remains_window)

        self.unuseful_write_offs_button = QPushButton("Списанные материалы")
        self.unuseful_write_offs_button.clicked.connect(self.show_unuseful_write_offs_window)

        layout = QVBoxLayout()
        layout.addWidget(self.fabric_remains_button)
        layout.addWidget(self.unuseful_write_offs_button)
        self.setLayout(layout)

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
    presentation = PresentationWindow()
    presentation.show()
    sys.exit(app.exec())
