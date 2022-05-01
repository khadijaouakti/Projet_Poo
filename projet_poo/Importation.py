#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 06:50:02 2022

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

# hostname = "10.188.191.76"
# username = "Myje"
# password = "myje"
# port = 22

acceuil = None

from Creation import Creation

class Importation(QWidget):
   
    def __init__(self,acceuil):
        super().__init__()
        
        self.acceuil = acceuil
        
        layout = QGridLayout()
        self.setWindowTitle("Importation")
        self.resize(500, 300)
        
        self.b1 = QPushButton("Afficher")
        layout.addWidget(self.b1,0,1)
        self.b1.setFixedWidth(100)
        self.b1.setToolTip("Cliquer pour afficher le dossier")
        self.b1.clicked.connect(self.Afficher)
        
        
        self.b2 = QPushButton("Selectionner")
        layout.addWidget(self.b2,0,2)
        self.b2.setFixedWidth(100)
        self.b2.setToolTip("Cliquer pour selectionner le dossier")
        self.b2.clicked.connect(self.Selectionner(self.acceuil))
        
        
        self.liste =  QComboBox()
        layout.addWidget(self.liste,0,0)
        self.liste.setFixedWidth(200)
        
        self.b3 = QPushButton("Retour")
        layout.addWidget(self.b3,1,0)
        self.b3.setFixedWidth(100)
        self.b3.clicked.connect(self.Fermer)
        
      
        
        self.b4 = QPushButton("Créer le dossier")
        layout.addWidget(self.b4,1,2)
        self.b4.setFixedWidth(150)
        self.b4.clicked.connect(self.creation)
        self.b4.setToolTip("Cliquer pour créer le dossier")
        self.b4.clicked.connect(self.Creer(self.acceuil))
        
        
        
        self.setLayout(layout)
        self.show()
        
        
        
    def Retour(self):
        self.hide()
        self.acceuil.show()
        
    def creation(self,acceuil):
        self.hide()
        self.Creationn = Creation(acceuil)
        

        
print(__name__)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # model = Model()
    # ctrl = Controller(model)
    # hostname = "192.168.1.78"
    # username = "etudiant"
    # password = "vitrygtr"
    # port = 22
    
    Impor = Importation(acceuil)
    
    sys.exit(app.exec_())
        
        
        
        
        
   