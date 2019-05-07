# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 400)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: #F8F8FF;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    border: none;\n"
"    spacing: 0px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(images/unpressed.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(images/pressed.png);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: #87CEFA;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4682B4;\n"
"    border-style: inset;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setObjectName("layout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 557, 113))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_shape = QtWidgets.QPushButton(self.centralwidget)
        self.add_shape.setObjectName("add_shape")
        self.verticalLayout.addWidget(self.add_shape)
        self.delete_shape = QtWidgets.QPushButton(self.centralwidget)
        self.delete_shape.setObjectName("delete_shape")
        self.verticalLayout.addWidget(self.delete_shape)
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setStyleSheet("")
        self.save.setObjectName("save")
        self.verticalLayout.addWidget(self.save)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.layout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.layout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.incorrect_share = QtWidgets.QVBoxLayout()
        self.incorrect_share.setObjectName("incorrect_share")
        self.horizontalLayout.addLayout(self.incorrect_share)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem4)
        self.recognize = QtWidgets.QPushButton(self.centralwidget)
        self.recognize.setMaximumSize(QtCore.QSize(100, 16777215))
        self.recognize.setObjectName("recognize")
        self.verticalLayout_5.addWidget(self.recognize)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.correct_share = QtWidgets.QVBoxLayout()
        self.correct_share.setObjectName("correct_share")
        self.horizontalLayout.addLayout(self.correct_share)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setText("")
        self.status.setObjectName("status")
        self.horizontalLayout.addWidget(self.status)
        spacerItem8 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.layout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.layout)
        spacerItem9 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_shape.setText(_translate("MainWindow", "Add Shape"))
        self.delete_shape.setText(_translate("MainWindow", "Delete Shape"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.recognize.setText(_translate("MainWindow", "Recognize"))

