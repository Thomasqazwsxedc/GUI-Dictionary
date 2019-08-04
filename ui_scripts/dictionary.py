import requests
import io

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from urllib.request import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 480)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 461, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setObjectName("vertical_layout")
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.word = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.word.setFont(font)
        self.word.setText("")
        self.word.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.word.setWordWrap(True)
        self.word.setObjectName("word")
        self.horizontal_layout.addWidget(self.word)
        self.pronunciation = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pronunciation.setFont(font)
        self.pronunciation.setText("")
        self.pronunciation.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.pronunciation.setObjectName("pronunciation")
        self.horizontal_layout.addWidget(self.pronunciation)
        self.vertical_layout.addLayout(self.horizontal_layout)
        self.content = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.content.setObjectName("content")
        self.vertical_layout.addWidget(self.content)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dictionary"))

    def display_content(self, text):
        response = requests.get('https://owlbot.info/api/v3/dictionary/%s' % text,
                                headers={'Authorization': 'Token 1135c11d4b69229fa3b343a43f71e44130415996'}).json()
        if type(response) == list:
            self.word.setText(text)
            self.content.setText('Word does not exist.')
        else:
            definitions = response['definitions'][0]
            self.word.setText(response['word'])
            self.pronunciation.setText(response['pronunciation'])
            parts_of_speech = definitions['type']
            definition = definitions['definition']
            example = definitions['example']
            image = definitions['image_url']

            string = '<p style="font-size:18px;"><strong>Parts of speech: </strong>%s</p><p style="font-size:18px;"><strong>Definition: </strong>%s</p>' % (parts_of_speech, definition)

            if example is not None:
                example = example.split()
                example[0] = example[0].capitalize()
                string += '<p style="font-size:18px;"><strong>Example: </strong>%s</p>' % ' '.join(example)

            if image is not None:
                headers = {'User-Agent': 'Chrome/41.0.2228.0'}
                reg_url = image
                req = Request(url=reg_url, headers=headers)
                img = Image.open(io.BytesIO(urlopen(req).read()))
                img.save('source/image.jpg')

                string += '<br><img src="source/image.jpg">'

            self.content.setHtml(string)
