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
        self.type = node['type']
        
        self.index = node['index']
        self.dateAdded = node['dateAdded']
        self.lastModified = node['lastModified']
        self.id = node['id']
        
        self.uri = ""
        self.tags = ""
        
        self.annos = list()#A déterminer si je vais m en servir ou pas...
        self.children = list()
        
        if self.type.find('text/x-moz-place-container') != -1:
        #Ici nous avons un dossier
            self.title = node['title']
            if node.has_key('children'):
                for node in node['children']:
                    self.children.append(NodeBookM(node))
            
        elif self.type.find('text/x-moz-place-separator') != -1:
        #Ici un séparateur
            pass
        
#         elif node['type'].find('text/x-moz-place') != -1:
        elif self.type.find('text/x-moz-place') != -1:
        #Et ici un favoris 
            self.title = node['title']
            if node.has_key('uri'):
                self.uri = node['uri']
            if node.has_key('tags'):
                self.tags = node['tags']
        else:
            print ('soucis dans le décodage des "NodeBookM"')