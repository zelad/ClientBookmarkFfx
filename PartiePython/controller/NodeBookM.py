#!/usr/bin/python
# -*- coding:Utf-8 -*-
'''
Created on 15 févr. 2016

@author: Kiki
'''
import json

class NodeBookM(object):
    '''
    classdocs
    '''
    def __init__(self,node):
        '''
        Constructor
        '''
#         self.nom = ""
#         self.prenom = ""
        
        self.title = ""
        self.type = ""
        
        self.index = -1
        self.dateAdded = -1
        self.lastModified = -1
        self.id = -1
        
        self.uri = ""
        self.tags = ""
        
        self.annos = dict()
        self.children = dict()
#@ICI compléter en fonction du type de node
        
        if node['type'].find('text/x-moz-place-container') != -1:
            pass
        elif node['type'].find('text/x-moz-place-separator') != -1:
            pass
        elif node['type'].find('text/x-moz-place') != -1: 
            pass
        else:
            print ('soucis dans le décodage des "NodeBookM"')