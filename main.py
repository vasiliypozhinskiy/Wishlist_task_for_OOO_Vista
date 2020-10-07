import wishlist_ui
from PyQt5 import QtWidgets
import database
import sys


class WishList(wishlist_ui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1167, 602)
        self.setWindowTitle('WishList')

        self.db = database.Database()
        self.db.create_table()
        self.read_from_db()

        self.tableWidget.setCurrentItem(None)

        self.tableWidget.setColumnWidth(0, 248)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 300)
        self.tableWidget.setColumnWidth(3, 350)

        self.table_for_input.setColumnWidth(0, 248)
        self.table_for_input.setColumnWidth(1, 100)
        self.table_for_input.setColumnWidth(2, 300)
        self.table_for_input.setColumnWidth(3, 350)

        self.AddButton.clicked.connect(self.add_button_clicked)
        self.DeleteButton.clicked.connect(self.delete_button_clicked)
        self.tableWidget.cellChanged.connect(self.update_db)

    def read_from_db(self):
        """Reads all data from db and adds it in tableWidget.
        Each cell have role 0x100 with row id in db"""
        data = self.db.read_all()
        for i, row in enumerate(data):
            items = (row['name'], row['price'], row['url'], row['comment'])
            row_id = row['id']
            self.tableWidget.insertRow(i)
            for j, item in enumerate(items):
                pyqt_item = QtWidgets.QTableWidgetItem(str(item))
                pyqt_item.setData(0x100, row_id)
                self.tableWidget.setItem(i, j, pyqt_item)

    def add_button_clicked(self):
        """Creates row from table_for_input for insert in db"""
        self.tableWidget.blockSignals(True)
        row = {}
        if self.table_for_input.item(0, 0):
            row['name'] = self.table_for_input.item(0, 0).text()
        else:
            pass
        if self.table_for_input.item(0, 1):
            row['price'] = self.table_for_input.item(0, 1).text()
            try:
                row['price'] = float(row['price'])
            except ValueError:
                row['price'] = 0
        else:
            pass
        if self.table_for_input.item(0, 2):
            row['url'] = self.table_for_input.item(0, 2).text()
        else:
            pass
        if self.table_for_input.item(0, 3):
            row['comment'] = self.table_for_input.item(0, 3).text()
        else:
            pass

        row_id = self.db.add_row(**row)
        self.add_row_in_tableWidget(row_id)

        self.table_for_input.clearContents()
        self.tableWidget.blockSignals(False)

    def add_row_in_tableWidget(self, row_id):
        number_of_row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(number_of_row)
        row = self.db.read_row(row_id)
        for i, item in enumerate([row['name'], str(row['price']), row['url'], row['comment']]):
            pyqt_item = QtWidgets.QTableWidgetItem(item)
            pyqt_item.setData(0x100, row['id'])
            self.tableWidget.setItem(number_of_row, i, pyqt_item)

        self.tableWidget.setCurrentItem(None)

    def delete_button_clicked(self):
        """Removes row from db and tableWidget"""
        if self.tableWidget.currentItem():
            current_row_number = self.tableWidget.currentItem().row()
            row_id = self.tableWidget.currentItem().data(0x100)
            self.db.delete_row(row_id)
            self.tableWidget.removeRow(current_row_number)

            self.tableWidget.setCurrentItem(None)

    def update_db(self):
        """Updates db when cell's content changes"""
        row_id = self.tableWidget.currentItem().data(0x100)
        number_of_row = self.tableWidget.currentItem().row()
        row = {}

        if self.tableWidget.item(number_of_row, 0):
            row['name'] = self.tableWidget.item(number_of_row, 0).text()
        else:
            pass
        if self.tableWidget.item(number_of_row, 1):
            row['price'] = self.tableWidget.item(number_of_row, 1).text()
            try:
                row['price'] = float(row['price'])
            except ValueError:
                row['price'] = 0
                self.tableWidget.currentItem().setText('0.0')
        else:
            pass
        if self.tableWidget.item(number_of_row, 2):
            row['url'] = self.tableWidget.item(number_of_row, 2).text()
        else:
            pass
        if self.tableWidget.item(number_of_row, 3):
            row['comment'] = self.tableWidget.item(number_of_row, 3).text()
        else:
            pass

        self.db.update_row(row_id, **row)
        self.tableWidget.setCurrentItem(None)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WishList()
    window.show()
    app.exec()

