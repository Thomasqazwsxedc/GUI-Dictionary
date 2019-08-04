import urllib
import requests
import json
from pandas import DataFrame

from PyQt5 import QtCore, QtGui, QtWidgets
from .dictionary import Ui_Dialog
from .more_info import Information_Ui_Dialog
from .parameters import Param_Ui_Dialog
from .about import About_Ui_Dialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(40, 20, 521, 411))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.main = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.main.setContentsMargins(0, 0, 0, 0)
        self.main.setObjectName("main")
        self.control = QtWidgets.QHBoxLayout()
        self.control.setObjectName("control")
        self.selection = QtWidgets.QVBoxLayout()
        self.selection.setObjectName("selection")
        self.parameter = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.parameter.setObjectName("parameter")
        self.selection.addWidget(self.parameter)
        self.meaning = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.meaning.setObjectName("meaning")
        self.selection.addWidget(self.meaning)
        self.pronunciation = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.pronunciation.setObjectName("pronunciation")
        self.selection.addWidget(self.pronunciation)
        self.spelling = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.spelling.setObjectName("spelling")
        self.selection.addWidget(self.spelling)
        self.relation = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.relation.setCheckable(True)
        self.relation.setChecked(False)
        self.relation.setAutoRepeat(False)
        self.relation.setObjectName("relation")
        self.selection.addWidget(self.relation)
        self.rel_type = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.rel_type.setEnabled(False)
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
        self.selection.addWidget(self.rel_type)
        self.more_info = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.more_info.setEnabled(True)
        self.more_info.setObjectName("more_info")
        self.selection.addWidget(self.more_info)
        self.additional_parameters = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.additional_parameters.setObjectName("additional_parameters")
        self.selection.addWidget(self.additional_parameters)
        self.control.addLayout(self.selection)
        self.input = QtWidgets.QVBoxLayout()
        self.input.setObjectName("input")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.word_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.word_label.setObjectName("word_label")
        self.horizontalLayout.addWidget(self.word_label)
        self.autocomplete = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.autocomplete.setObjectName("autocomplete")
        self.horizontalLayout.addWidget(self.autocomplete)
        self.input.addLayout(self.horizontalLayout)
        self.text_field = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.text_field.setObjectName("text_field")
        self.input.addWidget(self.text_field)
        self.dict_search = QtWidgets.QHBoxLayout()
        self.dict_search.setObjectName("dict_search")
        self.dictionary = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.dictionary.setObjectName("dictionary")
        self.dict_search.addWidget(self.dictionary)
        self.search = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.search.setObjectName("search")
        self.dict_search.addWidget(self.search)
        self.input.addLayout(self.dict_search)
        self.result = QtWidgets.QHBoxLayout()
        self.result.setObjectName("result")
        self.maximum_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.maximum_label.setObjectName("maximum_label")
        self.result.addWidget(self.maximum_label)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000)
        self.spinBox.setProperty("value", 100)
        self.spinBox.setObjectName("spinBox")
        self.result.addWidget(self.spinBox)
        self.words_all_switch = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.words_all_switch.setObjectName("words_all_switch")
        self.words_all_switch.addItem("")
        self.words_all_switch.addItem("")
        self.result.addWidget(self.words_all_switch)
        self.about = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.about.setObjectName("about")
        self.result.addWidget(self.about)
        self.input.addLayout(self.result)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.download_mode = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.download_mode.setObjectName("download_mode")
        self.download_mode.addItem("")
        self.download_mode.addItem("")
        self.horizontalLayout_4.addWidget(self.download_mode)
        self.download_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.download_button.setObjectName("download_button")
        self.horizontalLayout_4.addWidget(self.download_button)
        self.input.addLayout(self.horizontalLayout_4)
        self.control.addLayout(self.input)
        self.main.addLayout(self.control)
        self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget_3)
        self.tableView.setObjectName("tableView")
        self.main.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout_GUI = QtWidgets.QAction(MainWindow)
        self.actionAbout_GUI.setObjectName("actionAbout_GUI")
        self.actionNew_Tab = QtWidgets.QAction(MainWindow)
        self.actionNew_Tab.setObjectName("actionNew_Tab")
        self.actionNew_Window = QtWidgets.QAction(MainWindow)
        self.actionNew_Window.setObjectName("actionNew_Window")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionAbout_Python = QtWidgets.QAction(MainWindow)
        self.actionAbout_Python.setObjectName("actionAbout_Python")
        self.actionAbout_Dictionary = QtWidgets.QAction(MainWindow)
        self.actionAbout_Dictionary.setObjectName("actionAbout_Dictionary")

        self.functions()
        self.data = []
        self.model = QtGui.QStandardItemModel()
        self.param_selection = [0, []]
        self.metadata_list = ['Definition', 'Parts of speech', 'Syllable count', 'Pronunciation', 'Word frequency']
        self.metadata = ['d', 'p', 's', 'r', 'f']
        self.dictionary_words = open('source/text.txt').read().split()
        self.completer = QtWidgets.QCompleter(self.dictionary_words)

        self.mode_map = {
            'required': {
                'Meaning': 'ml',
                'Pronunciation': 'sl',
                'Spelling': 'sp',
                'Relation': [
                    'jja',  # Popular nouns modified by the given adjective, per Google Books Ngrams	gradual → increase
                    'jjb',  # Popular adjectives used to modify the given noun, per Google Books Ngrams	beach → sandy
                    'syn',  # Synonyms (words contained within the same WordNet synset)	ocean → sea
                    'trg',  # "Triggers" - words associated with the query word in the same piece of text	cow → milking
                    'ant',  # Antonyms (per WordNet)	late → early
                    'spc',  # "Kind of" (direct hypernyms, per WordNet)	gondola → boat
                    'gen',  # "More general than" (direct hyponyms, per WordNet)	boat → gondola
                    'com',  # "Comprises" (direct holonyms, per WordNet)	car → accelerator
                    'par',  # "Part of" (direct meronyms, per WordNet)	trunk → tree
                    'bga',  # Frequent followers (w′ such that P(w′|w) ≥ 0.001, per Google Books Ngrams)	wreak → havoc
                    'bgb',
                    # Frequent predecessors (w′ such that P(w|w′) ≥ 0.001, per Google Books Ngrams)	havoc → wreak
                    'rhy',  # Rhymes ("perfect" rhymes, per RhymeZone)	spade → aid
                    'nry',  # Approximate rhymes (per RhymeZone)	forest → chorus
                    'hom',  # Homophones (sound-alike words)	course → coarse
                    'cns'  # Consonant match	sample → simple
                ]},
            'optional': {
                'Identifier': 'v',
                'Topic words': 'topic',
                # An optional hint to the system about the theme of the document being written. Results will be skewed toward these topics. At most 5 words can be specified. Space or comma delimited. Nouns work best.
                'Left context': 'lc',
                # An optional hint to the system about the word that appears immediately to the left of the target word in a sentence. (At this time, only a single word may be specified.)
                'Right context': 'rc',
                # An optional hint to the system about the word that appears immediately to the right of the target word in a sentence. (At this time, only a single word may be specified.)
                'Maximum': 'max',  # Maximum number of results to return, not to exceed 1000. (default: 100)
                'Metadata': {'Definitions': 'd',
                             'Parts of speech': 'p',
                             'Syllable count': 's',
                             'Pronunciation': 'r',
                             'Word frequency': 'f'
                             }
            }
        }

        self.retranslateUi(MainWindow)
        self.relation.clicked['bool'].connect(self.rel_type.setEnabled)
        self.meaning.clicked['bool'].connect(self.rel_type.setDisabled)
        self.pronunciation.clicked['bool'].connect(self.rel_type.setDisabled)
        self.spelling.clicked['bool'].connect(self.rel_type.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dictionary"))
        self.parameter.setText(_translate("MainWindow", "Parameter"))
        self.meaning.setText(_translate("MainWindow", "Meaning"))
        self.pronunciation.setText(_translate("MainWindow", "Pronunciation"))
        self.spelling.setText(_translate("MainWindow", "Spelling"))
        self.relation.setText(_translate("MainWindow", "Relation"))
        self.rel_type.setItemText(0, _translate("MainWindow", "Adjective → Noun"))
        self.rel_type.setItemText(1, _translate("MainWindow", "Noun → Adjective"))
        self.rel_type.setItemText(2, _translate("MainWindow", "Synonyms"))
        self.rel_type.setItemText(3, _translate("MainWindow", "Triggers"))
        self.rel_type.setItemText(4, _translate("MainWindow", "Antonyms"))
        self.rel_type.setItemText(5, _translate("MainWindow", "Hypernyms"))
        self.rel_type.setItemText(6, _translate("MainWindow", "Hyponyms"))
        self.rel_type.setItemText(7, _translate("MainWindow", "Holonyms"))
        self.rel_type.setItemText(8, _translate("MainWindow", "Meronyms"))
        self.rel_type.setItemText(9, _translate("MainWindow", "Frequent Followers"))
        self.rel_type.setItemText(10, _translate("MainWindow", "Frequent Predecessors"))
        self.rel_type.setItemText(11, _translate("MainWindow", "Perfect Rhymes"))
        self.rel_type.setItemText(12, _translate("MainWindow", "Approximate Rhymes"))
        self.rel_type.setItemText(13, _translate("MainWindow", "Homophones"))
        self.rel_type.setItemText(14, _translate("MainWindow", "Consonant Match"))
        self.more_info.setText(_translate("MainWindow", "More Information"))
        self.additional_parameters.setText(_translate("MainWindow", "Additional Parameters"))
        self.word_label.setText(_translate("MainWindow", "Enter a word:"))
        self.autocomplete.setText(_translate("MainWindow", "Autocomplete"))
        self.text_field.setPlaceholderText(_translate("MainWindow", "Word"))
        self.dictionary.setText(_translate("MainWindow", "Dictionary"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.maximum_label.setText(_translate("MainWindow", "Maximum"))
        self.words_all_switch.setItemText(0, _translate("MainWindow", "Words"))
        self.words_all_switch.setItemText(1, _translate("MainWindow", "All"))
        self.about.setText(_translate("MainWindow", "About"))
        self.download_mode.setItemText(0, _translate("MainWindow", "Original"))
        self.download_mode.setItemText(1, _translate("MainWindow", "CSV"))
        self.download_button.setText(_translate("MainWindow", "Download"))
        self.actionAbout_GUI.setText(_translate("MainWindow", "About Dictionary"))
        self.actionNew_Tab.setText(_translate("MainWindow", "New Tab"))
        self.actionNew_Window.setText(_translate("MainWindow", "New Window"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionAbout_Python.setText(_translate("MainWindow", "About Python"))
        self.actionAbout_Dictionary.setText(_translate("MainWindow", "About Dictionary"))

    def functions(self):
        self.autocomplete.clicked.connect(self.auto_complete_function)
        self.more_info.clicked.connect(self.on_info_button_click)
        self.dictionary.clicked.connect(self.on_dictionary_button_click)
        self.search.clicked.connect(self.on_search_button_click)
        self.additional_parameters.clicked.connect(self.on_additional_parameters_click)
        self.download_button.clicked.connect(self.on_download_button_click)
        self.about.clicked.connect(self.on_about_click)

    def on_info_button_click(self):
        self.info_dialog = QtWidgets.QDialog()
        self.info_dialog.ui = Information_Ui_Dialog()
        self.info_dialog.ui.setupUi(self.info_dialog)
        self.info_dialog.show()
        self.info_dialog.exec_()

    def on_dictionary_button_click(self):
        if len(self.text_field.text()) > 0:
            self.dictionary_dialog = QtWidgets.QDialog()
            self.dictionary_dialog.ui = Ui_Dialog()
            self.dictionary_dialog.ui.setupUi(self.dictionary_dialog)
            self.dictionary_dialog.ui.display_content(self.text_field.text().lower())
            self.dictionary_dialog.show()
            self.dictionary_dialog.exec_()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText('Please enter a word')
            msg.exec()

    def on_search_button_click(self):
        if len(self.text_field.text()) > 0:
            if True not in [self.meaning.isChecked(), self.pronunciation.isChecked(),
                            self.spelling.isChecked(), self.relation.isChecked()]:
                msg = QtWidgets.QMessageBox()
                msg.setText('Please select a parameter')
                msg.exec()
            else:
                api = 'https://api.datamuse.com/words?'
                required_params = self.mode_map['required']
                if self.mode_parse() != 3:
                    key = \
                        [required_params['Meaning'], required_params['Pronunciation'], required_params['Spelling']][
                            self.mode_parse()]
                else:
                    rel_type = required_params['Relation']
                    key = 'rel_' + rel_type[self.rel_type.currentIndex()]

                word = self.text_field.text()
                url = api + urllib.parse.urlencode({key: word})
                if len(self.param_selection[1]) != 0:
                    metadata = ''
                    for i in self.param_selection[1]:
                        metadata += self.metadata[i]
                    url += '&md=%s' % metadata
                url += '&max=%s' % str(self.spinBox.value())
                dict_identifier = {0: '', 1: '&v=es'}
                url += dict_identifier[self.param_selection[0]]
                self.data = requests.get(url).json()
                if len(self.data) != 0:
                    self.table_function(self.data)
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setText('No Matches')
                    msg.exec()

        else:
            msg = QtWidgets.QMessageBox()
            msg.setText('Please enter a word')
            msg.exec()

    def mode_parse(self):
        try:
            return [self.meaning.isChecked(), self.pronunciation.isChecked(),
                    self.spelling.isChecked(), self.relation.isChecked()].index(True)
        except ValueError:
            pass

    def table_function(self, data):
        self.model.clear()
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # dpsrf
        self.labels = ['Word']
        word, definition, parts_of_speech, syllable, pronunciation, frequency = [], [], [], [], [], []
        if self.param_selection[1]:
            for i in self.param_selection[1]:
                self.labels.append(self.metadata_list[i])
        for i in data:
            word.append(i['word'])
            if 0 in self.param_selection[1]:
                try:
                    definition.append('\n'.join(i['defs']))
                except KeyError:
                    definition.append(None)
            if 1 in self.param_selection[1]:
                temp = []
                for j in i['tags']:
                    if 'pron:' not in j and 'f:' not in j:
                        temp.append(j)
                parts_of_speech.append(', '.join(temp))
            if 2 in self.param_selection[1]:
                syllable.append(i['numSyllables'])
            if 3 in self.param_selection[1]:
                pronunciation.append([j for j in i['tags'] if 'pron:' in j][0][5:])
            if 4 in self.param_selection[1]:
                frequency.append([j for j in i['tags'] if 'f:' in j][0][2:])

        if self.param_selection[1]:
            string = 'word, '
            _temp = []
            temp_list = ['definition', 'parts_of_speech', 'syllable', 'pronunciation', 'frequency']
            for i in temp_list:
                if eval(i):
                    _temp.append(i)
            string += ', '.join(_temp)
            data_model = list(zip(eval(string)))
            self.model.setRowCount(len(data))
            self.model.setColumnCount(1 + len(self.param_selection[1]))
            for i in range(len(data_model)):
                for j in range(len(data_model[i][0])):
                    item = QtGui.QStandardItem(str(data_model[i][0][j]))
                    self.model.setItem(j, i, item)
        else:
            self.model.setColumnCount(1)
            self.model.setRowCount(len(word))
            for i in range(len(word)):
                item = QtGui.QStandardItem(word[i])
                self.model.setItem(i, 0, item)
        self.model.setHorizontalHeaderLabels(self.labels)
        self.tableView.setModel(self.model)

        self.tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)

        font = QtGui.QFont("Open Sans", 14)
        self.tableView.setFont(font)
        # self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.resizeColumnsToContents()
        self.tableView.setSortingEnabled(True)

    def spinBox_properties(self):
        if 0 in self.param_selection[1]:
            if self.spinBox.value() > 200:
                self.spinBox.setValue(200)
            self.spinBox.setMaximum(200)
        else:
            self.spinBox.setMaximum(1000)

    def auto_complete_function(self):
        if self.autocomplete.isChecked():
            self.text_field.setCompleter(self.completer)
        else:
            self.text_field.setCompleter(QtWidgets.QCompleter())

    def on_additional_parameters_click(self):
        self.additional_param_dialog = QtWidgets.QDialog()
        self.additional_param_dialog.ui = Param_Ui_Dialog()
        self.additional_param_dialog.ui.setupUi(self.additional_param_dialog)
        self.additional_param_dialog.ui.load_param(self.param_selection)
        self.additional_param_dialog.ui.buttonBox.accepted.connect(self.save_data)
        self.additional_param_dialog.show()
        self.additional_param_dialog.exec_()

    def save_data(self):
        self.param_selection = self.additional_param_dialog.ui.parameters()
        self.spinBox_properties()

    def on_download_button_click(self):
        if self.data:
            download_modes = {0: 'download_original', 1: 'download_csv'}
            self.file_path = str(QtWidgets.QFileDialog.getSaveFileName(self.download_button,'Save File','./data'))
            eval('self.%s()' % download_modes[self.download_mode.currentIndex()])
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText('No data available')
            msg.exec()

    def download_original(self):
        with open(str(self.file_path[2:self.file_path.index('\'', 3)] + '.json'), 'w') as outfile:
            json.dump(self.data, outfile)

    def download_csv(self):
        file = self.file_path[2:self.file_path.index('\'', 3)] + '.csv'
        df_list = []
        for i in range(self.model.rowCount()):
            tmp = []
            for j in range(self.model.columnCount()):
                tmp.append(self.model.item(i, j).text())
            df_list.append(tmp)
        DataFrame(df_list, columns=self.labels).to_csv(file, index=False)

    def on_about_click(self):
        self.about_dialog = QtWidgets.QDialog()
        self.about_dialog.ui = About_Ui_Dialog()
        self.about_dialog.ui.setupUi(self.about_dialog)
        self.about_dialog.show()
        self.about_dialog.exec_()
