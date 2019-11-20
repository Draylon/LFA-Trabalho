import os,sys,time
from projeto_py.mecanica.fita import set_index
from projeto_py.mecanica.fita import index_current
from projeto_py.mecanica.fita import index_up
from projeto_py.mecanica.automato import *

clear = lambda: os.system('cls') #on Windows System
class Controle:
    def __init__(self):
        self.automato = Automato("projeto_py/mecanica/automatos/gerente.txt")
        self.shut = False

    def mainthread(self,blop,obj_list,ddl):
        #reler fita
        #pegar self.automato e avaliar fita
        while not self.shut:
            clear()
            print("controle reading updates")

            print(obj_list[0].fita_list)
            final = self.automato.avaliar_fita(obj_list[0],"estado_final")
            new_fita = self.automato.avaliar_fita(obj_list[0],"fita_saida")
            print(final)
            print(new_fita)
            obj_list[0].fita_list = new_fita
            if final == "init_1":
                obj_list[0].add_fita("prod_peca1")
            if final == "init_2":
                obj_list[0].add_fita("prod_peca2")
            time.sleep(ddl)
        print("controle shut down")

    
    
    def print_ab(self):
        return ("Controle")