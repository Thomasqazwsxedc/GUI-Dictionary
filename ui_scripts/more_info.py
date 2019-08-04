from PyQt5 import QtCore, QtGui, QtWidgets

_translate = QtCore.QCoreApplication.translate


class Information_Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 480)
        self.content = QtWidgets.QTabWidget(Dialog)
        self.content.setGeometry(QtCore.QRect(50, 30, 441, 411))
        self.content.setObjectName("content")
        self.meaning = QtWidgets.QWidget()
        self.meaning.setObjectName("meaning")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.meaning)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 381, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontal_spacer = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.horizontal_spacer.setContentsMargins(0, 0, 0, 0)
        self.horizontal_spacer.setObjectName("horizontal_spacer")
        self.meaning_title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.meaning_title_label.setFont(font)
        self.meaning_title_label.setObjectName("meaning_title_label")
        self.horizontal_spacer.addWidget(self.meaning_title_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_spacer.addItem(spacerItem)
        self.meaning_description_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.meaning_description_label.setFont(font)
        self.meaning_description_label.setObjectName("meaning_description_label")
        self.horizontal_spacer.addWidget(self.meaning_description_label)
        self.meaning_textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.meaning_textBrowser.setObjectName("meaning_textBrowser")
        self.horizontal_spacer.addWidget(self.meaning_textBrowser)
        self.content.addTab(self.meaning, "")
        self.pronunciation = QtWidgets.QWidget()
        self.pronunciation.setObjectName("pronunciation")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.pronunciation)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 30, 381, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.pronunciation_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.pronunciation_layout.setContentsMargins(0, 0, 0, 0)
        self.pronunciation_layout.setObjectName("pronunciation_layout")
        self.pronunciation_title_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pronunciation_title_label.setFont(font)
        self.pronunciation_title_label.setObjectName("pronunciation_title_label")
        self.pronunciation_layout.addWidget(self.pronunciation_title_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.pronunciation_layout.addItem(spacerItem1)
        self.pronunciation_description_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pronunciation_description_label.setFont(font)
        self.pronunciation_description_label.setObjectName("pronunciation_description_label")
        self.pronunciation_layout.addWidget(self.pronunciation_description_label)
        self.pronunciation_textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.pronunciation_textBrowser.setObjectName("pronunciation_textBrowser")
        self.pronunciation_layout.addWidget(self.pronunciation_textBrowser)
        self.content.addTab(self.pronunciation, "")
        self.spelling = QtWidgets.QWidget()
        self.spelling.setObjectName("spelling")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.spelling)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 30, 381, 321))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.spelling_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.spelling_layout.setContentsMargins(0, 0, 0, 0)
        self.spelling_layout.setObjectName("spelling_layout")
        self.spelling_title_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.spelling_title_label.setFont(font)
        self.spelling_title_label.setObjectName("spelling_title_label")
        self.spelling_layout.addWidget(self.spelling_title_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.spelling_layout.addItem(spacerItem2)
        self.spelling_description_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.spelling_description_label.setFont(font)
        self.spelling_description_label.setObjectName("spelling_description_label")
        self.spelling_layout.addWidget(self.spelling_description_label)
        self.spelling_textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.spelling_textBrowser.setObjectName("spelling_textBrowser")
        self.spelling_layout.addWidget(self.spelling_textBrowser)
        self.content.addTab(self.spelling, "")
        self.relation = QtWidgets.QWidget()
        self.relation.setObjectName("relation")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.relation)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(30, 30, 401, 321))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.relation_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.relation_layout.setContentsMargins(0, 0, 0, 0)
        self.relation_layout.setObjectName("relation_layout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.description_radio = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.description_radio.setChecked(True)
        self.description_radio.setObjectName("description_radio")
        self.horizontalLayout_2.addWidget(self.description_radio)
        self.parameter_radio = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.parameter_radio.setObjectName("parameter_radio")
        self.horizontalLayout_2.addWidget(self.parameter_radio)
        self.rel_type = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.rel_type.setEnabled(True)
        self.rel_type.setObjectName("rel_type")
        self.rel_type.addItem("")
        self.rel_type.addItem("")
        self.rel_type.addItem("")
        self.rel_type.addItem("")
        self.rel_type.addItem("")
        self.rel_type.addItem("")
        self.rel_type.addItem("")
        self.rel_type.addItem("")
        self.rel_type.addItem("")
        self.rel_type.addItem("")
        self.rel_type.addItem("")
        self.rel_type.addItem("")
        self.rel_type.addItem("")
        self.rel_type.addItem("")
        self.rel_type.addItem("")
        self.horizontalLayout_2.addWidget(self.rel_type)
        self.relation_layout.addLayout(self.horizontalLayout_2)
        self.relation_textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.relation_textBrowser.setObjectName("relation_textBrowser")
        self.relation_layout.addWidget(self.relation_textBrowser)
        self.checkBox = QtWidgets.QCheckBox(self.relation)
        self.checkBox.setGeometry(QtCore.QRect(-60, 130, 71, 18))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.content.addTab(self.relation, "")

        self.rel_modes = ['Adjective → Noun', 'Noun → Adjective',
                          'Synonyms', 'Triggers',
                          'Antonyms', 'Hypernyms',
                          'Hyponyms', 'Holonyms',
                          'Meronyms', 'Frequent Followers',
                          'Frequent Predecessors',
                          'Perfect Rhymes', 'Approximate Rhymes',
                          'Homophones', 'Consonant Match']
        self.rel_modes_code = ['jja', 'jjb', 'syn', 'trg', 'ant', 'spc', 'gen', 'com', 'par', 'bga', 'bgb', 'rhy',
                               'nry', 'hom', 'cns']
        self.rel_modes_description = ['Popular nouns modified by the given adjective, per Google Books Ngrams',
                                      'Popular adjectives used to modify the given noun, per Google Books Ngrams',
                                      'Synonyms (words contained within the same WordNet synset)',
                                      '"Triggers" (words that are statistically associated with the query word in the same piece of text.)',
                                      'Antonyms (per WordNet)', '“Kind of" (direct hypernyms, per WordNet)',
                                      '“More general than" (direct hyponyms, per WordNet)',
                                      '“Comprises" (direct holonyms, per WordNet)',
                                      '"Part of" (direct meronyms, per WordNet)',
                                      'Frequent followers (w′ such that P(w′|w) ≥ 0.001, per Google Books Ngrams)',
                                      'Frequent predecessors (w′ such that P(w|w′) ≥ 0.001, per Google Books Ngrams)',
                                      'Rhymes ("perfect" rhymes, per RhymeZone)', 'Approximate rhymes (per RhymeZone)',
                                      'Homophones (sound-alike words)', 'Consonant match'
                                      ]
        self.rel_modes_example = ['gradual → increase', 'beach → sandy', 'ocean → sea', 'cow → milking', 'late → early',
                                  'gondola → boat', 'boat → gondola', 'car → accelerator', 'trunk → tree',
                                  'wreak → havoc', 'havoc → wreak', 'spade → aid', 'forest → chorus', 'course → coarse',
                                  'sample → simple']

        self.text = self.parse_info(0)
        self.parameter_is_active = False
        self.functions()

        self.retranslateUi(Dialog)
        self.content.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Information"))
        self.meaning_title_label.setText(_translate("Dialog", "Meaning (ml)"))
        self.meaning_description_label.setText(_translate("Dialog", "Description"))
        self.meaning_textBrowser.setHtml(_translate("Dialog",
                                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\'; font-size:18pt; font-weight:600; color:#000000;\">Means like</span><span style=\" font-family:\'Open Sans\'; font-size:18pt; color:#000000;\"> constraint: require that the results have a meaning related to this string value, which can be any word or sequence of words. (This is effectively the </span><a href=\"https://onelook.com/reverse-dictionary.shtml\"><span style=\" font-family:\'Open Sans\'; font-size:18pt; text-decoration: underline; color:#0000ff;\">reverse dictionary</span></a><span style=\" font-family:\'Open Sans\'; font-size:18pt; color:#000000;\"> feature of OneLook.)</span></p>\n"
                                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Open Sans\'; font-size:18pt; color:#000000;\"><br /></p></body></html>"))
        self.content.setTabText(self.content.indexOf(self.meaning), _translate("Dialog", "Meaning"))
        self.pronunciation_title_label.setText(_translate("Dialog", "Pronunciation (sl)"))
        self.pronunciation_description_label.setText(_translate("Dialog", "Description"))
        self.pronunciation_textBrowser.setHtml(_translate("Dialog",
                                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                          "<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
                                                          "<tr>\n"
                                                          "<td>\n"
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\'; font-size:18pt; font-weight:600;\">Sounds like</span><span style=\" font-family:\'Open Sans\'; font-size:18pt;\"> constraint: require that the results are pronounced similarly to this string of characters. (If the string of characters doesn\'t have a known pronunciation, the system will make its best guess using a text-to-phonemes algorithm.)</span></p></td></tr></table>\n"
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.content.setTabText(self.content.indexOf(self.pronunciation), _translate("Dialog", "Pronunciation"))
        self.spelling_title_label.setText(_translate("Dialog", "Spelling (sp)"))
        self.spelling_description_label.setText(_translate("Dialog", "Description"))
        self.spelling_textBrowser.setHtml(_translate("Dialog",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                     "<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
                                                     "<tr>\n"
                                                     "<td>\n"
                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\'; font-size:18pt; font-weight:600;\">Spelled like</span><span style=\" font-family:\'Open Sans\'; font-size:18pt;\"> constraint: require that the results are spelled similarly to this string of characters, or that they match this </span><a href=\"https://www.onelook.com/?c=faq#patterns\"><span style=\" font-family:\'Open Sans\'; font-size:18pt; text-decoration: underline; color:#0000ff;\">wildcard pattern</span></a><span style=\" font-family:\'Open Sans\'; font-size:18pt;\">. A pattern can include any combination of alphanumeric characters, spaces, and two reserved characters that represent placeholders — </span><span style=\" font-family:\'Monaco\'; font-size:18pt;\">*</span><span style=\" font-family:\'Open Sans\'; font-size:18pt;\"> (matches any number of characters) and </span><span style=\" font-family:\'Monaco\'; font-size:18pt;\">?</span><span style=\" font-family:\'Open Sans\'; font-size:18pt;\"> (matches exactly one character).</span></p></td></tr></table></body></html>"))
        self.content.setTabText(self.content.indexOf(self.spelling), _translate("Dialog", "Spelling"))
        self.description_radio.setText(_translate("Dialog", "Description"))
        self.parameter_radio.setText(_translate("Dialog", "Parameters"))
        self.rel_type.setItemText(0, _translate("Dialog", "Adjective → Noun"))
        self.rel_type.setItemText(1, _translate("Dialog", "Noun → Adjective"))
        self.rel_type.setItemText(2, _translate("Dialog", "Synonyms"))
        self.rel_type.setItemText(3, _translate("Dialog", "Triggers"))
        self.rel_type.setItemText(4, _translate("Dialog", "Antonyms"))
        self.rel_type.setItemText(5, _translate("Dialog", "Hypernyms"))
        self.rel_type.setItemText(6, _translate("Dialog", "Hyponyms"))
        self.rel_type.setItemText(7, _translate("Dialog", "Holonyms"))
        self.rel_type.setItemText(8, _translate("Dialog", "Meronyms"))
        self.rel_type.setItemText(9, _translate("Dialog", "Frequent Followers"))
        self.rel_type.setItemText(10, _translate("Dialog", "Frequent Predecessors"))
        self.rel_type.setItemText(11, _translate("Dialog", "Perfect Rhymes"))
        self.rel_type.setItemText(12, _translate("Dialog", "Approximate Rhymes"))
        self.rel_type.setItemText(13, _translate("Dialog", "Homophones"))
        self.rel_type.setItemText(14, _translate("Dialog", "Consonant Match"))
        self.relation_textBrowser.setHtml(_translate("Dialog",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                     "<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
                                                     "<tr>\n"
                                                     "<td>\n"
                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\'; font-size:18pt; font-weight:600;\">Related word</span><span style=\" font-family:\'Open Sans\'; font-size:18pt;\"> constraints: require that the results, when paired with the word in this parameter, are in a predefined lexical relation indicated by [code]. Any number of these parameters may be specified any number of times. An assortment of semantic, phonetic, and corpus-statistics-based relations are available. At this time, these relations are available for English-language vocabularies only. </span></p></td></tr></table></body></html>"))
        self.content.setTabText(self.content.indexOf(self.relation), _translate("Dialog", "Relation"))

    def functions(self):
        self.description_radio.clicked.connect(self.on_description_radio_click)
        self.parameter_radio.clicked.connect(self.on_parameter_radio_click)
        self.rel_type.currentIndexChanged.connect(self.on_rel_type_activate)

    def on_description_radio_click(self):
        self.parameter_is_active = False
        self.relation_textBrowser.setHtml(_translate("Dialog",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                     "<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
                                                     "<tr>\n"
                                                     "<td>\n"
                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\'; font-size:18pt; font-weight:600;\">Related word</span><span style=\" font-family:\'Open Sans\'; font-size:18pt;\"> constraints: require that the results, when paired with the word in this parameter, are in a predefined lexical relation indicated by [code]. Any number of these parameters may be specified any number of times. An assortment of semantic, phonetic, and corpus-statistics-based relations are available. At this time, these relations are available for English-language vocabularies only. </span></p></td></tr></table></body></html>"))

    def on_parameter_radio_click(self):
        self.parameter_is_active = True
        self.display_info()

    def on_rel_type_activate(self):
        self.text = self.parse_info(self.rel_type.currentIndex())
        if self.parameter_is_active:
            self.display_info()

    def display_info(self):
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setFamily('Open Sans')
        self.relation_textBrowser.setFont(font)
        self.relation_textBrowser.setText(self.text)

    def parse_info(self, index):
        return '%s (%s)\n\nDescription:\n - %s\n\nExample:\n - %s' % \
               (self.rel_modes[index],
                self.rel_modes_code[index],
                self.rel_modes_description[index],
                self.rel_modes_example[index])
