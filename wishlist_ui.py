# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wishlist.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1167, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 1000, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(1020, 0, 141, 28))
        self.AddButton.setObjectName("AddButton")
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(1020, 50, 141, 28))
        self.DeleteButton.setObjectName("DeleteButton")
        self.table_for_input = QtWidgets.QTableWidget(self.centralwidget)
        self.table_for_input.setGeometry(QtCore.QRect(10, 0, 1000, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_for_input.setFont(font)
        self.table_for_input.setRowCount(1)
        self.table_for_input.setObjectName("table_for_input")
        self.table_for_input.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.table_for_input.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(False)
        item.setFont(font)
        self.table_for_input.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_for_input.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_for_input.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_for_input.setHorizontalHeaderItem(3, item)
        self.table_for_input.horizontalHeader().setVisible(False)
        self.table_for_input.horizontalHeader().setHighlightSections(True)
        self.table_for_input.verticalHeader().setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1167, 26))
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
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Цена"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ссылка"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Примечания"))
        self.AddButton.setText(_translate("MainWindow", "Добавить запись"))
        self.DeleteButton.setText(_translate("MainWindow", "Удалить запись"))
        item = self.table_for_input.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_for_input.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        item = self.table_for_input.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Цена"))
        item = self.table_for_input.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ссылка"))
        item = self.table_for_input.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Примечания"))