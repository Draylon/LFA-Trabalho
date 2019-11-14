import os,sys,time
from projeto_py.mecanica.fita import set_index
from projeto_py.mecanica.fita import index_current
from projeto_py.mecanica.fita import index_up
from projeto_py.mecanica.automato import *

class Controle:
    def __init__(self):
        self.automato = Automato()#controle.txt
        self.ultimaFita_len = 0
        self.shut = False

    def mainthread(self,blop,obj_list):
        #reler fita
        #pegar self.automato e avaliar fita
        while not self.shut:
            if obj_list[0].fita_len() > self.ultimaFita_len:
                print("controle reading updates")
                self.ultimaFita_len = obj_list[0].fita_len()
        print("FML")
        time.sleep(3)

    
    
    def print_ab(self):
        return ("Controle")