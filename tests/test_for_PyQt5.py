# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:00:51 2022

@author: brknk
"""
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("Hello World!")
label.show()

app.exec_()
