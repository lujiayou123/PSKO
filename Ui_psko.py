# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\VsCodeProjects\PSKO\psko.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PSKO(object):
    def setupUi(self, PSKO):
        PSKO.setObjectName("PSKO")
        PSKO.resize(720, 352)
        PSKO.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_leftPalyers = QtWidgets.QTextEdit(PSKO)
        self.textEdit_leftPalyers.setGeometry(QtCore.QRect(140, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.textEdit_leftPalyers.setFont(font)
        self.textEdit_leftPalyers.setObjectName("textEdit_leftPalyers")
        self.label_leftPlayers = QtWidgets.QLabel(PSKO)
        self.label_leftPlayers.setGeometry(QtCore.QRect(30, 40, 81, 16))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_leftPlayers.setFont(font)
        self.label_leftPlayers.setObjectName("label_leftPlayers")
        self.label_totalPlayers = QtWidgets.QLabel(PSKO)
        self.label_totalPlayers.setGeometry(QtCore.QRect(30, 90, 81, 16))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_totalPlayers.setFont(font)
        self.label_totalPlayers.setObjectName("label_totalPlayers")
        self.textEdit_totalPlayers = QtWidgets.QTextEdit(PSKO)
        self.textEdit_totalPlayers.setGeometry(QtCore.QRect(140, 80, 101, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.textEdit_totalPlayers.setFont(font)
        self.textEdit_totalPlayers.setObjectName("textEdit_totalPlayers")
        self.label_startingChips = QtWidgets.QLabel(PSKO)
        self.label_startingChips.setGeometry(QtCore.QRect(30, 140, 81, 16))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_startingChips.setFont(font)
        self.label_startingChips.setObjectName("label_startingChips")
        self.textEdit_startingChips = QtWidgets.QTextEdit(PSKO)
        self.textEdit_startingChips.setGeometry(QtCore.QRect(140, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.textEdit_startingChips.setFont(font)
        self.textEdit_startingChips.setObjectName("textEdit_startingChips")
        self.textEdit_bountyMagnification = QtWidgets.QTextEdit(PSKO)
        self.textEdit_bountyMagnification.setGeometry(QtCore.QRect(140, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.textEdit_bountyMagnification.setFont(font)
        self.textEdit_bountyMagnification.setObjectName("textEdit_bountyMagnification")
        self.textEdit_curPot = QtWidgets.QTextEdit(PSKO)
        self.textEdit_curPot.setGeometry(QtCore.QRect(140, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.textEdit_curPot.setFont(font)
        self.textEdit_curPot.setObjectName("textEdit_curPot")
        self.textEdit_toCall = QtWidgets.QTextEdit(PSKO)
        self.textEdit_toCall.setGeometry(QtCore.QRect(140, 280, 101, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.textEdit_toCall.setFont(font)
        self.textEdit_toCall.setObjectName("textEdit_toCall")
        self.label_bountyMagnification = QtWidgets.QLabel(PSKO)
        self.label_bountyMagnification.setGeometry(QtCore.QRect(30, 190, 91, 16))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_bountyMagnification.setFont(font)
        self.label_bountyMagnification.setObjectName("label_bountyMagnification")
        self.label_curPot = QtWidgets.QLabel(PSKO)
        self.label_curPot.setGeometry(QtCore.QRect(30, 240, 81, 16))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_curPot.setFont(font)
        self.label_curPot.setObjectName("label_curPot")
        self.label_toCall = QtWidgets.QLabel(PSKO)
        self.label_toCall.setGeometry(QtCore.QRect(30, 290, 81, 16))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_toCall.setFont(font)
        self.label_toCall.setObjectName("label_toCall")
        self.label_equity = QtWidgets.QLabel(PSKO)
        self.label_equity.setGeometry(QtCore.QRect(310, 170, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setItalic(True)
        self.label_equity.setFont(font)
        self.label_equity.setObjectName("label_equity")
        self.textBrowser = QtWidgets.QTextBrowser(PSKO)
        self.textBrowser.setGeometry(QtCore.QRect(270, 200, 181, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setObjectName("textBrowser")
        self.calculateButton = QtWidgets.QPushButton(PSKO)
        self.calculateButton.setGeometry(QtCore.QRect(300, 280, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setItalic(True)
        self.calculateButton.setFont(font)
        self.calculateButton.setMouseTracking(False)
        self.calculateButton.setIconSize(QtCore.QSize(16, 16))
        self.calculateButton.setObjectName("calculateButton")
        self.rangeButton = QtWidgets.QPushButton(PSKO)
        self.rangeButton.setGeometry(QtCore.QRect(480, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setItalic(True)
        self.rangeButton.setFont(font)
        self.rangeButton.setMouseTracking(False)
        self.rangeButton.setIconSize(QtCore.QSize(16, 16))
        self.rangeButton.setObjectName("rangeButton")
        self.range_label = QtWidgets.QLabel(PSKO)
        self.range_label.setGeometry(QtCore.QRect(500, 26, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.range_label.setFont(font)
        self.range_label.setObjectName("range_label")
        self.range_label_2 = QtWidgets.QLabel(PSKO)
        self.range_label_2.setGeometry(QtCore.QRect(510, 86, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.range_label_2.setFont(font)
        self.range_label_2.setObjectName("range_label_2")
        self.rangeButton_2 = QtWidgets.QPushButton(PSKO)
        self.rangeButton_2.setGeometry(QtCore.QRect(480, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setItalic(True)
        self.rangeButton_2.setFont(font)
        self.rangeButton_2.setMouseTracking(False)
        self.rangeButton_2.setIconSize(QtCore.QSize(16, 16))
        self.rangeButton_2.setObjectName("rangeButton_2")
        self.rangeButton_3 = QtWidgets.QPushButton(PSKO)
        self.rangeButton_3.setGeometry(QtCore.QRect(480, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setItalic(True)
        self.rangeButton_3.setFont(font)
        self.rangeButton_3.setMouseTracking(False)
        self.rangeButton_3.setIconSize(QtCore.QSize(16, 16))
        self.rangeButton_3.setObjectName("rangeButton_3")
        self.range_label_3 = QtWidgets.QLabel(PSKO)
        self.range_label_3.setGeometry(QtCore.QRect(500, 150, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.range_label_3.setFont(font)
        self.range_label_3.setObjectName("range_label_3")
        self.range_label_4 = QtWidgets.QLabel(PSKO)
        self.range_label_4.setGeometry(QtCore.QRect(510, 210, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setItalic(False)
        self.range_label_4.setFont(font)
        self.range_label_4.setObjectName("range_label_4")
        self.rangeButton_4 = QtWidgets.QPushButton(PSKO)
        self.rangeButton_4.setGeometry(QtCore.QRect(480, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setItalic(True)
        self.rangeButton_4.setFont(font)
        self.rangeButton_4.setMouseTracking(False)
        self.rangeButton_4.setIconSize(QtCore.QSize(16, 16))
        self.rangeButton_4.setObjectName("rangeButton_4")
        self.range_label_5 = QtWidgets.QLabel(PSKO)
        self.range_label_5.setGeometry(QtCore.QRect(500, 270, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.range_label_5.setFont(font)
        self.range_label_5.setObjectName("range_label_5")
        self.rangeButton_5 = QtWidgets.QPushButton(PSKO)
        self.rangeButton_5.setGeometry(QtCore.QRect(480, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setItalic(True)
        self.rangeButton_5.setFont(font)
        self.rangeButton_5.setMouseTracking(False)
        self.rangeButton_5.setIconSize(QtCore.QSize(16, 16))
        self.rangeButton_5.setObjectName("rangeButton_5")
        self.label_against_main_range = QtWidgets.QLabel(PSKO)
        self.label_against_main_range.setGeometry(QtCore.QRect(290, 10, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_against_main_range.setFont(font)
        self.label_against_main_range.setObjectName("label_against_main_range")
        self.textBrowser_range = QtWidgets.QTextBrowser(PSKO)
        self.textBrowser_range.setGeometry(QtCore.QRect(260, 40, 201, 121))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setItalic(True)
        self.textBrowser_range.setFont(font)
        self.textBrowser_range.setObjectName("textBrowser_range")
        self.rangeButton_12 = QtWidgets.QPushButton(PSKO)
        self.rangeButton_12.setGeometry(QtCore.QRect(600, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setItalic(True)
        self.rangeButton_12.setFont(font)
        self.rangeButton_12.setMouseTracking(False)
        self.rangeButton_12.setIconSize(QtCore.QSize(16, 16))
        self.rangeButton_12.setObjectName("rangeButton_12")
        self.range_label_13 = QtWidgets.QLabel(PSKO)
        self.range_label_13.setGeometry(QtCore.QRect(610, 150, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.range_label_13.setFont(font)
        self.range_label_13.setObjectName("range_label_13")
        self.range_label_12 = QtWidgets.QLabel(PSKO)
        self.range_label_12.setGeometry(QtCore.QRect(600, 90, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.range_label_12.setFont(font)
        self.range_label_12.setObjectName("range_label_12")
        self.range_label_11 = QtWidgets.QLabel(PSKO)
        self.range_label_11.setGeometry(QtCore.QRect(610, 30, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.range_label_11.setFont(font)
        self.range_label_11.setObjectName("range_label_11")
        self.range_label_15 = QtWidgets.QLabel(PSKO)
        self.range_label_15.setGeometry(QtCore.QRect(600, 270, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.range_label_15.setFont(font)
        self.range_label_15.setObjectName("range_label_15")
        self.rangeButton_15 = QtWidgets.QPushButton(PSKO)
        self.rangeButton_15.setGeometry(QtCore.QRect(600, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setItalic(True)
        self.rangeButton_15.setFont(font)
        self.rangeButton_15.setMouseTracking(False)
        self.rangeButton_15.setIconSize(QtCore.QSize(16, 16))
        self.rangeButton_15.setObjectName("rangeButton_15")
        self.rangeButton_14 = QtWidgets.QPushButton(PSKO)
        self.rangeButton_14.setGeometry(QtCore.QRect(600, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setItalic(True)
        self.rangeButton_14.setFont(font)
        self.rangeButton_14.setMouseTracking(False)
        self.rangeButton_14.setIconSize(QtCore.QSize(16, 16))
        self.rangeButton_14.setObjectName("rangeButton_14")
        self.range_label_14 = QtWidgets.QLabel(PSKO)
        self.range_label_14.setGeometry(QtCore.QRect(600, 210, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.range_label_14.setFont(font)
        self.range_label_14.setObjectName("range_label_14")
        self.rangeButton_11 = QtWidgets.QPushButton(PSKO)
        self.rangeButton_11.setGeometry(QtCore.QRect(600, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setItalic(True)
        self.rangeButton_11.setFont(font)
        self.rangeButton_11.setMouseTracking(False)
        self.rangeButton_11.setIconSize(QtCore.QSize(16, 16))
        self.rangeButton_11.setObjectName("rangeButton_11")
        self.rangeButton_13 = QtWidgets.QPushButton(PSKO)
        self.rangeButton_13.setGeometry(QtCore.QRect(600, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setItalic(True)
        self.rangeButton_13.setFont(font)
        self.rangeButton_13.setMouseTracking(False)
        self.rangeButton_13.setIconSize(QtCore.QSize(16, 16))
        self.rangeButton_13.setObjectName("rangeButton_13")

        self.retranslateUi(PSKO)
        QtCore.QMetaObject.connectSlotsByName(PSKO)

    def retranslateUi(self, PSKO):
        _translate = QtCore.QCoreApplication.translate
        PSKO.setWindowTitle(_translate("PSKO", "Form"))
        self.textEdit_leftPalyers.setHtml(_translate("PSKO", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'楷体\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_leftPlayers.setText(_translate("PSKO", "剩余玩家"))
        self.label_totalPlayers.setText(_translate("PSKO", "总玩家数"))
        self.label_startingChips.setText(_translate("PSKO", "起始筹码"))
        self.label_bountyMagnification.setText(_translate("PSKO", "赏金倍数"))
        self.label_curPot.setText(_translate("PSKO", "当前底池"))
        self.label_toCall.setText(_translate("PSKO", "需要跟注"))
        self.label_equity.setText(_translate("PSKO", "NeedEquity"))
        self.calculateButton.setText(_translate("PSKO", "Calculate"))
        self.rangeButton.setText(_translate("PSKO", "Solution"))
        self.range_label.setText(_translate("PSKO", "Super Tight"))
        self.range_label_2.setText(_translate("PSKO", "Tight"))
        self.rangeButton_2.setText(_translate("PSKO", "Solution"))
        self.rangeButton_3.setText(_translate("PSKO", "Solution"))
        self.range_label_3.setText(_translate("PSKO", "Standard"))
        self.range_label_4.setText(_translate("PSKO", "Wide"))
        self.rangeButton_4.setText(_translate("PSKO", "Solution"))
        self.range_label_5.setText(_translate("PSKO", "Super Wide"))
        self.rangeButton_5.setText(_translate("PSKO", "Solution"))
        self.label_against_main_range.setText(_translate("PSKO", "Opponent\'s Range"))
        self.rangeButton_12.setText(_translate("PSKO", "Solution"))
        self.range_label_13.setText(_translate("PSKO", "ISO Rejaming"))
        self.range_label_12.setText(_translate("PSKO", "Cold Call Jaming"))
        self.range_label_11.setText(_translate("PSKO", "5bb Jaming"))
        self.range_label_15.setText(_translate("PSKO", "Multiway Three"))
        self.rangeButton_15.setText(_translate("PSKO", "Solution"))
        self.rangeButton_14.setText(_translate("PSKO", "Solution"))
        self.range_label_14.setText(_translate("PSKO", "Multiway Two"))
        self.rangeButton_11.setText(_translate("PSKO", "Solution"))
        self.rangeButton_13.setText(_translate("PSKO", "Solution"))

