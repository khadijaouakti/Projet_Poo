#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 09:59:33 2022

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




# class Historique(QDialog):
#     def __init__(self):
#         super(Historique,self).__init__()
#         self.setWindowTitle("Historique")

#importation de mes deux classes creation et importation 
from Creation import Creation
from Importation import Importation

class Acceuil(QWidget):
    def __init__(self):
        super().__init__()

        # self.myCtrl = ctrl
        
        #création des boutons
        self.b1 = QPushButton("Créer un dossier")
        self.b2 = QPushButton("Importer un dossier")
        
        
        #titre de la plateforme
        self.l = QLabel("Téléconsultation \n \n \n Bienvenue sur notre plateforme")
        #importation de l'image
        self.pixmap = QPixmap('Dossier-medi-logo copie.png')
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.label.setGeometry(320, 320, 600, 80)
        self.label.move(145,0)
        #chemin des boutons 
        self.b1.clicked.connect(self.creation)
        self.b2.clicked.connect(self.importation)
        self.init_ui()       
        self.show()
    
    def init_ui(self):
        
        h_box = QHBoxLayout()
        v_box = QVBoxLayout()
        
        self.setLayout(v_box)
        v_box.addWidget(self.l)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)
        h_box.addStretch()
        self.l.setAlignment(QtCore.Qt.AlignCenter)
        v_box.addLayout(h_box)
        self.setWindowTitle("Page d'acceuil")
        self.setGeometry(0, 0, 350, 280) 
    
   
        
    # def historique(self):
    #     pass

    #methodes qui permettre d'affichier les autres fenetres
       
    def creation(self,acceuil):
          
            self.hide()
            self.Creationn = Creation(acceuil)
            
            
    def importation(self,acceuil):
          
            self.hide()
            self.Impor = Importation(acceuil)
            
            
            
    
            
            
            
       
          
            
    
        


print(__name__)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # model = Model()
    # ctrl = Controller(model)
    # hostname = "10.188.191.76"#Maison
    # #hostname = "10.10.96.228"#ecole
    # username = "Myje"
    # password = "myje"
    # port = 22
    acceuil = Acceuil()
    
    sys.exit(app.exec_())
