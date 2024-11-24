from PyQt6 import QtCore, QtGui, QtWidgets


class MainUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(705, 508)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 691, 491))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        # self.lineEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        # self.lineEdit.setObjectName("lineEdit")
        # self.verticalLayout.addWidget(self.lineEdit)
        # self.timeEdit = QtWidgets.QTimeEdit(parent=self.horizontalLayoutWidget)
        # self.timeEdit.setObjectName("timeEdit")
        # self.verticalLayout.addWidget(self.timeEdit)
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.listWidget = QtWidgets.QListWidget(parent=self.horizontalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Создать задачу"))


class DialogUi(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("Dialog")
        self.resize(400, 170)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.verticalLayoutWidget)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.accept)  # type: ignore
        self.buttonBox.rejected.connect(self.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
