from tkinter import filedialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import psycopg2
import pandas as pd
from tkinter import *
from tkinter.filedialog import *
import smtplib
from email.message import EmailMessage
from PyQt5.QtWidgets import QMessageBox
import sys
from Student_Details import Ui_Student_details

class Ui_MainPage(object):
    def setupUi(self, MainPage):
        self.attachments = []
        MainPage.setObjectName("MainPage")
        MainPage.resize(564, 741)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainPage.setFont(font)
        MainPage.setMouseTracking(True)
        MainPage.setTabletTracking(False)
        MainPage.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainPage.setAcceptDrops(True)
        MainPage.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(MainPage)
        self.centralwidget.setObjectName("centralwidget")
        self.attendance_btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.excel_file_read())
        self.attendance_btn.setGeometry(QtCore.QRect(180, 50, 221, 31))
        self.attendance_btn.setObjectName("attendance_btn")
        self.eventUpdate_text = QtWidgets.QTextEdit(self.centralwidget, placeholderText='Enter Your Event Updates (If Any!)', acceptRichText=True)
        self.eventUpdate_text.setEnabled(True)
        self.eventUpdate_text.setGeometry(QtCore.QRect(130, 130, 331, 91))
        self.eventUpdate_text.setAcceptDrops(True)
        self.eventUpdate_text.setToolTip("")
        self.eventUpdate_text.setObjectName("eventUpdate_text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 0, 131, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 90, 161, 21))
        self.label_2.setObjectName("label_2")
        self.eventUpdates_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.attachments_check_())
        self.eventUpdates_btn.setGeometry(QtCore.QRect(120, 230, 351, 31))
        self.eventUpdates_btn.setObjectName("eventUpdates_btn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 280, 161, 31))
        self.label_3.setObjectName("label_3")
        self.announcement_text = QtWidgets.QTextEdit(self.centralwidget,placeholderText='Enter Your Announcments (If Any!)', acceptRichText=True)
        self.announcement_text.setGeometry(QtCore.QRect(140, 320, 311, 91))
        self.announcement_text.setObjectName("announcement_text")
        self.announcment_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.attachments_check_())
        self.announcment_btn.setGeometry(QtCore.QRect(130, 420, 331, 31))
        self.announcment_btn.setObjectName("announcment_btn")
        self.sendMail_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.mailSend())
        self.sendMail_btn.setGeometry(QtCore.QRect(180, 610, 181, 31))
        self.sendMail_btn.setObjectName("sendMail_btn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 470, 191, 31))
        self.label_4.setObjectName("label_4")
        self.all_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.all_checkbox.stateChanged.connect(self.check_box_)
        self.all_checkbox.setGeometry(QtCore.QRect(20, 510, 70, 17))
        self.all_checkbox.setObjectName("all_checkbox")
        self.fe_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.fe_checkbox.setEnabled(False)
        self.fe_checkbox.stateChanged.connect(self.check_box_)
        self.fe_checkbox.setGeometry(QtCore.QRect(20, 570, 51, 17))
        self.fe_checkbox.setObjectName("fe_checkbox")
        self.se_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.se_checkbox.stateChanged.connect(self.check_box_)
        self.se_checkbox.setEnabled(False)
        self.se_checkbox.setGeometry(QtCore.QRect(80, 570, 51, 17))
        self.se_checkbox.setObjectName("se_checkbox")
        self.te_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.te_checkbox.setEnabled(False)
        self.te_checkbox.stateChanged.connect(self.check_box_)
        self.te_checkbox.setGeometry(QtCore.QRect(140, 570, 51, 17))
        self.te_checkbox.setObjectName("te_checkbox")
        self.be_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.be_checkbox.setEnabled(False)
        self.be_checkbox.stateChanged.connect(self.check_box_)
        self.be_checkbox.setGeometry(QtCore.QRect(210, 570, 51, 17))
        self.be_checkbox.setObjectName("be_checkbox")
        self.ce_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.ce_checkbox.stateChanged.connect(self.check_box_)
        self.ce_checkbox.setGeometry(QtCore.QRect(20, 540, 51, 17))
        self.ce_checkbox.setObjectName("ce_checkbox")
        self.it_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.it_checkbox.stateChanged.connect(self.check_box_)
        self.it_checkbox.setGeometry(QtCore.QRect(80, 540, 51, 17))
        self.it_checkbox.setObjectName("it_checkbox")
        self.ppt_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.ppt_checkbox.stateChanged.connect(self.check_box_)
        self.ppt_checkbox.setGeometry(QtCore.QRect(140, 540, 71, 17))
        self.ppt_checkbox.setObjectName("ppt_checkbox")
        self.extc_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.extc_checkbox.stateChanged.connect(self.check_box_)
        self.extc_checkbox.setGeometry(QtCore.QRect(210, 540, 81, 17))
        self.extc_checkbox.setObjectName("extc_checkbox")
        self.mech_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.mech_checkbox.stateChanged.connect(self.check_box_)
        self.mech_checkbox.setGeometry(QtCore.QRect(300, 540, 91, 17))
        self.mech_checkbox.setObjectName("mech_checkbox")
        self.line1 = QtWidgets.QFrame(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(-30, 70, 661, 41))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 270, 581, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 445, 631, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 650, 271, 31))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        MainPage.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainPage)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 564, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuOptions = QtWidgets.QMenu(self.menuBar)
        self.menuOptions.setObjectName("menuOptions")
        MainPage.setMenuBar(self.menuBar)
        self.Upload_Student_Data = QtWidgets.QAction(MainPage)
        self.Upload_Student_Data.setObjectName("Upload_Student_Data")
        self.Upload_Student_Data.triggered.connect(self.Upload_Student_Data_check)
        self.menuOptions.addAction(self.Upload_Student_Data)
        self.menuBar.addAction(self.menuOptions.menuAction())
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(4, 0, 561, 721))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../Design/mail sending.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.attendance_btn.raise_()
        self.eventUpdate_text.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.eventUpdates_btn.raise_()
        self.label_3.raise_()
        self.announcement_text.raise_()
        self.announcment_btn.raise_()
        self.sendMail_btn.raise_()
        self.label_4.raise_()
        self.all_checkbox.raise_()
        self.fe_checkbox.raise_()
        self.se_checkbox.raise_()
        self.te_checkbox.raise_()
        self.be_checkbox.raise_()
        self.ce_checkbox.raise_()
        self.it_checkbox.raise_()
        self.ppt_checkbox.raise_()
        self.extc_checkbox.raise_()
        self.mech_checkbox.raise_()
        self.line1.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_5.raise_()

        self.retranslateUi(MainPage)
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def Upload_Student_Data_check(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Student_details()
        self.ui.setupUi(self.window)
        self.window.show()

    def attachments_check_(self):
        self.filename = filedialog.askopenfilename(initialdir='/',title='Please Select A File')
        self.attachments.append(self.filename)
        self.label_5.setText('Attached '+str(len(self.attachments))+' files.')

    def excel_file_read(self):
        try:
            root = Tk()
            filetypes = (('Excel Files', '*.xlsx'),('All files', '*.*'))
            root.withdraw()
            self.file_name = askopenfilename(title='Open A File',initialdir='/',filetypes=filetypes)
            self.df = pd.read_excel(self.file_name)

            self.present_dataframe = self.df[self.df['Status'] == 'P']
            self.presentIDS = self.present_dataframe.iloc[:,1]

            self.absent_dataframe = self.df[self.df['Status'] == 'A']
            self.absentIDS = self.absent_dataframe.iloc[:,1]

            self.allRollNumbers = self.df['PRN']
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("File Is Read Successfully")
            msg.setWindowTitle("Success")
            msg.exec_()

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Error While Excel Reading {}'.format(e))
            msg.setWindowTitle("Error")
            msg.exec_()

    def mailSend(self):
        try:
            conn = psycopg2.connect(host='ec2-18-206-20-102.compute-1.amazonaws.com',
            user='gnmwvfusjgondu',
            password='d24dd511d794c7214bec9c67be92740279caabac4cb8e08f4769f49de27b580e',
            dbname='ddeuc850qat336')
            cur = conn.cursor()

            allBranches = ['CE','IT','EXTC','PPT','MECH']
            allYears = ['FE','SE','TE','BE']
            branchList = [self.ce_checkbox.isChecked(),self.it_checkbox.isChecked(),self.extc_checkbox.isChecked(),self.ppt_checkbox.isChecked(),self.mech_checkbox.isChecked()]
            YearList = [self.fe_checkbox.isChecked(),self.se_checkbox.isChecked(),self.te_checkbox.isChecked(),self.be_checkbox.isChecked()]
            branchPosition = [i for i,x in enumerate(branchList) if x]
            yearPositions = [j for j,y in enumerate(YearList) if y]
            branches = []
            for k in yearPositions:
                branches.append(allYears[k])
            finalQuery = "select email from ids where branch = '{}' and year in {} except select email from ids where prn in {}".format(allBranches[branchPosition[0]],tuple(branches),tuple(self.allRollNumbers))
            cur.execute(finalQuery)
            rows2 = cur.fetchall() # This is a list type
            self.finalList = []
            self.finalList = [i[0] for i in rows2]

            self.msg1 = EmailMessage()
            self.msg1['Subject'] = 'SIES Graduate School Of Technology'
            self.msg1['From'] = 'Faculty'
            self.msg1['X-Priority'] = '1'
            self.msg1['X-MSMail-Priority'] = 'High'
            self.msg1['To'] = self.presentIDS.values.tolist()
            self.msg1.set_content('''Hello Student,
            You Were Present For The Lecture.
            
            {}
            
            {}
            
            Keep Learning!

            Regards,
            SIES GST,
            Nerul, Navi Mumbai.'''.format(self.eventUpdate_text.toPlainText(), self.announcement_text.toPlainText())) 

            self.msg2 = EmailMessage()
            self.msg2['Subject'] = 'SIES Graduate School Of Technology'
            self.msg2['From'] = 'Faculty'
            self.msg2['X-Priority'] = '1'
            self.msg2['X-MSMail-Priority'] = 'High'
            self.msg2['To'] = self.absentIDS.values.tolist()
            self.msg2.set_content('''Hello Student,
            You Were Absent For The Lecture.
            Try Attending The Lectures On A Regular Basis.
            
            {}
            
            {}

            Regards,
            SIES GST,
            Nerul, Navi Mumbai.'''.format(self.eventUpdate_text.toPlainText(), self.announcement_text.toPlainText()))

            self.msg3 = EmailMessage()
            self.msg3['Subject'] = 'SIES Graduate School Of Technology'
            self.msg3['From'] = 'Faculty'
            self.msg3['X-Priority'] = '1'
            self.msg3['X-MSMail-Priority'] = 'High'
            self.msg3['To'] = self.finalList
            self.msg3.set_content('''Hello Student,

            {}
            
            {}

            Regards,
            SIES GST,
            Nerul, Navi Mumbai.'''.format(self.eventUpdate_text.toPlainText(), self.announcement_text.toPlainText()))

            for self.filename in self.attachments:
                self.filetype = self.filename.split('.')
                self.filetype = self.filetype[1]
                if self.filetype == "jpg" or self.filetype == "JPG" or self.filetype == "png" or self.filetype == "PNG":
                    import imghdr
                    with open(self.filename, 'rb') as self.f:
                        self.file_data = self.f.read()
                        self.image_type = imghdr.what(self.filename)
                    self.msg1.add_attachment(self.file_data, maintype='image', subtype = self.image_type, filename = self.f.name)
                    self.msg2.add_attachment(self.file_data, maintype='image', subtype = self.image_type, filename = self.f.name)
                    self.msg3.add_attachment(self.file_data, maintype='image', subtype = self.image_type, filename = self.f.name)
                else:
                    with open(self.filename, 'rb') as self.f:
                        self.file_data = self.f.read()
                    self.msg1.add_attachment(self.file_data, maintype = 'Application',subtype = 'octet-stream', filename = self.f.name)
                    self.msg2.add_attachment(self.file_data, maintype = 'Application',subtype = 'octet-stream', filename = self.f.name)
                    self.msg3.add_attachment(self.file_data, maintype = 'Application',subtype = 'octet-stream', filename = self.f.name)

            with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
                server.login('facultysies.email@gmail.com','facultyemail')
                server.send_message(self.msg1)
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as server2:
                server2.login('facultysies.email@gmail.com','facultyemail')
                server2.send_message(self.msg2)
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as server3:
                server3.login('facultysies.email@gmail.com','facultyemail')
                server3.send_message(self.msg3)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Mail Sent To Students")
            msg.setWindowTitle("Success")
            retVal = msg.exec_()
            if retVal == 1024:
                self.eventUpdate_text.setText('')
                self.announcement_text.setText('')
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f'Error Occured While Mail Sending {str(e)}')
            msg.setWindowTitle("Warning")
            msg.exec_()
        finally:
            cur.close()
            conn.close()

    def check_box_(self):
        if self.all_checkbox.isChecked():
            self.fe_checkbox.setEnabled(False)
            self.se_checkbox.setEnabled(False)
            self.te_checkbox.setEnabled(False)
            self.be_checkbox.setEnabled(False)
            self.ce_checkbox.setEnabled(False)
            self.it_checkbox.setEnabled(False)
            self.extc_checkbox.setEnabled(False)
            self.mech_checkbox.setEnabled(False)
            self.ppt_checkbox.setEnabled(False)

        if self.all_checkbox.isChecked() == False:
            self.fe_checkbox.setEnabled(True)
            self.se_checkbox.setEnabled(True)
            self.te_checkbox.setEnabled(True)
            self.be_checkbox.setEnabled(True)
            self.ce_checkbox.setEnabled(True)
            self.it_checkbox.setEnabled(True)
            self.extc_checkbox.setEnabled(True)
            self.mech_checkbox.setEnabled(True)
            self.ppt_checkbox.setEnabled(True)

        if self.ce_checkbox.isChecked():
            self.all_checkbox.setEnabled(False)
            self.it_checkbox.setEnabled(False)
            self.extc_checkbox.setEnabled(False)
            self.ppt_checkbox.setEnabled(False)
            self.mech_checkbox.setEnabled(False)

        if self.it_checkbox.isChecked():
            self.all_checkbox.setEnabled(False)
            self.ce_checkbox.setEnabled(False)
            self.extc_checkbox.setEnabled(False)
            self.ppt_checkbox.setEnabled(False)
            self.mech_checkbox.setEnabled(False)

        if self.extc_checkbox.isChecked():
            self.all_checkbox.setEnabled(False)
            self.it_checkbox.setEnabled(False)
            self.ce_checkbox.setEnabled(False)
            self.ppt_checkbox.setEnabled(False)
            self.mech_checkbox.setEnabled(False)
        
        if self.ppt_checkbox.isChecked():
            self.all_checkbox.setEnabled(False)
            self.it_checkbox.setEnabled(False)
            self.ce_checkbox.setEnabled(False)
            self.extc_checkbox.setEnabled(False)
            self.mech_checkbox.setEnabled(False)

        if self.mech_checkbox.isChecked():
            self.all_checkbox.setEnabled(False)
            self.it_checkbox.setEnabled(False)
            self.ce_checkbox.setEnabled(False)
            self.extc_checkbox.setEnabled(False)
            self.ppt_checkbox.setEnabled(False)

        if (self.ce_checkbox.isChecked() or self.it_checkbox.isChecked() or self.extc_checkbox.isChecked() or self.ppt_checkbox.isChecked() or self.mech_checkbox.isChecked()):
            self.all_checkbox.setEnabled(False)
            self.fe_checkbox.setEnabled(True)
            self.se_checkbox.setEnabled(True)
            self.te_checkbox.setEnabled(True)
            self.be_checkbox.setEnabled(True)
        else:
            self.all_checkbox.setEnabled(True)
            self.se_checkbox.setEnabled(False)
            self.fe_checkbox.setEnabled(False)
            self.te_checkbox.setEnabled(False)
            self.be_checkbox.setEnabled(False)

    def retranslateUi(self, MainPage):
        _translate = QtCore.QCoreApplication.translate
        MainPage.setWindowTitle(_translate("MainPage", "Mail Sending"))
        self.attendance_btn.setText(_translate("MainPage", "Select Your Files "))
        self.eventUpdate_text.setHtml(_translate("MainPage", ""))
        self.label.setText(_translate("MainPage", "Attendance"))
        self.label_5.setText(_translate("MainPage", ""))
        self.label_2.setText(_translate("MainPage", "Event Updates"))
        self.eventUpdates_btn.setText(_translate("MainPage", "Browse for Attatchments"))
        self.label_3.setText(_translate("MainPage", "Announcements"))
        self.announcment_btn.setText(_translate("MainPage", "Browse for Attatchments"))
        self.sendMail_btn.setText(_translate("MainPage", "Send Mail"))
        self.label_4.setText(_translate("MainPage", "Select Category"))
        self.all_checkbox.setText(_translate("MainPage", "All"))
        self.fe_checkbox.setText(_translate("MainPage", "FE"))
        self.se_checkbox.setText(_translate("MainPage", "SE"))
        self.te_checkbox.setText(_translate("MainPage", "TE"))
        self.be_checkbox.setText(_translate("MainPage", "BE"))
        self.ce_checkbox.setText(_translate("MainPage", "CE"))
        self.it_checkbox.setText(_translate("MainPage", "IT"))
        self.ppt_checkbox.setText(_translate("MainPage", "PPT"))
        self.extc_checkbox.setText(_translate("MainPage", "EXTC"))
        self.mech_checkbox.setText(_translate("MainPage", "MECH"))
        self.menuOptions.setTitle(_translate("MainPage", "Options"))
        self.Upload_Student_Data.setText(_translate("MainPage", "Upload Student Data"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainPage = QtWidgets.QMainWindow()
    ui = Ui_MainPage()
    ui.setupUi(MainPage)
    MainPage.show()
    sys.exit(app.exec_())
