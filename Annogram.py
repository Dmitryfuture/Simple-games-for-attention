# -*- coding: utf-8 -*-


import random
from random import randint

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QEventLoop, QTimer


class RunTimer(QThread):
    thread_timer = QtCore.pyqtSignal()

    def run(self):
        self.thread_timer.emit()


class Ui_MainWindow(object):

    def __init__(self):
        self.ALL_RIGHT_ANSWER = 0
        self.ALL_NOT_RIGHT_ANSWER = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 616)
        font = QtGui.QFont()
        font.setKerning(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(21, 170, 148);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.right_or_not_lable = QtWidgets.QLabel(self.centralwidget)
        self.right_or_not_lable.setGeometry(QtCore.QRect(60, 70, 190, 31))
        self.right_or_not_lable.setStyleSheet('color: rgb(0, 0, 0);'
                                              'font: 10pt "MS Shell Dlg 2"')
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 0, 611, 61))
        self.label.setStyleSheet("background-color: rgb(26, 202, 202);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.time_label_name = QtWidgets.QLabel(self.centralwidget)
        self.time_label_name.setGeometry(QtCore.QRect(300, 7, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.time_label_name.setFont(font)
        self.time_label_name.setStyleSheet("background-color: rgb(26, 202, 202);")
        self.time_label_name.setObjectName("time_label_name")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(291, 23, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.time_label.setFont(font)
        self.time_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time_label.setStyleSheet("background-color: rgb(26, 202, 202);")
        self.time_label.setObjectName("time_label")
        self.level_label_name = QtWidgets.QLabel(self.centralwidget)
        self.level_label_name.setGeometry(QtCore.QRect(419, 7, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.level_label_name.setFont(font)
        self.level_label_name.setStyleSheet("background-color: rgb(26, 202, 202);")
        self.level_label_name.setObjectName("level_label_name")
        self.level_label = QtWidgets.QLabel(self.centralwidget)
        self.level_label.setGeometry(QtCore.QRect(437, 23, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.level_label.setFont(font)
        self.level_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.level_label.setStyleSheet("background-color: rgb(26, 202, 202);")
        self.level_label.setObjectName("level_label")
        self.score_level_label = QtWidgets.QLabel(self.centralwidget)
        self.score_level_label.setGeometry(QtCore.QRect(533, 23, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.score_level_label.setFont(font)
        self.score_level_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.score_level_label.setStyleSheet("background-color: rgb(26, 202, 202);")
        self.score_level_label.setObjectName("score_level_label")
        self.score_label_name = QtWidgets.QLabel(self.centralwidget)
        self.score_label_name.setGeometry(QtCore.QRect(550, 7, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.score_label_name.setFont(font)
        self.score_label_name.setStyleSheet("background-color: rgb(26, 202, 202);")
        self.score_label_name.setObjectName("score_label_name")
        self.factor_label_name = QtWidgets.QLabel(self.centralwidget)
        self.factor_label_name.setGeometry(QtCore.QRect(700, 7, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.factor_label_name.setFont(font)
        self.factor_label_name.setStyleSheet("background-color: rgb(26, 202, 202);")
        self.factor_label_name.setObjectName("factor_label_name")
        self.factor_label = QtWidgets.QLabel(self.centralwidget)
        self.factor_label.setGeometry(QtCore.QRect(740, 23, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.factor_label.setFont(font)
        self.factor_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.factor_label.setStyleSheet("background-color: rgb(26, 202, 202);")
        self.factor_label.setObjectName("factor_label")
        self.word_1_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.word_1_pushButton.setGeometry(QtCore.QRect(60, 420, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.word_1_pushButton.setFont(font)
        self.word_1_pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.word_1_pushButton.setObjectName("word_1_pushButton")
        self.word_2_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.word_2_pushButton.setGeometry(QtCore.QRect(450, 420, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(18)
        font.setBold(True)
        self.word_2_pushButton.setFont(font)
        self.word_2_pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.word_2_pushButton.setObjectName("word_2_pushButton")
        self.word_3_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.word_3_pushButton.setGeometry(QtCore.QRect(60, 510, 331, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(18)
        self.word_3_pushButton.setFont(font)
        self.word_3_pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.word_3_pushButton.setObjectName("word_3_pushButton")
        self.word_4_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.word_4_pushButton.setGeometry(QtCore.QRect(450, 510, 331, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(18)
        self.word_4_pushButton.setFont(font)
        self.word_4_pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.word_4_pushButton.setObjectName("word_4_pushButton")
        self.start_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.start_pushButton.setGeometry(QtCore.QRect(60, 10, 141, 51))
        self.start_pushButton.setStyleSheet("background-color: rgb(26, 202, 202);\n"
                                            "font: 75 14pt \"MS Shell Dlg 2\";\n"
                                            "color: rgb(255, 255, 255);")
        self.start_pushButton.setObjectName("pushButton")
        self.basic_word = QtWidgets.QPushButton(self.centralwidget)
        self.basic_word.setGeometry(QtCore.QRect(60, 110, 721, 271))
        self.basic_word.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.basic_word.setFont(font)
        self.basic_word.setStyleSheet("color: rgb(255, 255, 255);")
        self.basic_word.setObjectName("basic_word")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.list_buttons = [self.word_1_pushButton, self.word_2_pushButton, self.word_3_pushButton,
                             self.word_4_pushButton]

        self.alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'К', 'З', 'И', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
                         'Х', 'Ч', 'Щ', 'Ш', 'Ы', 'Л']

        self.words = ['ПРИМЕР', 'ЛИМОНАД', 'ВОДОПАД', 'ДОМОСЕД', 'ФОНТАН', 'ПИРАМИДА', 'ПЕРЕВАЛ', 'КОСМОНАВТ',
                      'ТЕЛЕГРАФ', 'ПРОГРАММА', 'ИМПРОВИЗАЦИЯ', 'АНАРХИЯ', 'ТЕЛЕВИЗОР', 'АКСАКАЛ', 'КАСКАДЕР',
                      'ЗВЕЗДОЛЕТ', 'САМОЛЕТ', 'ПОРЯДОЧНОСТЬ', 'АВТОМОБИЛЬ', 'ПЕРЕСТРОЙКА', 'СУДОСТРОЕНИЕ', 'ДОМОВОЙ',
                      'АЛАБАЙ', 'НОУТБУК', 'КОМПЬЮТЕР', 'САНТЕХНИК', 'ВЕНТИЛЯТОР', 'ЗАМЕЩЕНИЕ', 'НАТЮРМОРТ', 'АБДУКЦИЯ',
                      'ЛАБИРИНТ', 'ЛАКФИОЛЬ', 'ЛАТУННЫЙ', 'АКЦИОНЕР', 'БАГАЖНИК', 'БАЛЕРИНА', 'АРХАИЧНЫЙ', 'ЛЯМОЧНИК',
                      'АВТОРУЧКА', 'БУТАФОРИЯ', 'ВЕСТИБЮЛЬ', 'ГЕОГРАФИЯ', 'ГОДОВЩИНА', 'ДВОРЕЦКИЙ', 'ЦИФЕРБЛАТ',
                      'ЕЖЕВИЧНИК', 'ЖАРТОВАТЬ', 'ЖЕМАНСТВО', 'ЖИМОЛОСТЬ', 'ИЗВИНЕНИЕ', 'ИМЕНИННИК', 'ИЗЫСКАНИЕ',
                      'КОНФЕРАНС', 'ЛИЦЕМЕРИЕ', 'ЛОКОМОТИВ', 'ПАДЧЕРИЦА', 'СКУПЕРДЯЙ', 'УДАЧЛИВЫЙ', 'ФАЛЬШИВЫЙ',
                      'ЦИРЮЛЬНИК', 'ЭФФЕКТНЫЙ', 'АТЛЕТИЗМ', 'АВАНПОСТ', 'АВАНГАРД', 'АПОЛОГЕТ', 'БЕССИЛИЕ', 'ВЕТРЕНЫЙ',
                      'ДИЛЕТАНТ', 'ДОБЛЕСТЬ', 'ЕДИНЕНИЕ', 'ЖИВОТНОЕ', 'ИЗОЛЯТОР', 'ИЗМОРОЗЬ', 'ИНЕРТНЫЙ', 'ИНСТИТУТ',
                      'КОНДИЦИЯ', 'ЛЕСИСТЫЙ', 'МОДЕЛИСТ', 'МОШЕННИК', 'НЕПОСЕДА', 'ОККУПАНТ', 'ОТДУШИНА', 'ПОДЛОВКА',
                      'ПИЛИГРИМ', 'РУТИННЫЙ', 'ТЕПЛУШКА', 'УЯЗВИМЫЙ', 'ФЛАГШТОК', 'ФОЛЬКЛЕР', 'ФАНФАРОН', 'ФАРАОН',
                      'ХОЛОСТЯК', 'ЦИНИЧНЫЙ', 'ЦИСТЕРНА', 'МЕДОВИК', 'ЦИТАДЕЛЬ', 'ШЕВЕЛЮРА', 'ЩУПАЛЬЦА', 'ЭКСПОНАТ',
                      'АПРИОРИ', 'АЖИОТАЖ', 'АЛЛЕГРО', 'АНТУРАЖ', 'ВЕТРИЛО', 'ГЕРОИЗМ', 'ЕХИДНЫЙ', 'ЖЕРЕБЕЦ', 'ЗРИТЕЛЬ',
                      'ИНТРИГА', 'КАЗУИСТ', 'АППАРАТ', 'СТОЛИЦА', 'ПЕРЕНОСКА', 'МОНОЛОГ', 'ОБИТЕЛЬ', 'ОКОЛИЦА',
                      'ПРОФИЛЬ', 'РЕВИЗОР', 'РВАНИНА', 'СКУДНЫЙ', 'СТАТНЫЙ', 'ТАКСИСТ', 'ФОРМУЛА', 'ТАБЛИЦА', 'ФЕНОМЕН',
                      'ЦИНОВКА', 'ШТАБЕЛЬ', 'ЭМБЛЕМА', 'ЭСТРАДА', 'ЮМОРИСТ', 'ЯГНЕНОК', 'ЯЩЕРИЦА', 'ЯРМАРКА']

        self.function()

        self.signal_timer = RunTimer()
        self.signal_timer.thread_timer.connect(self.run_time)
        self.minus_second = QEventLoop()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анаграммы"))
        self.time_label_name.setText(_translate("MainWindow", "Время"))
        self.time_label.setText(_translate("MainWindow", "00:60"))
        self.level_label_name.setText(_translate("MainWindow", "Уровень"))
        self.level_label.setText(_translate("MainWindow", "0"))
        self.score_level_label.setText(_translate("MainWindow", "0"))
        self.score_label_name.setText(_translate("MainWindow", "Очки"))
        self.factor_label_name.setText(_translate("MainWindow", "Коэффициент"))
        self.factor_label.setText(_translate("MainWindow", "х1"))
        self.start_pushButton.setText(_translate("MainWindow", "Старт"))

    def function(self):
        self.start_pushButton.clicked.connect(lambda: (self.start(), self.launch_threads()))

    def create_basic_word(self):
        """ Создает главное слово, которое будет изменено """
        word = random.choice(self.words)
        self.basic_word.setText(word)
        self.words.pop(self.words.index(word))

    def create_anogramms(self):
        """ Создает измененные слова """

        word_for_change = self.basic_word.text()
        for but in self.list_buttons:
            but.setText(
                word_for_change.replace(
                    random.choice(word_for_change),
                    random.choice(self.alphabet),
                    randint(1, 2))
            )
        random.choice(self.list_buttons).setText(word_for_change)

        # Проверка на условие, что если есть 2 одиннаковых слова в выборе ответов, идет новая генерация ответов
        for _ in self.list_buttons:
            if [i.text() for i in self.list_buttons].count(_.text()) >= 2:
                return self.create_anogramms()

        # К кнопкам привязываем функию по определению правильного ответа
        for but in self.list_buttons:
            but.clicked.connect(lambda ch, button_object=but: self.text_clicked_button(button_object.text()))

    def text_clicked_button(self, text):
        """ Проверяет совпал ли текст нажатой кнопки с базовым словом """

        if text == self.basic_word.text():
            self.right_or_not_lable.setText("Верно!")
            self.score_level_label.setText(
                str(int(self.score_level_label.text()) + 100 * int(self.factor_label.text()[1])))
            self.ALL_RIGHT_ANSWER += 1
            if self.ALL_RIGHT_ANSWER in range(0, 200, 10):
                self.level_label.setText(str(int(self.level_label.text()) + 1))
            if self.ALL_RIGHT_ANSWER in range(0, 105, 15):
                try:
                    self.factor_label.setText('x' + str(int(self.factor_label.text()[1]) + 1))
                except Exception as err:
                    print(err)
        else:
            self.right_or_not_lable.setText("Не верно(")
            self.ALL_NOT_RIGHT_ANSWER += 1
            if self.score_level_label.text() == '0':
                pass
            else:
                self.score_level_label.setText(str(int(self.score_level_label.text()) - 100))

            if self.ALL_NOT_RIGHT_ANSWER in range(0, 200, 10):
                if self.level_label.text() != '0':
                    self.level_label.setText(str(int(self.level_label.text()) - 1))
        # Разрываем связи в кнопках выбора ответа
        for i in self.list_buttons:
            i.disconnect()

        self.start()

    def start(self):
        """ Функция генерации нового слова """
        self.start_pushButton.setEnabled(False)
        self.create_basic_word()
        self.create_anogramms()

    def run_time(self):
        """ Заупск таймера """

        for i in range(61):
            sec = 60 - i
            self.time_label.setText(f'00:{str(sec)}')
            if sec < 10:
                self.time_label.setText(f'00:0{str(sec)}')
            if sec == 0:
                self.start_pushButton.setEnabled(True)
                for i in self.list_buttons:
                    i.disconnect()
                self.right_or_not_lable.setText(f'Ваш результат: {self.score_level_label.text()}')
                self.level_label.setText('0')
                self.score_level_label.setText('0')
                self.factor_label.setText('x1')
                self.ALL_NOT_RIGHT_ANSWER = 0
                self.ALL_RIGHT_ANSWER = 0
            QTimer.singleShot(1000, self.minus_second.quit)
            self.minus_second.exec_()

    def launch_threads(self):
        self.signal_timer.start()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
