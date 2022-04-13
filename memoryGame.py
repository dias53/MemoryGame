from concurrent.futures import thread

from PyQt5 import QtCore, QtGui, QtWidgets
import time

from PyQt5.QtWidgets import QButtonGroup


class Ui_MainWindow(object):
    fastest_time = 0
    pairs_left = 12

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progress_label = QtWidgets.QLabel(self.centralwidget)
        self.progress_label.setGeometry(QtCore.QRect(130, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Amiri Quran")
        font.setPointSize(14)
        self.progress_label.setFont(font)
        self.progress_label.setObjectName("progress_label")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(130, 120, 81, 81))
        self.Button_1.setObjectName("Button_1")
        self.Button_1.pressed.connect(self.button1_press)
        self.Button_1.released.connect(self.button1_release)
        self.Button_1.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(220, 120, 81, 81))
        self.Button_2.setObjectName("Button_2")
        self.Button_2.pressed.connect(self.button2_press)
        self.Button_2.released.connect(self.button2_release)
        self.Button_2.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(310, 120, 81, 81))
        self.Button_3.setObjectName("Button_3")
        self.Button_3.pressed.connect(self.button3_press)
        self.Button_3.released.connect(self.button3_release)
        self.Button_3.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(400, 120, 81, 81))
        self.Button_4.setObjectName("Button_4")
        self.Button_4.pressed.connect(self.button4_press)
        self.Button_4.released.connect(self.button4_release)
        self.Button_4.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(490, 120, 81, 81))
        self.Button_5.setObjectName("Button_5")
        self.Button_5.pressed.connect(self.button5_press)
        self.Button_5.released.connect(self.button5_release)
        self.Button_5.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(580, 120, 81, 81))
        self.Button_6.setObjectName("Button_6")
        self.Button_6.pressed.connect(self.button6_press)
        self.Button_6.released.connect(self.button6_release)
        self.Button_6.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_10 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_10.setGeometry(QtCore.QRect(400, 210, 81, 81))
        self.Button_10.setObjectName("Button_10")
        self.Button_10.pressed.connect(self.button10_press)
        self.Button_10.released.connect(self.button10_release)
        self.Button_10.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(130, 210, 81, 81))
        self.Button_7.setObjectName("Button_7")
        self.Button_7.pressed.connect(self.button7_press)
        self.Button_7.released.connect(self.button7_release)
        self.Button_7.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(310, 210, 81, 81))
        self.Button_9.setObjectName("Button_9")
        self.Button_9.pressed.connect(self.button9_press)
        self.Button_9.released.connect(self.button9_release)
        self.Button_9.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_12 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_12.setGeometry(QtCore.QRect(580, 210, 81, 81))
        self.Button_12.setObjectName("Button_12")
        self.Button_12.pressed.connect(self.button12_press)
        self.Button_12.released.connect(self.button12_release)
        self.Button_12.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(220, 210, 81, 81))
        self.Button_8.setObjectName("Button_8")
        self.Button_8.pressed.connect(self.button8_press)
        self.Button_8.released.connect(self.button8_release)
        self.Button_8.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_11 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_11.setGeometry(QtCore.QRect(490, 210, 81, 81))
        self.Button_11.setObjectName("Button_11")
        self.Button_11.pressed.connect(self.button11_press)
        self.Button_11.released.connect(self.button11_release)
        self.Button_11.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_16 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_16.setGeometry(QtCore.QRect(400, 300, 81, 81))
        self.Button_16.setObjectName("Button_16")
        self.Button_16.pressed.connect(self.button16_press)
        self.Button_16.released.connect(self.button16_release)
        self.Button_16.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_13 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_13.setGeometry(QtCore.QRect(130, 300, 81, 81))
        self.Button_13.setObjectName("Button_13")
        self.Button_13.pressed.connect(self.button13_press)
        self.Button_13.released.connect(self.button13_release)
        self.Button_13.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_15 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_15.setGeometry(QtCore.QRect(310, 300, 81, 81))
        self.Button_15.setObjectName("Button_15")
        self.Button_15.pressed.connect(self.button15_press)
        self.Button_15.released.connect(self.button15_release)
        self.Button_15.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_18 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_18.setGeometry(QtCore.QRect(580, 300, 81, 81))
        self.Button_18.setObjectName("Button_18")
        self.Button_18.pressed.connect(self.button18_press)
        self.Button_18.released.connect(self.button18_release)
        self.Button_18.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_14 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_14.setGeometry(QtCore.QRect(220, 300, 81, 81))
        self.Button_14.setObjectName("Button_14")
        self.Button_14.pressed.connect(self.button14_press)
        self.Button_14.released.connect(self.button14_release)
        self.Button_14.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_17 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_17.setGeometry(QtCore.QRect(490, 300, 81, 81))
        self.Button_17.setObjectName("Button_17")
        self.Button_17.pressed.connect(self.button17_press)
        self.Button_17.released.connect(self.button17_release)
        self.Button_17.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_22 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_22.setGeometry(QtCore.QRect(400, 390, 81, 81))
        self.Button_22.setObjectName("Button_22")
        self.Button_22.pressed.connect(self.button22_press)
        self.Button_22.released.connect(self.button22_release)
        self.Button_22.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_19 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_19.setGeometry(QtCore.QRect(130, 390, 81, 81))
        self.Button_19.setObjectName("Button_19")
        self.Button_19.pressed.connect(self.button19_press)
        self.Button_19.released.connect(self.button19_release)
        self.Button_19.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_21 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_21.setGeometry(QtCore.QRect(310, 390, 81, 81))
        self.Button_21.setObjectName("Button_21")
        self.Button_21.pressed.connect(self.button21_press)
        self.Button_21.released.connect(self.button21_release)
        self.Button_21.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_24 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_24.setGeometry(QtCore.QRect(580, 390, 81, 81))
        self.Button_24.setObjectName("Button_24")
        self.Button_24.pressed.connect(self.button24_press)
        self.Button_24.released.connect(self.button24_release)
        self.Button_24.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_20 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_20.setGeometry(QtCore.QRect(220, 390, 81, 81))
        self.Button_20.setObjectName("Button_20")
        self.Button_20.pressed.connect(self.button20_press)
        self.Button_20.released.connect(self.button20_release)
        self.Button_20.setStyleSheet("border-image : url(world.jpeg);")
        self.Button_23 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_23.setGeometry(QtCore.QRect(490, 390, 81, 81))
        self.Button_23.setObjectName("Button_23")
        self.Button_23.pressed.connect(self.button23_press)
        self.Button_23.released.connect(self.button23_release)
        self.Button_23.setStyleSheet("border-image : url(world.jpeg);")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(110, 50, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.hint_label = QtWidgets.QLabel(self.centralwidget)
        self.hint_label.setGeometry(QtCore.QRect(370, 490, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Amiri Quran")
        font.setPointSize(10)
        self.hint_label.setFont(font)
        self.hint_label.setObjectName("hint_label")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(610, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Amiri Quran")
        font.setPointSize(14)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btn_grp = QButtonGroup()
        self.btn_grp.setExclusive(True)
        self.btn_grp.addButton(self.Button_1)
        self.btn_grp.addButton(self.Button_2)
        self.btn_grp.addButton(self.Button_3)
        self.btn_grp.addButton(self.Button_4)
        self.btn_grp.addButton(self.Button_5)
        self.btn_grp.addButton(self.Button_6)
        self.btn_grp.addButton(self.Button_7)
        self.btn_grp.addButton(self.Button_8)
        self.btn_grp.addButton(self.Button_9)
        self.btn_grp.addButton(self.Button_10)
        self.btn_grp.addButton(self.Button_11)
        self.btn_grp.addButton(self.Button_12)
        self.btn_grp.addButton(self.Button_13)
        self.btn_grp.addButton(self.Button_14)
        self.btn_grp.addButton(self.Button_15)
        self.btn_grp.addButton(self.Button_16)
        self.btn_grp.addButton(self.Button_17)
        self.btn_grp.addButton(self.Button_18)
        self.btn_grp.addButton(self.Button_19)
        self.btn_grp.addButton(self.Button_20)
        self.btn_grp.addButton(self.Button_21)
        self.btn_grp.addButton(self.Button_22)
        self.btn_grp.addButton(self.Button_23)
        self.btn_grp.addButton(self.Button_24)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Memory Game"))
        self.progress_label.setText(_translate("MainWindow", "Progress"))
        self.Button_1.setText(_translate("MainWindow", ""))
        self.Button_2.setText(_translate("MainWindow", ""))
        self.Button_3.setText(_translate("MainWindow", ""))
        self.Button_4.setText(_translate("MainWindow", ""))
        self.Button_5.setText(_translate("MainWindow", ""))
        self.Button_6.setText(_translate("MainWindow", ""))
        self.Button_10.setText(_translate("MainWindow", ""))
        self.Button_7.setText(_translate("MainWindow", ""))
        self.Button_9.setText(_translate("MainWindow", ""))
        self.Button_12.setText(_translate("MainWindow", ""))
        self.Button_8.setText(_translate("MainWindow", ""))
        self.Button_11.setText(_translate("MainWindow", ""))
        self.Button_16.setText(_translate("MainWindow", ""))
        self.Button_13.setText(_translate("MainWindow", ""))
        self.Button_15.setText(_translate("MainWindow", ""))
        self.Button_18.setText(_translate("MainWindow", ""))
        self.Button_14.setText(_translate("MainWindow", ""))
        self.Button_17.setText(_translate("MainWindow", ""))
        self.Button_22.setText(_translate("MainWindow", ""))
        self.Button_19.setText(_translate("MainWindow", ""))
        self.Button_21.setText(_translate("MainWindow", ""))
        self.Button_24.setText(_translate("MainWindow", ""))
        self.Button_20.setText(_translate("MainWindow", ""))
        self.Button_23.setText(_translate("MainWindow", ""))
        self.hint_label.setText(_translate("MainWindow", f"{self.pairs_left} pairs are left to find"))

    def button1_press(self):
        self.Button_1.setStyleSheet("border-image : url(arg.png);")
    def button1_release(self):
        self.Button_1.setStyleSheet("border-image : url(world.jpeg);")
    def button2_press(self):
        self.Button_2.setStyleSheet("border-image : url(be.png);")
    def button2_release(self):
        self.Button_2.setStyleSheet("border-image : url(world.jpeg);")
    def button3_press(self):
        self.Button_3.setStyleSheet("border-image : url(arg.png);")
    def button3_release(self):
        self.Button_3.setStyleSheet("border-image : url(world.jpeg);")
    def button4_press(self):
        self.Button_4.setStyleSheet("border-image : url(brazil.jpg);")
    def button4_release(self):
        self.Button_4.setStyleSheet("border-image : url(world.jpeg);")
    def button5_press(self):
        self.Button_5.setStyleSheet("border-image : url(be.png);")
    def button5_release(self):
        self.Button_5.setStyleSheet("border-image : url(world.jpeg);")
    def button6_press(self):
        self.Button_6.setStyleSheet("border-image : url(neth.png);")
    def button6_release(self):
        self.Button_6.setStyleSheet("border-image : url(world.jpeg);")
    def button7_press(self):
        self.Button_7.setStyleSheet("border-image : url(brazil.jpg);")
    def button7_release(self):
        self.Button_7.setStyleSheet("border-image : url(world.jpeg);")
    def button8_press(self):
        self.Button_8.setStyleSheet("border-image : url(kz.png);")
    def button8_release(self):
        self.Button_8.setStyleSheet("border-image : url(world.jpeg);")
    def button9_press(self):
        self.Button_9.setStyleSheet("border-image : url(hun.jpg);")
    def button9_release(self):
        self.Button_9.setStyleSheet("border-image : url(world.jpeg);")
    def button10_press(self):
        self.Button_10.setStyleSheet("border-image : url(germany.jpg);")
    def button10_release(self):
        self.Button_10.setStyleSheet("border-image : url(world.jpeg);")
    def button11_press(self):
        self.Button_11.setStyleSheet("border-image : url(neth.png);")
    def button11_release(self):
        self.Button_11.setStyleSheet("border-image : url(world.jpeg);")
    def button12_press(self):
        self.Button_12.setStyleSheet("border-image : url(france.jpg);")
    def button12_release(self):
        self.Button_12.setStyleSheet("border-image : url(world.jpeg);")
    def button13_press(self):
        self.Button_13.setStyleSheet("border-image : url(Turkey.jpg);")
    def button13_release(self):
        self.Button_13.setStyleSheet("border-image : url(world.jpeg);")
    def button14_press(self):
        self.Button_14.setStyleSheet("border-image : url(uk.jpg);")
    def button14_release(self):
        self.Button_14.setStyleSheet("border-image : url(world.jpeg);")
    def button15_press(self):
        self.Button_15.setStyleSheet("border-image : url(uk.jpg);")
    def button15_release(self):
        self.Button_15.setStyleSheet("border-image : url(world.jpeg);")
    def button16_press(self):
        self.Button_16.setStyleSheet("border-image : url(spain.jpg);")
    def button16_release(self):
        self.Button_16.setStyleSheet("border-image : url(world.jpeg);")
    def button17_press(self):
        self.Button_17.setStyleSheet("border-image : url(germany.jpg);")
    def button17_release(self):
        self.Button_17.setStyleSheet("border-image : url(world.jpeg);")
    def button18_press(self):
        self.Button_18.setStyleSheet("border-image : url(usa.jpg);")
    def button18_release(self):
        self.Button_18.setStyleSheet("border-image : url(world.jpeg);")
    def button19_press(self):
        self.Button_19.setStyleSheet("border-image : url(hun.jpg);")
    def button19_release(self):
        self.Button_19.setStyleSheet("border-image : url(world.jpeg);")
    def button20_press(self):
        self.Button_20.setStyleSheet("border-image : url(usa.jpg);")
    def button20_release(self):
        self.Button_20.setStyleSheet("border-image : url(world.jpeg);")
    def button21_press(self):
        self.Button_21.setStyleSheet("border-image : url(spain.jpg);")
    def button21_release(self):
        self.Button_21.setStyleSheet("border-image : url(world.jpeg);")
    def button22_press(self):
        self.Button_22.setStyleSheet("border-image : url(kz.png);")
    def button22_release(self):
        self.Button_22.setStyleSheet("border-image : url(world.jpeg);")
    def button23_press(self):
        self.Button_23.setStyleSheet("border-image : url(neth.png);")
    def button23_release(self):
        self.Button_23.setStyleSheet("border-image : url(world.jpeg);")
    def button24_press(self):
        self.Button_24.setStyleSheet("border-image : url(Turkey.jpg);")
    def button24_release(self):
        self.Button_24.setStyleSheet("border-image : url(world.jpeg);")
    





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())