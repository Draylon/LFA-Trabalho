import os,sys,time
from projeto_py.mecanica.fita import set_index
from projeto_py.mecanica.fita import index_current
from projeto_py.mecanica.fita import index_up
from projeto_py.mecanica.automato import *

class Torno:
    def __init__(self):
        self.automato = Automato("projeto_py/mecanica/automatos/torno.txt")
        self.shut = False

    def mainthread(self,blop,obj_list,ddl):
        #reler fita
        #pegar self.automato e avaliar fita
        while not self.shut:
            print("\n\ntorno reading updates")
            print(obj_list[0].fita_list)

            new_fita = self.automato.avaliar_fita(obj_list[0],"fita_saida")
            final = self.automato.avaliar_fita(obj_list[0],"estado_final")
            print(final)
            print(new_fita)
            obj_list[0].fita_list = new_fita
            
            if final == "chegar_cmp":
                obj_list[0].add_fita("cmp_alinhado_qualt")

            if final == "parar_esteira":
                obj_list[0].add_fita("parar_esteira")

            if final == "movimentar_esteira":
                obj_list[0].add_fita("libera_esteira")

            if final == "pegar_cmp":
                obj_list[0].add_fita("cmp_recolhido")
            
            if final == "cmp_na_quald":
                obj_list[0].add_fita("processar_cmp")
            
            if final == "processando_cmpq":
                obj_list[0].add_fita("cmp_passa")
            
            if final == "sign_torno":
                obj_list[0].add_fita("qualidade_load")

            time.sleep(ddl)

    def print_ab(self):
        return ("torno")