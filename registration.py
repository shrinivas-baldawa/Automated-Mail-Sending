from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import psycopg2
import re

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
class Ui_registration(object):
    def setupUi(self, registration):
        registration.setObjectName("registration")
        registration.resize(848, 518)
        self.regisWidget = QtWidgets.QWidget(registration)
        self.regisWidget.setObjectName("regisWidget")
        self.heading_label = QtWidgets.QLabel(self.regisWidget)
        self.heading_label.setGeometry(QtCore.QRect(340, 30, 171, 41))
        self.heading_label.setObjectName("heading_label")
        self.name_label = QtWidgets.QLabel(self.regisWidget)
        self.name_label.setGeometry(QtCore.QRect(50, 110, 61, 31))
        self.name_label.setObjectName("name_label")
        self.emailid_label = QtWidgets.QLabel(self.regisWidget)
        self.emailid_label.setGeometry(QtCore.QRect(50, 170, 91, 31))
        self.emailid_label.setObjectName("emailid_label")
        self.phoneno_label = QtWidgets.QLabel(self.regisWidget)
        self.phoneno_label.setGeometry(QtCore.QRect(50, 230, 151, 31))
        self.phoneno_label.setObjectName("phoneno_label")
        self.phoneno_label_2 = QtWidgets.QLabel(self.regisWidget)
        self.phoneno_label_2.setGeometry(QtCore.QRect(50, 290, 101, 31))
        self.phoneno_label_2.setObjectName("phoneno_label_2")
        self.phoneno_label_3 = QtWidgets.QLabel(self.regisWidget)
        self.phoneno_label_3.setGeometry(QtCore.QRect(50, 350, 191, 31))
        self.phoneno_label_3.setObjectName("phoneno_label_3")
        self.name_field = QtWidgets.QLineEdit(self.regisWidget)
        self.name_field.setGeometry(QtCore.QRect(270, 111, 511, 31))
        self.name_field.setObjectName("name_field")
        self.emailid_field = QtWidgets.QLineEdit(self.regisWidget)
        self.emailid_field.setGeometry(QtCore.QRect(270, 170, 511, 31))
        self.emailid_field.setObjectName("emailid_field")
        self.phoneno_field = QtWidgets.QLineEdit(self.regisWidget)
        self.phoneno_field.setGeometry(QtCore.QRect(270, 230, 511, 31))
        self.phoneno_field.setObjectName("phoneno_field")
        self.password_field = QtWidgets.QLineEdit(self.regisWidget)
        self.password_field.setGeometry(QtCore.QRect(270, 290, 511, 31))
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_field.setObjectName("password_field")
        self.confirmpassword_field = QtWidgets.QLineEdit(self.regisWidget)
        self.confirmpassword_field.setGeometry(QtCore.QRect(270, 350, 511, 31))
        self.confirmpassword_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword_field.setObjectName("confirmpassword_field")
        self.pushButton = QtWidgets.QPushButton(self.regisWidget,clicked=lambda :self.registrations_())
        self.pushButton.setGeometry(QtCore.QRect(150, 430, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        registration.setCentralWidget(self.regisWidget)
        self.label = QtWidgets.QLabel(self.regisWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 851, 521))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Design/registration.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.heading_label.raise_()
        self.name_label.raise_()
        self.emailid_label.raise_()
        self.phoneno_label.raise_()
        self.phoneno_label_2.raise_()
        self.phoneno_label_3.raise_()
        self.name_field.raise_()
        self.emailid_field.raise_()
        self.phoneno_field.raise_()
        self.password_field.raise_()
        self.confirmpassword_field.raise_()
        self.pushButton.raise_()

        self.retranslateUi(registration)
        QtCore.QMetaObject.connectSlotsByName(registration)

    def registrations_(self):
        varName = self.name_field.text()
        varEmail = self.emailid_field.text()
        varPhone = self.phoneno_field.text()
        varPass = self.password_field.text()
        varConPass = self.confirmpassword_field.text()
        if varName == "" or varEmail == "" or varPhone == "" or varPass == "" or varConPass == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("All Details Are Required")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            if varPass == varConPass:
                if (re.search(regex,varEmail)):
                    if Pattern.match(varPhone):
                        conn = psycopg2.connect(
                        host='ec2-18-206-20-102.compute-1.amazonaws.com',
                        database='ddeuc850qat336',
                        user='gnmwvfusjgondu',
                        password='d24dd511d794c7214bec9c67be92740279caabac4cb8e08f4769f49de27b580e',
                        port='5432')
                        cur = conn.cursor()
                        checkQuery = "select * from logindetails where mobileno = '{}'".format(self.phoneno_field.text())
                        cur.execute(checkQuery)
                        checkValue = cur.fetchone()
                        if checkValue == None:
                            query = "INSERT INTO logindetails(username,password,name,mobileno) VALUES (%s,%s,%s,%s)"
                            checkTuple = (varEmail,varConPass,varName,varPhone)
                            cur.execute(query,checkTuple)
                            conn.commit()
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setText("Registration Is Successful")
                            msg.setWindowTitle("Success")
                            msg.setStandardButtons(QMessageBox.Ok)
                            retVal = msg.exec_()
                            if retVal == 1024:
                                self.name_field.setText("")
                                self.emailid_field.setText("")
                                self.phoneno_field.setText("")
                                self.password_field.setText("")
                                self.confirmpassword_field.setText("")
                                registration.close()
                            cur.close()
                            conn.close()
                        else:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setText("Already Registered")
                            msg.setWindowTitle("Error")
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.exec_()

                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("Invalid Mobile Number")
                        msg.setWindowTitle("Error")
                        msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Invalid Email ID")
                    msg.setWindowTitle("Error")
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Passwords Don't Match")
                msg.setWindowTitle("Error")
                msg.exec_()

    def retranslateUi(self, registration):
        _translate = QtCore.QCoreApplication.translate
        registration.setWindowTitle(_translate("registration", "Registration"))
        self.heading_label.setText(_translate("registration", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Registration</span></p></body></html>"))
        self.name_label.setText(_translate("registration", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name</span></p></body></html>"))
        self.emailid_label.setText(_translate("registration", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Email Id</span></p></body></html>"))
        self.phoneno_label.setText(_translate("registration", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Phone Number</span></p></body></html>"))
        self.phoneno_label_2.setText(_translate("registration", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Password</span></p></body></html>"))
        self.phoneno_label_3.setText(_translate("registration", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Confirm Password</span></p></body></html>"))
        self.pushButton.setText(_translate("registration", "Register !"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registration = QtWidgets.QMainWindow()
    ui = Ui_registration()
    ui.setupUi(registration)
    registration.show()
    sys.exit(app.exec_())
