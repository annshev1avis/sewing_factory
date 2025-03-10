import sys

from PyQt6.QtWidgets import QApplication

from app.authorization_window import AuthorizationWindow
from app.db import Database
from app.main_window import MainWindow


app = QApplication(sys.argv)

db = Database()
window = AuthorizationWindow(
    allowed_roles=[1, 2],
    db_for_other_windows=db,
)
window.show()

app.exec()
