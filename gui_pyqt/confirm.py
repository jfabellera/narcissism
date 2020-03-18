# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Confirm(object):
    def setupUi(self, Confirm):
        Confirm.setObjectName("Confirm")
        Confirm.setEnabled(True)
        Confirm.resize(372, 109)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Confirm.sizePolicy().hasHeightForWidth())
        Confirm.setSizePolicy(sizePolicy)
        Confirm.setAcceptDrops(False)
        self.buttonConfirm = QtWidgets.QDialogButtonBox(Confirm)
        self.buttonConfirm.setGeometry(QtCore.QRect(10, 70, 351, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonConfirm.sizePolicy().hasHeightForWidth())
        self.buttonConfirm.setSizePolicy(sizePolicy)
        self.buttonConfirm.setOrientation(QtCore.Qt.Horizontal)
        self.buttonConfirm.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonConfirm.setObjectName("buttonConfirm")
        self.label = QtWidgets.QLabel(Confirm)
        self.label.setGeometry(QtCore.QRect(10, 10, 351, 61))
        self.label.setObjectName("label")

        self.retranslateUi(Confirm)
        self.buttonConfirm.accepted.connect(Confirm.accept)
        self.buttonConfirm.rejected.connect(Confirm.reject)
        QtCore.QMetaObject.connectSlotsByName(Confirm)

    def retranslateUi(self, Confirm):
        _translate = QtCore.QCoreApplication.translate
        Confirm.setWindowTitle(_translate("Confirm", "Dialog"))
        self.label.setText(_translate("Confirm", "<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">No destination directory specified, overwrite the source directory?</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Confirm = QtWidgets.QDialog()
    ui = Ui_Confirm()
    ui.setupUi(Confirm)
    Confirm.show()
    sys.exit(app.exec_())
