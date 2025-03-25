import sys

from PyQt6.QtWidgets import QApplication

from app.authorization_window import AuthorizationWindow
from app.db import Database


app = QApplication(sys.argv)

db = Database()
window = AuthorizationWindow(
    allowed_roles=[1, 2],
    db_for_other_windows=db,
)

window.show()

app.exec()
