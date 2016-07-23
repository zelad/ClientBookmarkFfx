#!/usr/bin/python
# -*- coding:Utf-8 -*-
'''
Created on 15 janv. 2016

@author: Kiki
@note: inspiration WebSocket ici: https://pypi.python.org/pypi/websocket-server/0.4
@note: ou: https://github.com/Pithikos/python-websocket-server
@note: test le 29/01 pour changement de map dossier de GitH
'''
from websocket_server import WebsocketServer
import json
import os
import sqlite3 as lite
import sys

from NodeBookM import NodeBookM

# global switch
# global NodeBookM
def setDB(node,cur):
    
    if node['type'].find('text/x-moz-place-container') != -1:
    #Ici nous avons un dossier
    #TEMP: un p tit test pour gitLab
#@ICI: construire un string avec les champs correspondant à la ligne ci-dessous
        cur.execute("INSERT INTO folder (title, position, dateAdded, lastModified, parent) VALUES ()")
#         dictTreeNode['label'] = node['title']
        if node.has_key('children'):
            for node in node['children']:
                setDB(node, cur)
    elif node['type'].find('text/x-moz-place-separator') != -1:
    #ici nous avons un séparateur
        pass
    elif node['type'].find('text/x-moz-place') != -1:
    #et ici un favoris, "bookMark" pour la base
        pass
    
def laboSQLite(node):
    con = lite.connect('bookMark.db')
    with con:
        cur = con.cursor()
        setDB(node, cur)
#<unExemple>
#     with con:
#         cur = con.cursor()
#     #Ci Dessous: on va pas se faire kiki je vais utiliser "SQLite Manager" Add-on de FireFox!! 
#         #cur.execute("CREATE TABLE bookMarks(Guid TEXT, Name TEXT, Price INT)")
#         cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
#</unExemple>


def serialTreeNode(node):
        dictTreeNode = dict()
        children = list()
        
        if node['type'].find('text/x-moz-place-container') != -1:
        #Ici nous avons un dossier
            dictTreeNode['label'] = node['title']
            if node.has_key('children'):
                for node in node['children']:
                    children.append(serialTreeNode(node))
                dictTreeNode['children'] = children
        elif node['type'].find('text/x-moz-place-separator') != -1:
            dictTreeNode['label'] = "___"
        elif node['type'].find('text/x-moz-place') != -1:
            dictTreeNode['label'] = node['title']
        return dictTreeNode
    
def getNodeBookM(listNodesBookM):
#     dictObjNodeBookM = dict()
    listObjNodeBookM = list()
    listObjNodeTree = list()
    for node in listNodesBookM:
    #version dico
#         strNode = str(node['guid'])
#         dictObjNodeBookM[strNode] = NodeBookM(node)
    #version Liste
        #Création des objets node, contenant tous les infos des favoris
        listObjNodeBookM.append(NodeBookM(node))
        #Version sérialisé pour transmission au client
        listObjNodeTree.append(serialTreeNode(node))
    return listObjNodeBookM, listObjNodeTree

def getJson(file):
    with open(file) as data_file:#test de lecture de sav FireFox 
        data = json.load(data_file)
    return  data

def new_client(client, server):
    global wsIHM
    wsIHM = client
    print "client connecte"
    
def rxMessage(client, server, message):
#     print message
    ihmRouting(message, server)
    
def clientLeft(client, server):
    print "le client:"
    print client
    print "est partie"
    
'''
Fonction de routage des message entrants
'''    
def ihmRouting(message, server):
#     objDict = ast.literal_eval(message) //pour compatibilité avec Android
    objDict = json.loads(message)
    func = switch[objDict["sendType"]]
    func(message, server)

def doLogin(message, server):
    global jsonTree
    global wsIHM
# Envoie de l arborésence des favoris au Client
    server.send_message(wsIHM, jsonTree)
#     obj = ast.literal_eval(message) //pour compatibilité avec Android
#     print message //aucune idée pourquoi mais il faut mettre cela pour que ça fonctionne avec Android!!?
#     obj = json.loads(message)
#     objLogin = obj["object"]
#     NodeBookM.nom = objLogin["name"]
#     NodeBookM.prenom = objLogin["firstname"]
    #Ack client
#     dict={}
#     dict["messageType"]="ackLogin"
#     objJson = json.dumps(dict)
#     server.send_message(wsIHM, objJson)
    
if __name__ == "__main__":
# Fixation du point de lecture de fichier
    os.chdir('../')#Obligation de donner le chemin du fichier avec le QPython
# routage des messages receptionnes    
    switch={
        "login":doLogin
    }
# Initialisation des models
    # Récupération du Json
    jsonData = getJson('bookmarks.json')
    barPersonal = jsonData['children'][14]['children']
    nodesBM, tree = getNodeBookM(barPersonal)
    #Passage en Json pour envoie au client
    dictTree = dict()
    dictTree['treeBookMark'] = tree
    dictTree['messageType'] = "treeForShow"
    jsonTree = json.dumps(dictTree)
#     jsonToDictForTest = json.loads(jsonTree)
    
# Connexion au client web
    server = WebsocketServer(9999)
    server.set_fn_new_client(new_client) #définition de la fonction pour l arrivé d un nouveau client
    server.set_fn_message_received(rxMessage) #Définition de la fonction pour l arrivé d un nouveau message
    server.set_fn_client_left(clientLeft) #définition de la fonction pour la déconnexion d'un client
    
    server.run_forever()

