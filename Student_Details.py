from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter.filedialog import *
import pandas as pd
from tkinter import *
import psycopg2
from PyQt5.QtWidgets import QMessageBox

class Ui_Student_details(object):
    def setupUi(self, Student_details):
        Student_details.setObjectName("Student_details")
        Student_details.resize(586, 236)
        self.centralwidget = QtWidgets.QWidget(Student_details)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_browse = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.browse_and_upload())
        self.btn_browse.setGeometry(QtCore.QRect(200, 110, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_browse.setFont(font)
        self.btn_browse.setObjectName("btn_browse")
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.clicked.connect(Student_details.close)
        self.btn_close.setGeometry(QtCore.QRect(460, 180, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_close.setFont(font)
        self.btn_close.setObjectName("btn_close")
        Student_details.setCentralWidget(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-200, 0, 811, 281))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Design/upload student details.jpg"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.btn_browse.raise_()
        self.btn_close.raise_()
        self.retranslateUi(Student_details)
        QtCore.QMetaObject.connectSlotsByName(Student_details)

    def browse_and_upload(self):
        root = Tk()
        filetypes = (('Excel Files', '*.xlsx'),('All files', '*.*'))
        root.withdraw()
        self.file_name = askopenfilename(title='Open A File',initialdir='/',filetypes=filetypes)
        self.df = pd.read_excel(self.file_name)
        self.stuNames = self.df['name'].tolist()
        self.stuBranch = self.df['branch'].tolist()
        self.stuYear = self.df['year'].tolist()
        self.stuEmail = self.df['email'].tolist()
        self.stuPRN = self.df['prn'].tolist()

        try:
            conn = psycopg2.connect(
            host='ec2-18-206-20-102.compute-1.amazonaws.com',
            database='ddeuc850qat336',
            user='gnmwvfusjgondu',
            password='d24dd511d794c7214bec9c67be92740279caabac4cb8e08f4769f49de27b580e',
            port='5432')
            cur = conn.cursor()

            for i in range(len(self.stuPRN)):
                query = "insert into ids values('{}','{}','{}','{}','{}')".format(self.stuNames[i],self.stuBranch[i],self.stuYear[i],self.stuEmail[i],self.stuPRN[i])
                cur.execute(query)
                conn.commit()
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Data Inserted Successfully")
            msg.setWindowTitle("Success")
            msg.exec_()

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f"Error due to {str(e)}")
            msg.setWindowTitle("Error")
            msg.exec_()
        finally:
            conn.close()
            cur.close()

    def retranslateUi(self, Student_details):
        _translate = QtCore.QCoreApplication.translate
        Student_details.setWindowTitle(_translate("Student_details", "Upload Student Details"))
        self.label.setText(_translate("Student_details", "UPLOAD STUDENT DETAILS"))
        self.btn_browse.setText(_translate("Student_details", "Browse for file"))
        self.btn_close.setText(_translate("Student_details", "Close"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Student_details = QtWidgets.QMainWindow()
    ui = Ui_Student_details()
    ui.setupUi(Student_details)
    Student_details.show()
    sys.exit(app.exec_())