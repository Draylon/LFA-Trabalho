import os,sys,time
from projeto_py.mecanica.fita import set_index
from projeto_py.mecanica.fita import index_current
from projeto_py.mecanica.fita import index_up

class Estoque:
    def __init__(self):
        self.movimento = False
        self.estoque = []

    def mainthread(self,blop,obj_list):
        while obj_list[0].valid:
            prg = set_index()
            while index_current(prg) < len(obj_list[0].fita_list):
                print(obj_list[0].fita_list)
                if obj_list[0].query_fita(prg) == "shut":
                    obj_list[0].switch_valid()
                    break
                if obj_list[0].query_fita(prg) == "peca1":
                    #tem componentes da peca 1 no estoque?
                    if self.consulta_componente("peca1"):
                        #esteira andando?
                        if obj_list[2].esteira_status():
                            # parar esteira ( escrever : fita geral pra parar a esteira )
                            if obj_list[0].endoftape(prg):
                                print("esteira.parar()")
                        else:
                            # colocar na esteira ( escrever : há componente a caminho na esteira )
                            if obj_list[0].endoftape(prg):
                                print("estoque.add_component()") #de estoque para esteira
            print("estoque_loop")
            time.sleep(3)

    def consulta_componente(self,id_peca):
        if self.estoque[id_peca]:
            return True
        else:
            return False

    
    def print_ab(self):
        return ("Estoque")