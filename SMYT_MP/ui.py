# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Form implementation generated from reading ui file 'd:/test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))
QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("utf8"))
QtCore.QTextCodec.setCodecForLocale(QtCore.QTextCodec.codecForName("utf8"))

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(814, 488)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #设置壁纸
        png = QtGui.QPixmap()
        png.load("bizhi.jpg")
        palette1 = QtGui.QPalette()
        #palette1.setBrush(self.centralwidget.backgroundRole(),QtGui.QColor(192, 253, 123))
        palette1.setBrush(self.centralwidget.backgroundRole(), QtGui.QBrush(png))
        self.centralwidget.setPalette(palette1)
        self.centralwidget.setAutoFillBackground(True)

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 60, 75, 61))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 60, 75, 61))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.sql_box = QtGui.QTextBrowser(self.centralwidget)
        self.sql_box.setGeometry(QtCore.QRect(450, 50, 251, 81))
        self.sql_box.setObjectName(_fromUtf8("sql_box"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 121, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roman"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setIndent(0)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 300, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 120, 71, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 150, 71, 16))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.fund_names_box = QtGui.QPlainTextEdit(self.centralwidget)
        self.fund_names_box.setGeometry(QtCore.QRect(90, 50, 251, 181))
        self.fund_names_box.setPlainText(_fromUtf8(""))
        self.fund_names_box.setObjectName(_fromUtf8("fund_names_box"))
        self.form_name = QtGui.QLineEdit(self.centralwidget)
        self.form_name.setGeometry(QtCore.QRect(170, 300, 171, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.form_name.setFont(font)
        self.form_name.setObjectName(_fromUtf8("form_name"))
        self.search = QtGui.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(360, 300, 75, 61))
        self.search.setObjectName(_fromUtf8("search"))

        self.export_excel = QtGui.QPushButton(self.centralwidget)
        self.export_excel.setGeometry(QtCore.QRect(710, 300, 75, 61))
        self.export_excel.setObjectName(_fromUtf8("export_excel"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 350, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.other_requires = QtGui.QPlainTextEdit(self.centralwidget)
        self.other_requires.setGeometry(QtCore.QRect(170, 350, 171, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.other_requires.setFont(font)
        self.other_requires.setObjectName(_fromUtf8("other_requires"))

        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(450, 141, 251, 311))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1000)
        self.tableWidget.setHorizontalHeaderLabels(['基金名称','查询到数量'])
        #自动列宽
        #self.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)

        self.activate_export = QtGui.QPushButton(self.centralwidget)
        self.activate_export.setGeometry(QtCore.QRect(710, 370, 75, 23))
        self.activate_export.setObjectName(_fromUtf8("pushButton_3"))


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sql_box.copy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SMYT Version1.1.0", None))
        self.pushButton.setText(_translate("MainWindow", "生成SQL", None))
        self.pushButton_2.setText(_translate("MainWindow", "复制", None))
        self.label.setText(_translate("MainWindow", "基金名称", None))
        self.label_2.setText(_translate("MainWindow", "设置表名", None))
        self.checkBox.setText(_translate("MainWindow", "完全匹配", None))
        self.checkBox_2.setText(_translate("MainWindow", "模    糊", None))
        self.form_name.setText(_translate("MainWindow", "fund_type_mapping", None))
        self.form_name.setText(_translate("MainWindow", "base.fund_type_mapping", None))
        self.search.setText(_translate("MainWindow", "直接查询", None))
        self.export_excel.setText(_translate("MainWindow", "导出excel", None))
        self.label_3.setText(_translate("MainWindow", "设置来源代码", None))
        self.other_requires.setPlainText(_translate("MainWindow", "typestandard_code = ", None))
        self.activate_export.setText(_translate("MainWindow", "启用导出", None))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

