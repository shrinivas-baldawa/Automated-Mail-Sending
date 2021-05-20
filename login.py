import psycopg2
from PyQt5.QtWidgets import QMessageBox
from registration import Ui_registration
from MainPage import Ui_MainPage
from finalForgotPassword import Ui_ForgotPass
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(581, 439)
        self.LoginWidget = QtWidgets.QWidget(LoginWindow)
        self.LoginWidget.setObjectName("LoginWidget")
        self.LoginLabel = QtWidgets.QLabel(self.LoginWidget)
        self.LoginLabel.setGeometry(QtCore.QRect(240, 50, 101, 51))
        self.LoginLabel.setObjectName("LoginLabel")
        self.UsernameLabel = QtWidgets.QLabel(self.LoginWidget)
        self.UsernameLabel.setGeometry(QtCore.QRect(40, 140, 121, 41))
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.password_label = QtWidgets.QLabel(self.LoginWidget)
        self.password_label.setGeometry(QtCore.QRect(40, 220, 121, 41))
        self.password_label.setObjectName("password_label")
        self.username_field = QtWidgets.QLineEdit(self.LoginWidget)
        self.username_field.setGeometry(QtCore.QRect(190, 150, 341, 31))
        self.username_field.setObjectName("username_field")
        self.password_field = QtWidgets.QLineEdit(self.LoginWidget)
        self.password_field.setGeometry(QtCore.QRect(190, 230, 341, 31))
        self.password_field.setObjectName("password_field")
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signin_btn = QtWidgets.QPushButton(self.LoginWidget, clicked=lambda:self.login_check())
        self.signin_btn.setGeometry(QtCore.QRect(40, 360, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.signin_btn.setFont(font)
        self.signin_btn.setObjectName("signin_btn")
        self.forgot_pass_btn = QtWidgets.QPushButton(self.LoginWidget, clicked=lambda :self.forgot_pass_redirect())
        self.forgot_pass_btn.setGeometry(QtCore.QRect(300, 300, 251, 41))
        self.forgot_pass_btn.setObjectName("forgot_pass_label")
        font1 = QtGui.QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.forgot_pass_btn.setFont(font1)
        self.label = QtWidgets.QLabel(self.LoginWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 581, 441))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Design/login.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.LoginLabel.raise_()
        self.UsernameLabel.raise_()
        self.password_label.raise_()
        self.username_field.raise_()
        self.password_field.raise_()
        self.signin_btn.raise_()
        self.forgot_pass_btn.raise_()
        LoginWindow.setCentralWidget(self.LoginWidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def login_check(self):
        conn = psycopg2.connect(
                host='ec2-18-206-20-102.compute-1.amazonaws.com',
                database='ddeuc850qat336',
                user='gnmwvfusjgondu',
                password='d24dd511d794c7214bec9c67be92740279caabac4cb8e08f4769f49de27b580e',
                port='5432')
        cur = conn.cursor()
        if self.username_field.text() == "" or self.password_field.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("All Fields Are Must")
            msg.setWindowTitle("Error")
            msg.exec_()

        elif self.username_field.text() == "adminemail@gmail.com" and self.password_field.text() == "admin":
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_registration()
            self.ui.setupUi(self.window)
            self.window.show()

        else:
            try:
                cur.execute("SELECT * FROM logindetails WHERE username = %s and password = %s",(self.username_field.text(),self.password_field.text()))
                row = cur.fetchone()
                if row == None:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Incorrct Details")
                    msg.setWindowTitle("Error")
                    returnVal = msg.exec_()
                else:
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_MainPage()
                    self.ui.setupUi(self.window)
                    self.window.show()
            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f"Error due to {str(e)}")
                msg.setWindowTitle("Error")
            finally:
                cur.close()
                conn.close()

    def forgot_pass_redirect(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ForgotPass()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.LoginLabel.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">LOGIN</span></p></body></html>"))
        self.UsernameLabel.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Username</span></p></body></html>"))
        self.password_label.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Password</span></p></body></html>"))
        self.signin_btn.setText(_translate("LoginWindow", "Sign In !"))
        self.forgot_pass_btn.setText(_translate("LoginWindow", "Forgot Password ?"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())