import sys, random, sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 737)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 921, 611))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 630, 281, 41))
        self.pushButton.setObjectName("pushButton")
        self.update = QtWidgets.QPushButton(self.centralwidget)
        self.update.setGeometry(QtCore.QRect(120, 630, 281, 41))
        self.update.setObjectName("update")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 923, 26))
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
        self.pushButton.setText(_translate("MainWindow", "Добавить или изменить"))
        self.update.setText(_translate("MainWindow", "Обновить"))


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(642, 458)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Layout_inf = QtWidgets.QVBoxLayout()
        self.Layout_inf.setObjectName("Layout_inf")
        self.name_inf = QtWidgets.QLabel(Form)
        self.name_inf.setMinimumSize(QtCore.QSize(154, 40))
        self.name_inf.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.name_inf.setObjectName("name_inf")
        self.Layout_inf.addWidget(self.name_inf)
        self.genre_inf = QtWidgets.QLabel(Form)
        self.genre_inf.setMinimumSize(QtCore.QSize(143, 40))
        self.genre_inf.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.genre_inf.setObjectName("genre_inf")
        self.Layout_inf.addWidget(self.genre_inf)
        self.game_pub_inf = QtWidgets.QLabel(Form)
        self.game_pub_inf.setMinimumSize(QtCore.QSize(143, 40))
        self.game_pub_inf.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.game_pub_inf.setObjectName("game_pub_inf")
        self.Layout_inf.addWidget(self.game_pub_inf)
        self.year_inf = QtWidgets.QLabel(Form)
        self.year_inf.setMinimumSize(QtCore.QSize(143, 40))
        self.year_inf.setObjectName("year_inf")
        self.Layout_inf.addWidget(self.year_inf)
        self.grade_inf = QtWidgets.QLabel(Form)
        self.grade_inf.setMinimumSize(QtCore.QSize(143, 40))
        self.grade_inf.setObjectName("grade_inf")
        self.Layout_inf.addWidget(self.grade_inf)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(143, 40))
        self.label_2.setObjectName("label_2")
        self.Layout_inf.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.Layout_inf)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setMinimumSize(QtCore.QSize(300, 30))
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.roasting = QtWidgets.QLineEdit(Form)
        self.roasting.setMinimumSize(QtCore.QSize(300, 30))
        self.roasting.setObjectName("roasting")
        self.verticalLayout.addWidget(self.roasting)
        self.type = QtWidgets.QLineEdit(Form)
        self.type.setMinimumSize(QtCore.QSize(300, 30))
        self.type.setObjectName("type")
        self.verticalLayout.addWidget(self.type)
        self.taste = QtWidgets.QLineEdit(Form)
        self.taste.setMinimumSize(QtCore.QSize(380, 30))
        self.taste.setObjectName("taste")
        self.verticalLayout.addWidget(self.taste)
        self.cost = QtWidgets.QLineEdit(Form)
        self.cost.setMinimumSize(QtCore.QSize(380, 30))
        self.cost.setObjectName("cost")
        self.verticalLayout.addWidget(self.cost)
        self.vol = QtWidgets.QLineEdit(Form)
        self.vol.setMinimumSize(QtCore.QSize(380, 30))
        self.vol.setObjectName("vol")
        self.verticalLayout.addWidget(self.vol)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.errors_3 = QtWidgets.QLabel(Form)
        self.errors_3.setMinimumSize(QtCore.QSize(400, 20))
        self.errors_3.setMaximumSize(QtCore.QSize(696, 25))
        self.errors_3.setObjectName("errors_3")
        self.verticalLayout_2.addWidget(self.errors_3)
        self.errors = QtWidgets.QLabel(Form)
        self.errors.setMinimumSize(QtCore.QSize(400, 20))
        self.errors.setMaximumSize(QtCore.QSize(696, 25))
        self.errors.setObjectName("errors")
        self.verticalLayout_2.addWidget(self.errors)
        self.errors_2 = QtWidgets.QLabel(Form)
        self.errors_2.setMinimumSize(QtCore.QSize(400, 20))
        self.errors_2.setMaximumSize(QtCore.QSize(696, 25))
        self.errors_2.setObjectName("errors_2")
        self.verticalLayout_2.addWidget(self.errors_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.adder = QtWidgets.QPushButton(Form)
        self.adder.setMinimumSize(QtCore.QSize(250, 30))
        self.adder.setObjectName("adder")
        self.horizontalLayout_2.addWidget(self.adder)
        self.rename = QtWidgets.QPushButton(Form)
        self.rename.setMinimumSize(QtCore.QSize(238, 30))
        self.rename.setObjectName("rename")
        self.horizontalLayout_2.addWidget(self.rename)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление"))
        self.name_inf.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#000000;\">Назввние:</span></p></body></html>"))
        self.genre_inf.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#000000;\">Степень обжарки:</span></p></body></html>"))
        self.game_pub_inf.setText(_translate("Form", "<html><head/><body><p>Молотый или зерновой</p></body></html>"))
        self.year_inf.setText(_translate("Form", "<html><head/><body><p>Описание вкуса:</p></body></html>"))
        self.grade_inf.setText(_translate("Form", "<html><head/><body><p>Цена:</p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>Обьем упаковки:</p></body></html>"))
        self.errors_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.errors.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.errors_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.adder.setText(_translate("Form", "Добавить в БД"))
        self.rename.setText(_translate("Form", "Изменить"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.connection = sqlite3.connect("coffee.sqlite")
        self.setWindowTitle('Кофе')
        self.pushButton.clicked.connect(self.open_ed)
        self.update.clicked.connect(self.select_data)
        self.select_data()

    def open_ed(self):
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        if len(ids) == 0:
            ids = ['', '']
        self.ed = Editer(self, ids[0])
        self.ed.show()

    def select_data(self):
        res = []
        all = self.connection.cursor().execute("""SELECT * FROM all_cof""").fetchall()
        for i in all:
            res.append((i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.setHorizontalHeaderLabels(['id', 'Название сорта', 'степень обжарки',
                                                    'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])


class Editer(QWidget, Ui_Form):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.initUI(args)

    def initUI(self, args):
        self.sel = args[0]
        self.id = args[1]
        self.setWindowTitle('Добавление и удаление')
        self.connection = sqlite3.connect("coffee.sqlite")
        self.adder.clicked.connect(self.add_game)
        self.rename.clicked.connect(self.changed)

    def add_game(self):
        cur = self.connection.cursor()
        cur.execute('''INSERT INTO all_cof(name, ro_degree, type, taste, price, size)
        VALUES(?, ?, ?, ?, ?, ?)''', (self.name.text(),
                                   self.roasting.text(),
                                   self.type.text(),
                                   self.taste.text(),
                                   int(self.cost.text()),
                                   int(self.vol.text())))
        self.connection.commit()

    def changed(self):
        if self.id == '':
            self.sel.statusBar().showMessage(f'Вы должны выбрать кофе')
            self.sel.statusBar().setStyleSheet('background:green')
            Editer.setVisible(self, False)
        else:
            req = []
            if self.name.text() != '':
                req.append(f'SET name = "{self.name.text()}"')
            if self.roasting.text() != '':
                req.append(f'SET ro_degree = "{self.roasting.text()}"')
            if self.taste.text() != '':
                req.append(f'SET type = "{self.type.text()}"')
            if self.taste.text() != '':
                req.append(f'SET taste = "{self.taste.text()}"')
            if self.cost.text() != '':
                req.append(f'SET price = {int(self.cost.text())}')
            if self.vol.text() != '':
                req.append(f'SET size = {int(self.vol.text())}')
            for i in range(len(req)):
                cur = self.connection.cursor()
                que = "UPDATE all_cof\n"
                que += req[i] + '\n'
                que += f"WHERE id = {self.id}"
                cur.execute(que)
                self.connection.commit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())