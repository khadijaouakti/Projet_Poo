#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 01:20:43 2022

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


from Historique import Historique 

acceuil = None

class Creation(QWidget):
    fermeturefen2 = QtCore.pyqtSignal()
   
    def __init__(self,acceuil, n = "",p = "", s = "", a = ""):
        super().__init__()
        
        self.name=n
        self.first_name=p
        self.gender=s
        self.years=a
        print(self.gender)
        
        self.acceuil = acceuil
        #chemin et nom fichier
        # self.machine_file = first_name +"_"+ name +"_"+ years +"_"+ gender +"_.txt"
        # self.virtual_file = "/home/myje/" + self.machine_file
        # self.setToolTip("")
        # self.first_name = first_name
        # self.name = name
        # self.years = years
        # self.gender = gender
        # print(self.gender)
        
        
        self.setWindowTitle("Création de dossier")
        self.resize(500, 300)
       # # Create a QFormLayout instance
       #  # self.layout = QFormLayout()
        layout = QGridLayout()
        self.l1 = QLabel("Nom")        
        self.nom = QLineEdit()
        self.nom.setFixedWidth(300)
        layout.addWidget(self.l1,0,0)
        layout.addWidget(self.nom,0,1)
        
        self.l2 = QLabel("Prenom")
        self.prenom = QLineEdit()
        self.prenom.setFixedWidth(300)        
        layout.addWidget(self.l2,1,0)
        layout.addWidget(self.prenom,1,1)
        
        self.l3 = QLabel("Age")
        self.age = QLineEdit()
        self.age.setFixedWidth(300)
        layout.addWidget(self.l3,2,0)
        layout.addWidget(self.age,2,1)
          # Add widgets to the layout
        self.r1 = QRadioButton("Male")
        layout.addWidget(self.r1,3,0)
        
        self.r2 = QRadioButton("Female")
        layout.addWidget(self.r2,3,1)
        
        self.b4 = QPushButton("Historique")       
        layout.addWidget(self.b4,1,3)
        self.b4.setFixedWidth(100)
        self.b4.clicked.connect(self.historique)
        
                
        
        
        #zone de texte pour medecin 
        self.l4=QLabel("Symptômes du patient : ")
        layout.addWidget(self.l4,4,1)
        self.z1 = QTextEdit()
        self.z1.setFixedWidth(200)
        self.z1.setFixedHeight(200)
        layout.addWidget(self.z1,5,1)
        # self.z1.textChanged.connect(self.medicament)            

        self.l5=QLabel("Ordonnance: ")
        layout.addWidget(self.l5,4,2)
        self.z2 = QTextEdit()
        self.z2.setFixedWidth(200)
        self.z2.setFixedHeight(200)
        layout.addWidget(self.z2,5,2)
        
        
        
        self.b2 = QPushButton("Enregistrer")
        layout.addWidget(self.b2,6,1)
        self.b2.setFixedWidth(100)
        # self.b2.clicked.connect(self.Enregistrement)
        
        
        
        self.b3 = QPushButton("Fermer")
        layout.addWidget(self.b3,6,2)
        self.b3.setFixedWidth(100)
        self.b3.setToolTip("Cliquer pour fermer la fenetre")
        # self.b3.clicked.connect(self.Fermer)
        
        
        
       
        
        
        self.setLayout(layout)
        self.show()
        
    
            
    def Fermer(self):
        self.hide()
        self.Acceuil = Acceuil(Creationn)
    def closeEvent(self, event):
        """à la fermeture de cette fenêtre 2, celle-ci envoie un signal à la 
           fenêtre 1 appelante
        """
        self.fermeturefen2.emit() 
        event.accept()
         
    def historique(self,Creationn):
          
            self.hide()
            self.Histo = Historique(Creationn)
            
    def Dossier_enre(self):
        self.name = self.nom.text()
        self.first_name = self.prenom.text()
        self.years = self.age.text()
        
        if self.r1.isChecked():
            self.gender = "homme"
            
        elif self.r2.isChecked():
                self.gender = "femme"
                
        else:
            self.gender = ""
            
        if (self.neme =="" or self.first_neme =="" or self.years=="" or self.gender ==""):
            
            self.b4.setToolTip("Veillez à remplir le formulaire avant de cliquer")
            self.b2.setToolTip("Veillez à remplir le formulaire avant de cliquer")
            return False
        else:
           
            self.b2.setToolTip("Cliquez pour enregistrer le fichier de "+ self.name +""+self.first_name)
            self.b1.setToolTip("liquez pour accéder à l'historique de " + self.name +""+self.first_name)
            
            return True
        
        def Enregistrement(self):
            
            fichier = [self.name,self.prenom,self.years,self.gender ]
            ajout = self.Dossier_enre()
            # self.fichier = self.name + "_" + self.prenom +"-"+ self.years +"_"+ self.gender +"_.txt"
            
            if ajout:
                with open(self.name + "_" + self.prenom+"_.txt","w+")as fich:
                    for i in fich:
                        print("Nom: {0}".format(self.nom.text()))
                        print("Prenom : {0}".format(self.prenom.currentText()))
                        print("Age : {0}".format(self.age.text()))
                        print("Sexe : {0}".format(self.sexe.text()))
            
            
            
                self.symptome="Symptome : "+self.z1.toPlainText()
                self.ordonnance="Ordonnance : "+self.z2.toPlainText()
            
                self.z1.clear()
                self.z2.clear()
            
            else:
                print("veullez résseyer")
                    
                        
                        
                        
                
            
        
            
            
            

            
            

    
    
    
print(__name__)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # model = Model()
    # ctrl = Controller(model)
    Creationn = Creation(acceuil)
    
    
    sys.exit(app.exec_())
            