# -*- coding: utf-8 -*-

from random import choice, randint

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QEventLoop, QTimer


class RunTimer(QThread):
    thread_timer = QtCore.pyqtSignal()

    def run(self):
        self.thread_timer.emit()


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(255, 141, 48);")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 341, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.basic_widget = QtWidgets.QWidget(self.centralwidget)
        self.basic_widget.setGeometry(QtCore.QRect(15, 70, 440, 550))
        self.basic_widget.setObjectName("basic_widget")
        self.basic_widget.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                        "border-style: outset;\n"
                                        "border-width: 0px;\n"
                                        "border-radius: 15px;\n")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(490, 250, 61, 31))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(20)
        self.spinBox.setMaximum(45)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 220, 210, 22))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.button_New_game = QtWidgets.QPushButton(self.centralwidget)
        self.button_New_game.setGeometry(QtCore.QRect(490, 330, 231, 41))
        self.button_New_game.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "font: 75 11pt \"MS Shell Dlg 2\";")
        self.button_New_game.setObjectName("pushButton")
        self.Stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.Stop_button.setGeometry(QtCore.QRect(490, 390, 231, 41))
        self.Stop_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "font: 75 11pt \"MS Shell Dlg 2\";\n"
                                       "background-color: rgb(255, 0, 0);")
        self.Stop_button.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.lable_timer = QtWidgets.QLabel(self.centralwidget)
        self.lable_timer.setGeometry(QtCore.QRect(490, 70, 210, 22))
        self.lable_timer.setObjectName("lable_timer")
        self.lable_timer.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")

        self.timer = QtWidgets.QLabel(self.centralwidget)
        self.timer.setGeometry(QtCore.QRect(490, 95, 210, 25))
        self.timer.setObjectName("timer")
        self.timer.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")

        self.lable_time_end = QtWidgets.QLabel(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.name_button = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                            26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]

        self.buttons = []
        self.new_list = []
        self.previos = 1

        self.signal_timer = RunTimer()
        self.signal_timer.thread_timer.connect(self.run_time)
        self.minus_second = QEventLoop()

        self.count = 0
        self.button_New_game.clicked.connect(lambda: (self.create_button(self.spinBox.value()), self.launch_threads()))
        self.Stop_button.clicked.connect(lambda: self.stop())
        self.STOP = False
        self.Stop_button.setEnabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Клик Клик"))
        self.label_2.setText(_translate("MainWindow", "Выберите уровень"))
        self.button_New_game.setText(_translate("MainWindow", "Новая игра"))
        self.Stop_button.setText(_translate("MainWindow", "Сбросить"))
        self.lable_timer.setText(_translate("MainWindow", "Время:"))
        self.timer.setText(_translate("MainWindow", "00:60"))

    def create_button(self, quantity):
        self.spinBox.setEnabled(False)
        self.button_New_game.setEnabled(False)
        self.Stop_button.setEnabled(True)
        self.STOP = False
        self.lable_time_end.clear()
        for i in self.buttons:  # Закрытие старых кнопок и очистка списка
            i.close()
        self.buttons.clear()
        self.new_list = self.name_button[0:quantity]
        if quantity < 30:
            x = 15
            y = 15
        elif quantity >= 30:
            x = 10
            y = 10
        for i in range(quantity):  # Создание списка с объектами кнопками
            if quantity < 30:
                size_x = 57
                size_y = 57
                factor = randint(1, 3)
                inter = 59
            elif quantity >= 30:
                size_x = 50
                size_y = 50
                factor = randint(1, 2)
                inter = 53
            button = QtWidgets.QPushButton(self.basic_widget)
            button.setGeometry(QtCore.QRect(x, y, size_x, size_y))
            self.buttons.append(button)
            x += inter * factor
            if quantity < 30:
                if x >= 406:
                    x = 15
                    y += 59
                if y >= 513:
                    self.create_button(quantity)
            elif quantity >= 30:
                if x >= 390:
                    x = 10
                    y += 53
                if y >= 530:
                    self.create_button(quantity)

        try:  # Присваивание рандомной нумерации кнопкам
            for but in self.buttons:
                name = choice(self.new_list)
                but.setText(str(name))
                but.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                  "border-width: 0px;"
                                  "border-color: rgb(255, 255, 255);\n"
                                  "color: rgb(170, 85, 0);\n"
                                  "border-radius: 9px;"
                                  "background-color: rgb(255, 255, 255);\n")
                self.new_list.pop(self.new_list.index(name))
                but.clicked.connect(lambda ch, button_object=but: self.close(button_object))
                but.show()
        except Exception:
            pass

    def close(self, but):
        if int(but.text()) == self.previos:
            but.close()
            self.previos += 1
            self.count += 1
            if self.previos > len(self.buttons):
                self.previos = 1
                self.spinBox.setEnabled(True)
                self.spinBox.setValue(self.spinBox.value() + 2)
                self.create_button(self.spinBox.value())
                self.spinBox.setEnabled(False)
        elif int(but.text()) != self.previos:
            self.previos = 1
            self.spinBox.setEnabled(True)
            self.spinBox.setValue(self.spinBox.value() - 2)
            self.create_button(self.spinBox.value())
            self.spinBox.setEnabled(False)

    def run_time(self):
        self.count = 0
        for i in range(61):
            if self.STOP is False:
                sec = 60 - i
                self.timer.setText(f'00:{str(sec)}')
                if sec < 10:
                    self.timer.setText(f'00:0{str(sec)}')
                if sec == 0:
                    for i in self.buttons:
                        i.setEnabled(False)
                    self.spinBox.setEnabled(True)
                    self.lable_time_end.setGeometry(QtCore.QRect(490, 130, 225, 22))
                    self.lable_time_end.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
                    self.lable_time_end.setText(f'Время вышло, ваш счет - {self.count}')
                    self.lable_time_end.show()
                    self.button_New_game.setEnabled(True)
                    self.Stop_button.setEnabled(False)
                QTimer.singleShot(1000, self.minus_second.quit)
                self.minus_second.exec_()
            elif self.STOP:
                break

    def launch_threads(self):
        self.signal_timer.start()

    def stop(self):
        self.spinBox.setEnabled(True)
        self.STOP = True
        self.previos = 1
        self.Stop_button.setEnabled(False)
        self.button_New_game.setEnabled(True)
        self.timer.setText('00:60')
        self.signal_timer.exit()
        for elem in self.buttons:
            elem.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
