from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, AddEmployeeForm):
        AddEmployeeForm.setObjectName("AddEmployeeForm")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/logo-02.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        AddEmployeeForm.setWindowIcon(icon)
        AddEmployeeForm.resize(700, 700)  # Фиксированный размер окна
        AddEmployeeForm.setStyleSheet("""
            #AddEmployeeForm {
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
            QLineEdit, QComboBox {
                background-color: rgb(255, 255, 255);
                border-radius: 6px;
                font-size: 12pt;
                color: rgb(0, 0, 0);
                font-family: "MS Shell Dlg 2";
                padding: 5px;
            }
        """)

        # Логотип в правом верхнем углу
        self.label_logo = QtWidgets.QLabel(parent=AddEmployeeForm)
        self.label_logo.setGeometry(QtCore.QRect(500, 20, 150, 150))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("logo.png"))  # Укажите путь к логотипу
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")

        # Заголовок формы
        self.label_title = QtWidgets.QLabel(parent=AddEmployeeForm)
        self.label_title.setGeometry(QtCore.QRect(50, 50, 600, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setFamily("MS Shell Dlg 2")
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")

        # Поле для ввода фамилии
        self.label_surname = QtWidgets.QLabel(parent=AddEmployeeForm)
        self.label_surname.setGeometry(QtCore.QRect(50, 120, 200, 30))
        self.label_surname.setObjectName("label_surname")

        self.lineEdit_surname = QtWidgets.QLineEdit(parent=AddEmployeeForm)
        self.lineEdit_surname.setGeometry(QtCore.QRect(50, 150, 600, 40))
        self.lineEdit_surname.setObjectName("lineEdit_surname")

        # Поле для ввода имени
        self.label_name = QtWidgets.QLabel(parent=AddEmployeeForm)
        self.label_name.setGeometry(QtCore.QRect(50, 200, 200, 30))
        self.label_name.setObjectName("label_name")

        self.lineEdit_name = QtWidgets.QLineEdit(parent=AddEmployeeForm)
        self.lineEdit_name.setGeometry(QtCore.QRect(50, 230, 600, 40))
        self.lineEdit_name.setObjectName("lineEdit_name")

        # Поле для ввода отчества
        self.label_patronymic = QtWidgets.QLabel(parent=AddEmployeeForm)
        self.label_patronymic.setGeometry(QtCore.QRect(50, 280, 200, 30))
        self.label_patronymic.setObjectName("label_patronymic")

        self.lineEdit_patronymic = QtWidgets.QLineEdit(parent=AddEmployeeForm)
        self.lineEdit_patronymic.setGeometry(QtCore.QRect(50, 310, 600, 40))
        self.lineEdit_patronymic.setObjectName("lineEdit_patronymic")

        # Поле для выбора роли
        self.label_role = QtWidgets.QLabel(parent=AddEmployeeForm)
        self.label_role.setGeometry(QtCore.QRect(50, 360, 200, 30))
        self.label_role.setObjectName("label_role")

        self.comboBox_role = QtWidgets.QComboBox(parent=AddEmployeeForm)
        self.comboBox_role.setGeometry(QtCore.QRect(50, 390, 600, 40))
        self.comboBox_role.setObjectName("comboBox_role")

        # Кнопка "Добавить сотрудника"
        self.pushButton_add = QtWidgets.QPushButton(parent=AddEmployeeForm)
        self.pushButton_add.setGeometry(QtCore.QRect(250, 500, 200, 50))
        self.pushButton_add.setObjectName("pushButton_add")

        self.retranslateUi(AddEmployeeForm)
        QtCore.QMetaObject.connectSlotsByName(AddEmployeeForm)

    def retranslateUi(self, AddEmployeeForm):
        _translate = QtCore.QCoreApplication.translate
        AddEmployeeForm.setWindowTitle(_translate("AddEmployeeForm", "Добавить сотрудника"))
        self.label_title.setText(_translate("AddEmployeeForm", "Добавить сотрудника"))
        self.label_surname.setText(_translate("AddEmployeeForm", "Фамилия:"))
        self.label_name.setText(_translate("AddEmployeeForm", "Имя:"))
        self.label_patronymic.setText(_translate("AddEmployeeForm", "Отчество:"))
        self.label_role.setText(_translate("AddEmployeeForm", "Роль:"))
        self.pushButton_add.setText(_translate("AddEmployeeForm", "Добавить"))
