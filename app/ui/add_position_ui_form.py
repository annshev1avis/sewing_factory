from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/logo-02.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.resize(700, 700)  # Фиксированный размер окна
        Form.setStyleSheet("""
            #Form {
                background-color: rgb(181, 213, 202);
            }
            QPushButton {
                background-color: rgb(224, 169, 175);
                border: none;
                border-radius: 6px;
                font-size: 12pt;
                color: rgb(0, 0, 0);
                font-family: "MS Shell Dlg 2";
            }
            QLabel {
                font-size: 14pt;
                color: rgb(0, 0, 0);
                font-family: "MS Shell Dlg 2";
            }
            QLineEdit {
                background-color: rgb(255, 255, 255);
                border-radius: 6px;
                font-size: 12pt;
                color: rgb(0, 0, 0);
                font-family: "MS Shell Dlg 2";
                padding: 5px;
            }
        """)

        # Логотип в правом верхнем углу
        self.label_logo = QtWidgets.QLabel(parent=Form)
        self.label_logo.setGeometry(QtCore.QRect(500, 20, 150, 150))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("resources/logo-01.jpg"))  # Укажите путь к логотипу
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")

        # Заголовок формы
        self.label_title = QtWidgets.QLabel(parent=Form)
        self.label_title.setGeometry(QtCore.QRect(50, 50, 600, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setFamily("MS Shell Dlg 2")
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")

        # Поле для ввода названия должности
        self.label_position_name = QtWidgets.QLabel(parent=Form)
        self.label_position_name.setGeometry(QtCore.QRect(50, 150, 200, 30))
        self.label_position_name.setObjectName("label_position_name")

        self.lineEdit_position_name = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_position_name.setGeometry(QtCore.QRect(50, 190, 600, 40))
        self.lineEdit_position_name.setObjectName("lineEdit_position_name")

        # Кнопка "Добавить должность"
        self.pushButton_add = QtWidgets.QPushButton(parent=Form)
        self.pushButton_add.setGeometry(QtCore.QRect(250, 300, 200, 50))
        self.pushButton_add.setObjectName("pushButton_add")

        # Список для отображения должностей
        self.listWidget_positions = QtWidgets.QListWidget(parent=Form)
        self.listWidget_positions.setGeometry(QtCore.QRect(150, 400, 400, 200))
        self.listWidget_positions.setObjectName("listWidget_positions")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, AddPositionForm):
        _translate = QtCore.QCoreApplication.translate
        AddPositionForm.setWindowTitle(_translate("AddPositionForm", "Добавить должность"))
        self.label_title.setText(_translate("AddPositionForm", "Добавить должность"))
        self.label_position_name.setText(_translate("AddPositionForm", "Название должности:"))
        self.pushButton_add.setText(_translate("AddPositionForm", "Добавить"))
