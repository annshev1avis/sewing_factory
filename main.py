import sys

from PyQt6.QtWidgets import QApplication

from app.authorization_window import AuthorizationWindow
from app.main_window import MainWindow


app = QApplication(sys.argv)
window = AuthorizationWindow(
    allowed_roles=[1, 2],
    main_window_class=MainWindow,
)
window.show()
app.exec()
