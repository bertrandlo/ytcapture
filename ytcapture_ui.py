# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ytcapture.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TessReader(object):
    def setupUi(self, TessReader):
        TessReader.setObjectName("TessReader")
        TessReader.resize(640, 480)
        TessReader.setMinimumSize(QtCore.QSize(640, 480))
        TessReader.setAcceptDrops(False)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TessReader)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.graphicsView = QtWidgets.QGraphicsView(TessReader)
        self.graphicsView.setObjectName("graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)
        self.comboBox = QtWidgets.QComboBox(TessReader)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(TessReader)
        QtCore.QMetaObject.connectSlotsByName(TessReader)

    def retranslateUi(self, TessReader):
        _translate = QtCore.QCoreApplication.translate
        TessReader.setWindowTitle(_translate("TessReader", "Form"))

