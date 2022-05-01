#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 01:07:44 2022

@author: didij
"""
import sys
import numpy as np
import os
from paramiko import client
from PyQt5 import QtCore
from PyQt5.QtGui import QIntValidator
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import ( QTextEdit,QLineEdit,QComboBox ,QRadioButton,  QDialog,QSpinBox,  QDialogButtonBox, 
                             QFormLayout, QGridLayout, QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout,
                             QApplication, QWidget, QLabel)


acceuil = None
Creationn = None
# SCP = None

# hostname = "10.188.191.76"
# username = "Myje"
# password = "myje"
# port = 22


        
class Historique(QWidget):
    def __init__(self,acceuil):
        super().__init__()
        
        self.acceuil = acceuil
        
        layout = QGridLayout()
        self.setWindowTitle("Histoqrique")
        self.resize(500, 300)
        self.l4 = QLabel("Nom")        
        self.nom = QLineEdit()
        self.nom.setFixedWidth(300)
        layout.addWidget(self.l4,0,0)
        layout.addWidget(self.nom,0,1)
        
        self.l5 = QLabel("Prenom")
        self.prenom = QLineEdit()
        self.prenom.setFixedWidth(300)        
        layout.addWidget(self.l5,1,0)
        layout.addWidget(self.prenom,1,1)
        
        self.l6 = QLabel("Age")
        self.age = QSpinBox()
        self.age.setFixedWidth(300)
        layout.addWidget(self.l6,2,0)
        layout.addWidget(self.age,2,1)
        
        self.z1 = QLineEdit()
        self.z1.setFixedWidth(200)
        self.z1.setFixedHeight(200)
        layout.addWidget(self.z1,4,1)
        
        self.b3 = QPushButton("Fermer")
        layout.addWidget(self.b3,5,1)
        self.b3.setFixedWidth(100)
        self.b3.setToolTip("Cliquer pour fermer la fenetre")
       
        
        self.setLayout(layout)
        self.show()
        
        # def Fermer(self):
        #     self.hide()
        #     self.acceuil.show()
            

        
    
        
    
        
print(__name__)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # model = Model()
    # ctrl = Controller(model)
    Histo = Historique(Creationn)
    Creationn = Creation(acceuil)
    
    sys.exit(app.exec_())
        

        
        
