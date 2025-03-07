from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(599, 489)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/logo-02.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
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
            QPushButton:hover {
                background-color: rgb(200, 150, 155);
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
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(180, 260, 244, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(230, 0, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(150, 150))
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("resources/logo-01.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(150, 310, 302, 139))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fabric_remains_button = QtWidgets.QPushButton(parent=self.widget)
        self.fabric_remains_button.setMinimumSize(QtCore.QSize(0, 65))
        self.fabric_remains_button.setMaximumSize(QtCore.QSize(300, 70))
        self.fabric_remains_button.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.fabric_remains_button.setObjectName("fabric_remains_button")
        self.verticalLayout.addWidget(self.fabric_remains_button)
        self.unuseful_write_offs_button = QtWidgets.QPushButton(parent=self.widget)
        self.unuseful_write_offs_button.setMinimumSize(QtCore.QSize(300, 65))
        self.unuseful_write_offs_button.setMaximumSize(QtCore.QSize(320, 65))
        self.unuseful_write_offs_button.setObjectName("unuseful_write_offs_button")
        self.verticalLayout.addWidget(self.unuseful_write_offs_button)
        self.label_2.raise_()
        self.label.raise_()
        self.fabric_remains_button.raise_()
        self.unuseful_write_offs_button.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Главное окно"))
        self.label.setText(_translate("Form", "Учет затрат и остатков"))
        self.fabric_remains_button.setText(_translate("Form", "Остатки ткани\n"
"(можно использовать)"))
        self.unuseful_write_offs_button.setText(_translate("Form", "Списанные материалы\n"
"(нельзя использовать)"))
