# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        MainWindow.setMinimumSize(QtCore.QSize(320, 300))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.icon = QtWidgets.QLabel(self.centralwidget)
        self.icon.setMinimumSize(QtCore.QSize(0, 100))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("icon.png"))
        self.icon.setScaledContents(False)
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.icon.setObjectName("icon")
        self.verticalLayout.addWidget(self.icon)
        self.url_textedit = QtWidgets.QTextEdit(self.centralwidget)
        self.url_textedit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.url_textedit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.url_textedit.setPlaceholderText("Rutube URL:")
        self.url_textedit.setObjectName("url_textedit")
        self.verticalLayout.addWidget(self.url_textedit)
        self.file_label = QtWidgets.QLabel(self.centralwidget)
        self.file_label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.file_label.setObjectName("file_label")
        self.verticalLayout.addWidget(self.file_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file_textedit = QtWidgets.QTextEdit(self.centralwidget)
        self.file_textedit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.file_textedit.setDocumentTitle("")
        self.file_textedit.setOverwriteMode(False)
        self.file_textedit.setPlaceholderText("")
        self.file_textedit.setObjectName("file_textedit")
        self.horizontalLayout.addWidget(self.file_textedit)
        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_button.setMaximumSize(QtCore.QSize(16777215, 30))
        self.browse_button.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.browse_button.setObjectName("browse_button")
        self.horizontalLayout.addWidget(self.browse_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.World))
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.download_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_button.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.download_button.setObjectName("download_button")
        self.verticalLayout.addWidget(self.download_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rutube Downloader"))
        self.file_label.setText(_translate("MainWindow", "Path to directory:"))
        self.browse_button.setText(_translate("MainWindow", "Browse"))
        self.comboBox.setToolTip(_translate("MainWindow", "Video quality"))
        self.download_button.setText(_translate("MainWindow", "Download"))
