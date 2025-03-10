from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1027, 604)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/logo-02.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        # Form.setStyleSheet("""
        #     #Form{
        #         background-color:rgb(181, 213, 202);
        #     }
        #     QPushButton{
        #         background-color: rgb(224, 169, 175); /* Зеленый цвет */
        #         border: none; /* Убираем рамку */
        #         border-radius: 6px; /* Скругленные края */
        #         font-size: 10pt;
        #     }
        #     QTableWidget{
        #         background-color: rgb(255, 252, 214);
        #     }
        # )""")
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

                    QMessage
                    }
                """)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.icon_label = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_label.sizePolicy().hasHeightForWidth())
        self.icon_label.setSizePolicy(sizePolicy)
        self.icon_label.setMinimumSize(QtCore.QSize(60, 60))
        self.icon_label.setMaximumSize(QtCore.QSize(60, 60))
        self.icon_label.setPixmap(QtGui.QPixmap("resources/logo-02.jpg"))
        self.icon_label.setScaledContents(True)
        self.icon_label.setObjectName("icon_label")
        self.horizontalLayout_3.addWidget(self.icon_label)
        self.title_label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout_3.addWidget(self.title_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.material_layout = QtWidgets.QVBoxLayout()
        self.material_layout.setObjectName("material_layout")
        self.material_label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.material_label.setFont(font)
        self.material_label.setObjectName("material_label")
        self.material_layout.addWidget(self.material_label)
        self.material_combobox = QtWidgets.QComboBox(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.material_combobox.sizePolicy().hasHeightForWidth())
        self.material_combobox.setSizePolicy(sizePolicy)
        self.material_combobox.setMinimumSize(QtCore.QSize(230, 0))
        self.material_combobox.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.material_combobox.setFont(font)
        self.material_combobox.setObjectName("material_combobox")
        self.material_layout.addWidget(self.material_combobox)
        self.horizontalLayout_2.addLayout(self.material_layout)
        self.reason_layout = QtWidgets.QVBoxLayout()
        self.reason_layout.setObjectName("reason_layout")
        self.reason_label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reason_label.setFont(font)
        self.reason_label.setObjectName("reason_label")
        self.reason_layout.addWidget(self.reason_label)
        self.reason_combobox = QtWidgets.QComboBox(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reason_combobox.sizePolicy().hasHeightForWidth())
        self.reason_combobox.setSizePolicy(sizePolicy)
        self.reason_combobox.setMinimumSize(QtCore.QSize(230, 0))
        self.reason_combobox.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reason_combobox.setFont(font)
        self.reason_combobox.setObjectName("reason_combobox")
        self.reason_layout.addWidget(self.reason_combobox)
        self.horizontalLayout_2.addLayout(self.reason_layout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.graph_pushbutton = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_pushbutton.sizePolicy().hasHeightForWidth())
        self.graph_pushbutton.setSizePolicy(sizePolicy)
        self.graph_pushbutton.setMinimumSize(QtCore.QSize(120, 50))
        self.graph_pushbutton.setMaximumSize(QtCore.QSize(150, 50))
        self.graph_pushbutton.setAutoFillBackground(False)
        self.graph_pushbutton.setObjectName("graph_pushbutton")
        self.horizontalLayout_3.addWidget(self.graph_pushbutton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.scrollArea = QtWidgets.QScrollArea(parent=Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1003, 509))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.materials_table = QtWidgets.QTableWidget(parent=self.scrollAreaWidgetContents)
        self.materials_table.setObjectName("materials_table")
        self.materials_table.setColumnCount(0)
        self.materials_table.setRowCount(0)
        self.horizontalLayout.addWidget(self.materials_table)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Списанные материалы"))
        self.title_label.setText(_translate("Form", "Списанные материалы"))
        self.material_label.setText(_translate("Form", "Выбрать материал:"))
        self.reason_label.setText(_translate("Form", "Выбрать причину:"))
        self.graph_pushbutton.setText(_translate("Form", "Построить\nграфик"))
