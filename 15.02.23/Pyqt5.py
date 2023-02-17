from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QIcon,QFont

# # 1 Problem
# app = QApplication([])
# oyna = QWidget()
# oyna.setWindowTitle("Ism-Familiya")
# oyna.setGeometry(1000,450,500,500)

# ism = QLabel('',oyna)
# ism.setText("Saloxiddin")
# ism.setFont(QFont("Times",15))

# familiya = QLabel('',oyna)
# familiya.setText("Sunnatov")
# familiya.setFont(QFont("Times",15))
# familiya.move(0,33)

# yosh = QLabel('',oyna)
# yosh.setText("19")
# yosh.setFont((QFont("Times",15)))
# yosh.move(0,65)

# oyna.show()
# app.exec_()


# 2 Problem

app = QApplication([])
oyna = QWidget()
oyna.setGeometry(1000,450,500,500)

name = QLabel('Ism:',oyna)
name.setFont(QFont("Times",10))

surname = QLabel("Familiya:",oyna)
surname.setFont(QFont("Times",10))
surname.move(0,30)

btn = QPushButton("OK",oyna)
btn.setGeometry(10,63,40,40)

result = QLabel('RESULT: ',oyna)
result.setGeometry(80,58,50,50)

name_edit = QLineEdit('',oyna)
name_edit.move(35,0)

surname_edit = QLineEdit('',oyna)
surname_edit.setGeometry(70,30,130,25)


oyna.show()
app.exec_()


