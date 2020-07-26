#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 23:28:07 2020

@author: sams
"""
from file import file
class parcours(object):
    def __init__(self):
        self.Q1 = False
        self.Q2 = False
        self.Q3 = False
        self.Q4 = False
        self.Q5 = False
        self.Q6 = False
        self.credit_total = 0
        self.cours_valide = {}
        self.cours_echec = {}
        self.annee = 0
        
    def read_data(self,namefile):
        #methode de lecture de parcours
        
        try:
            f = file('parcours',namefile)
            f.read()
        except Exception:
            pass
    
    def write_data(self,namefile):
        #methode d'écriture de parcours
        try:
            f = file('parcours',namefile)
            f.write()
        except Exception:
            pass