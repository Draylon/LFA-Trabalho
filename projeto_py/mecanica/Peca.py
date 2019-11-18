import os,sys,time
from projeto_py.mecanica.fita import set_index
from projeto_py.mecanica.fita import index_current
from projeto_py.mecanica.fita import index_up
from projeto_py.mecanica.automato import *

class Estoque:
    def __init__(self):
        self.movimento = False
        self.estoque = []
        self.automato = Automato()
        self.shut = False

    def mainthread(self,blop,obj_list):
        #reler fita
        #pegar self.automato e avaliar fita
        while not self.shut:
            if len(obj_list[0].fita_list) > self.ultimaFita_len:
                print("Peca reading updates")
                self.ultimaFita_len = len(obj_list[0].fita_list)
        print("FML")
        time.sleep(3)

    def consulta_componente(self,id_peca):
        if self.estoque[id_peca]:
            return True
        else:
            return False

    
    def print_ab(self):
        return ("Peca")