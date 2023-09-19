# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\VsCodeProjects\PSKO\range.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Range(object):
    def setupUi(self, Range):
        Range.setObjectName("Range")
        Range.resize(700, 700)
        self.graphicsView = QtWidgets.QGraphicsView(Range)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.graphicsView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(Range)
        QtCore.QMetaObject.connectSlotsByName(Range)

    def retranslateUi(self, Range):
        _translate = QtCore.QCoreApplication.translate
        Range.setWindowTitle(_translate("Range", "Form"))

