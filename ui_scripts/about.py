from PyQt5 import QtCore, QtWidgets


class About_Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(541, 440)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(50, 30, 451, 371))
        self.tabWidget.setObjectName("tabWidget")
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.about_textBrowser = QtWidgets.QTextBrowser(self.main)
        self.about_textBrowser.setGeometry(QtCore.QRect(20, 50, 405, 280))
        self.about_textBrowser.setObjectName("about_textBrowser")
        self.tabWidget.addTab(self.main, "")
        self.instructions = QtWidgets.QWidget()
        self.instructions.setObjectName("instructions")
        self.instructions_textBrowser = QtWidgets.QTextBrowser(self.instructions)
        self.instructions_textBrowser.setGeometry(QtCore.QRect(20, 50, 405, 280))
        self.instructions_textBrowser.setObjectName("instructions_textBrowser")
        self.tabWidget.addTab(self.instructions, "")
        self.contacts = QtWidgets.QWidget()
        self.contacts.setObjectName("contacts")
        self.contacts_textBrowser = QtWidgets.QTextBrowser(self.contacts)
        self.contacts_textBrowser.setGeometry(QtCore.QRect(20, 50, 405, 280))
        self.contacts_textBrowser.setObjectName("contacts_textBrowser")
        self.tabWidget.addTab(self.contacts, "")

        self.functions()

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), _translate("Dialog", "About"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.instructions), _translate("Dialog", "Instructions"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contacts), _translate("Dialog", "Contacts"))

    def functions(self):
        self.about_textBrowser.setHtml(
            """<h2>Dictionary App</h2><p style="font-size:18px;">Self designed dictionary app.</p><p style="font-size:18px;"><strong>APIs:</strong></p><ol><li style="font-size:18px;"><a href="https://www.datamuse.com/api/">https://www.datamuse.com/api/</a></li><li style="font-size:18px;"><a href="https://owlbot.info">https://owlbot.info</a></li></ol>""")
        self.instructions_textBrowser.setHtml("""
            <p style="font-size:18px;"><strong>Steps (Required): </strong></p>
            <ol><li style="font-size:18px;">Enter word</li><li style="font-size:18px;">Select parameter</li><li style="font-size:18px;">Click “Search” button</li></ol>
            <p style="font-size:18px;"><strong>Steps (Optional):</strong></p>
            <ol><li style="font-size:18px;">Search Dictionary (Click “Dictionary” button)</li><li style="font-size:18px;">Select metadata</li><li style="font-size:18px;">Download data</li></ol>""")
        self.contacts_textBrowser.setHtml(
            '<p style="font-size:18px;"><strong>Github Account:</strong> <a href="https://github.com/Thomasqazwsxedc">https://github.com/Thomasqazwsxedc</a></p><p style="font-size:18px;"><strong>Gmail: </strong> <a href="thomaslin910608@gmail.com">thomaslin910608@gmail.com</a></p><p style="font-size:18px;"><strong>Linkedin: </strong><a href="https://www.linkedin.com/in/thomas-lin-6384a111b/">https://www.linkedin.com/in/thomas-lin-6384a111b/</a></p>')
