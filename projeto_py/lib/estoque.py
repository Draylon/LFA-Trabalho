import os,sys,time
from projeto_py.mecanica.fita import set_index
from projeto_py.mecanica.fita import index_current
from projeto_py.mecanica.fita import index_up
from projeto_py.mecanica.automato import *

class Estoque:
    def __init__(self):
        self.movimento = False
        self.estoque = []
        self.automato = Automato("projeto_py/mecanica/automatos/estoque.txt")
        self.shut = False

    def mainthread(self,blop,obj_list,ddl):
        #reler fita
        #pegar self.automato e avaliar fita
        while not self.shut:
            print("\n\nestoque reading updates")
            
            print(obj_list[0].fita_list)

            final = self.automato.avaliar_fita(obj_list[0],"estado_final")
            new_fita = self.automato.avaliar_fita(obj_list[0],"fita_saida")
            print(final)
            print(new_fita)
            obj_list[0].fita_list = new_fita
            if final == "consulta_estoque":
                obj_list[0].add_fita("tem_cmp")

            if final == "colocar_componente":
                obj_list[0].add_fita("cmp_colocado")
            
            if final == "parar_esteira":
                obj_list[0].add_fita("parar_esteira")

            if final == "movimentar_esteira":
                obj_list[0].add_fita("libera_esteira")
            
            if final == "componente_set":
                obj_list[0].add_fita("qualidade_load")

            time.sleep(ddl)
        print("estoque shut down")

    def consulta_componente(self,id_peca):
        if id_peca in self.estoque:
            return True
        else:
            return False

    
    def print_ab(self):
        return ("Estoque")