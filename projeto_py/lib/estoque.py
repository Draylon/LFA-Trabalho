import os,sys,time
from projeto_py.mecanica.fita import set_index
from projeto_py.mecanica.fita import index_current
from projeto_py.mecanica.fita import index_up
from projeto_py.mecanica.automato import *

class Estoque:
    def __init__(self):
        self.movimento = False
        self.estoque = []
        self.automato = Automato("estoque.txt")
        self.shut = False

    def mainthread(self,blop,obj_list):
        #reler fita
        #pegar self.automato e avaliar fita
        while not self.shut:
            if len(obj_list[0].fita_list) > self.ultimaFita_len:
                print("estoque reading updates")
                
                final = self.automato.avaliar_fita(obj_list[0],"estado_final")
                new_fita = self.automato.avaliar_fita(obj_list[0],"fita_saida")
                obj_list[0].fita_list = new_fita
                if final == "init_1":
                    obj_list[0].add_fita("prod_peca1")
                if final == "init_2":
                    obj_list[0].add_fita("prod_peca2")

                self.ultimaFita_len = len(obj_list[0].fita_list)
        print("FML")
        time.sleep(3)

    def consulta_componente(self,id_peca):
        if self.estoque[id_peca]:
            return True
        else:
            return False

    
    def print_ab(self):
        return ("Estoque")