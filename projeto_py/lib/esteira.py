import os,sys,time
from projeto_py.mecanica.fita import set_index
from projeto_py.mecanica.fita import index_current
from projeto_py.mecanica.fita import index_up
from projeto_py.mecanica.automato import *
class Esteira:
    def __init__(self):
        self.automato = Automato("projeto_py/mecanica/automatos/esteira.txt")
        self.ultimaFita_len = 0
        self.shut = False

    def mainthread(self,blop,obj_list,ddl):
        #reler fita
        #pegar self.automato e avaliar fita
        while not self.shut:
            print("\n\nesteira reading updates")

            print(obj_list[0].fita_list)
            final = self.automato.avaliar_fita(obj_list[0],"estado_final")
            new_fita = self.automato.avaliar_fita(obj_list[0],"fita_saida")
            print(final)
            print(new_fita)
            obj_list[0].fita_list = new_fita

            if final == "parar_esteira":
                self.parar()

            if final == "andando":
                self.mover()

            time.sleep(ddl)
        print("esteira shut down")

    #===========================

    def esteira_get(self):
        return self.movimento

    def parar(self):
        self.movimento = False

    def mover(self):
        self.movimento = True

    def print_ab(self):
        return ("esteira")