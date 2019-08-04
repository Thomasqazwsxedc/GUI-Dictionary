from PyQt5 import QtCore, QtGui, QtWidgets


class Param_Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 30, 281, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frequency = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.frequency.setObjectName("frequency")
        self.gridLayout.addWidget(self.frequency, 2, 1, 1, 1)
        self.pronunciation = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.pronunciation.setObjectName("pronunciation")
        self.gridLayout.addWidget(self.pronunciation, 2, 0, 1, 1)
        self.syllable_count = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.syllable_count.setObjectName("syllable_count")
        self.gridLayout.addWidget(self.syllable_count, 1, 1, 1, 1)
        self.parts_of_speech = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.parts_of_speech.setObjectName("parts_of_speech")
        self.gridLayout.addWidget(self.parts_of_speech, 1, 0, 1, 1)
        self.definition = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.definition.setObjectName("definition")
        self.gridLayout.addWidget(self.definition, 0, 1, 1, 1)
        self.english_spanish = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.english_spanish.setObjectName("english_spanish")
        self.english_spanish.addItem("")
        self.english_spanish.addItem("")
        self.gridLayout.addWidget(self.english_spanish, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.param = [self.definition, self.parts_of_speech, self.syllable_count, self.pronunciation, self.frequency]

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Metadata Parameters"))
        self.label.setText(_translate("Dialog", "Metadata"))
        self.frequency.setText(_translate("Dialog", "Frequency"))
        self.pronunciation.setText(_translate("Dialog", "Pronunciation"))
        self.syllable_count.setText(_translate("Dialog", "Syllable Count"))
        self.parts_of_speech.setText(_translate("Dialog", "Parts of speech"))
        self.definition.setText(_translate("Dialog", "Definition"))
        self.english_spanish.setItemText(0, _translate("Dialog", "English"))
        self.english_spanish.setItemText(1, _translate("Dialog", "Spanish"))

    def load_param(self, params):
        self.english_spanish.setCurrentIndex(params[0])
        if len(params[1]) > 0:
            for i in params[1]:
                self.param[i].click()

    def parameters(self):
        self.identifier = self.english_spanish.currentIndex()
        self.indices = [i for i, x in enumerate(self.param) if x.isChecked()]
        self.parameter_selection = []
        self.parameter_selection.append(self.identifier)
        self.parameter_selection.append(self.indices)
        return self.parameter_selection
