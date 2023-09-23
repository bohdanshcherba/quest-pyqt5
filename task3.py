from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

app = QApplication([])
my_win = QWidget()
my_win.resize(500, 500)
title = QLabel("Натисни щоб дізнатися переможця")
number = QLabel("?")

btn = QPushButton("Generate number")
line = QVBoxLayout()
line.addWidget(title, alignment=Qt.AlignCenter)
line.addWidget(number, alignment=Qt.AlignCenter)
line.addWidget(btn, alignment=Qt.AlignCenter)

my_win.setLayout(line)

my_win.show()
app.exec_()
