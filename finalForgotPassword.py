from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
from PyQt5.QtWidgets import QMessageBox
import requests
import random


class Ui_ForgotPass(object):
    def setupUi(self, ForgotPass):
        ForgotPass.setObjectName("ForgotPass")
        ForgotPass.resize(656, 698)
        self.centralwidget = QtWidgets.QWidget(ForgotPass)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 100, 361, 41))
        self.label.setObjectName("label")
        self.mobile_field = QtWidgets.QLineEdit(self.centralwidget)
        self.mobile_field.setGeometry(QtCore.QRect(270, 180, 291, 31))
        self.mobile_field.setObjectName("mobile_field")
        self.enter_label = QtWidgets.QLabel(self.centralwidget)
        self.enter_label.setGeometry(QtCore.QRect(60, 160, 181, 81))
        self.enter_label.setObjectName("enter_label")
        self.enterotp_label = QtWidgets.QLabel(self.centralwidget)
        self.enterotp_label.setGeometry(QtCore.QRect(90, 390, 121, 31))
        self.enterotp_label.setObjectName("enterotp_label")
        self.otpenter_field = QtWidgets.QLineEdit(self.centralwidget)
        self.otpenter_field.setGeometry(QtCore.QRect(340, 390, 211, 31))
        self.otpenter_field.setReadOnly(True)
        self.otpenter_field.setObjectName("otpenter_field")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 530, 311, 31))
        self.label_2.setObjectName("label_2")
        self.otpsent_label = QtWidgets.QLabel(self.centralwidget)
        self.otpsent_label.setGeometry(QtCore.QRect(200, 250, 251, 31))
        self.otpsent_label.setObjectName("otpsent_label")
        self.newpassword_field = QtWidgets.QLineEdit(self.centralwidget)
        self.newpassword_field.setGeometry(QtCore.QRect(100, 570, 451, 41))
        self.newpassword_field.setReadOnly(True)
        self.newpassword_field.setObjectName("newpassword_field")
        self.newpassword_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sendotp_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.opt_send_())
        self.sendotp_btn.setGeometry(QtCore.QRect(220, 300, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sendotp_btn.setFont(font)
        self.sendotp_btn.setObjectName("sendotp_btn")
        self.checkotp_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.opt_check_())
        self.checkotp_btn.setGeometry(QtCore.QRect(220, 460, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.checkotp_btn.setFont(font)
        self.checkotp_btn.setObjectName("checkotp_btn")
        self.change_password_btn = QtWidgets.QPushButton(self.centralwidget, clicked =lambda:self.password_update_())
        self.change_password_btn.setGeometry(QtCore.QRect(150, 630, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.change_password_btn.setFont(font)
        self.change_password_btn.setObjectName("change_password_btn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 661, 701))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../Design/forgot password.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label.raise_()
        self.mobile_field.raise_()
        self.enter_label.raise_()
        self.enterotp_label.raise_()
        self.otpenter_field.raise_()
        self.label_2.raise_()
        self.otpsent_label.raise_()
        self.newpassword_field.raise_()
        self.sendotp_btn.raise_()
        self.checkotp_btn.raise_()
        self.change_password_btn.raise_()
        ForgotPass.setCentralWidget(self.centralwidget)

        self.retranslateUi(ForgotPass)
        QtCore.QMetaObject.connectSlotsByName(ForgotPass)

    def opt_send_(self):
        try:
            conn = psycopg2.connect(
                host='ec2-18-206-20-102.compute-1.amazonaws.com',
                database='ddeuc850qat336',
                user='gnmwvfusjgondu',
                password='d24dd511d794c7214bec9c67be92740279caabac4cb8e08f4769f49de27b580e',
                port='5432')
            cur = conn.cursor()
            varPhoneCheck = str(self.mobile_field.text())
            cur.execute("SELECT * FROM logindetails WHERE mobileno = '{}'".format(varPhoneCheck))
            row = cur.fetchone()
            if row == None:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Mobile Number Is Not Registered")
                msg.setWindowTitle("Error")
                msg.exec_()
                self.mobile_field.setText("")
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(f"OTP Sent To Your Registered Mobile Number")
                msg.setWindowTitle("Information")
                msg.exec_()
                self.otpenter_field.setReadOnly(False)
                self.otp = random.randint(1000,9999)
                url = 'https://www.fast2sms.com/dev/bulk'
                query_string = {"authorization":"azscTIE0NFdCx5F5w9CU6DuYFTAyLcLafhUR24oZabvK2tbe2Qtf5Swgtl5P",
                "sender_id":"SIES GST",
                "message":"Your OTP Is : {0}".format(self.otp),
                "language":"English",
                "route":"p",
                "numbers":"{0}".format(varPhoneCheck)}
                headers = {'cache-control':'no-cache'}
                response = requests.request("GET",url,headers=headers, params=query_string)
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f"Error Occured: {str(e)}")
            msg.setWindowTitle("Error")
            msg.exec_()
        finally:
            cur.close()
            conn.close()
            
    def opt_check_(self):
        if self.otp == int(self.otpenter_field.text()):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"OTP Verified, You Can Change Your Password Now!")
            msg.setWindowTitle("Information")
            msg.exec_()
            self.newpassword_field.setReadOnly(False)
        else:
            self.otpsent_label.setText('Invalid OTP!')

    def password_update_(self):
        try:
            conn = psycopg2.connect(
                host='ec2-18-206-20-102.compute-1.amazonaws.com',
                database='ddeuc850qat336',
                user='gnmwvfusjgondu',
                password='d24dd511d794c7214bec9c67be92740279caabac4cb8e08f4769f49de27b580e',
                port='5432')
            cur = conn.cursor()
            varNewPass = self.newpassword_field.text()
            cur.execute("UPDATE logindetails SET password = '{}' WHERE mobileno = '{}'".format(varNewPass,self.mobile_field.text()))
            conn.commit()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Password Is Updated Successfully")
            msg.setWindowTitle("Success")
            msg.exec_()

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f"Error Ocured Due To {str(e)}")
            msg.setWindowTitle("Error")
            msg.exec_()

        finally:
            cur.close()
            conn.close()

    def retranslateUi(self, ForgotPass):
        _translate = QtCore.QCoreApplication.translate
        ForgotPass.setWindowTitle(_translate("ForgotPass", "Forgot Password"))
        self.label.setText(_translate("ForgotPass", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Forgot Your Password ?</span></p></body></html>"))
        self.enter_label.setText(_translate("ForgotPass", "<html><head/><body><p><span style=\" font-size:16pt;\">Enter Your </span></p><p><span style=\" font-size:16pt;\">Mobile Number</span></p></body></html>"))
        self.enterotp_label.setText(_translate("ForgotPass", "<html><head/><body><p><span style=\" font-size:16pt;\">Enter OTP</span></p></body></html>"))
        self.label_2.setText(_translate("ForgotPass", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter Your New Password</span></p></body></html>"))
        self.otpsent_label.setText(_translate("ForgotPass", "<html><head/><body><p><br/></p></body></html>"))
        self.sendotp_btn.setText(_translate("ForgotPass", "Send OTP"))
        self.checkotp_btn.setText(_translate("ForgotPass", "Check OTP !"))
        self.change_password_btn.setText(_translate("ForgotPass", "Change Password !"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgotPass = QtWidgets.QMainWindow()
    ui = Ui_ForgotPass()
    ui.setupUi(ForgotPass)
    ForgotPass.show()
    sys.exit(app.exec_())
