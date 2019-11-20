import os
import sys
import logging
import threading
import time

sys.path.append(os.path.dirname("../"))
sys.path.append(os.path.dirname(".."))

from projeto_py.lib.estoque import *
from projeto_py.lib.controle import *
from projeto_py.lib.esteira import *
from projeto_py.lib.parafusadeira import *
from projeto_py.lib.qualidade import *
from projeto_py.lib.torno import *
from projeto_py.mecanica.fita import *

def produzir_peca(tipo_peca):
    peca = Peca()
    return peca

def mg_engine(name,dlp):
    print("Thread Start")
    print(dlp.print_ab())
    time.sleep(15)
    print("Thread Finish")

if __name__ == "__main__":

    estoque = Estoque()
    controle = Controle()
    esteira = Esteira()
    torno = Torno()
    parafusadeira = Parafusadeira()
    qualidade = Qualidade()
    #peca = Peca()
    #componente = Componente()
    fita_geral = Fita("")
    producao = []
    ddl = 8
                         #0       1      2        3       4           5           6
    thread_list = []
    lista_objects = [fita_geral,estoque,controle,qualidade,esteira,torno,parafusadeira,thread_list]
    
    controle_thread = threading.Thread(target=controle.mainthread, args=(1,lista_objects,ddl))
    estoque_thread = threading.Thread(target=estoque.mainthread, args=(1,lista_objects,ddl))
    esteira_thread = threading.Thread(target=esteira.mainthread, args=(1,lista_objects,ddl))
    torno_thread = threading.Thread(target=torno.mainthread, args=(1,lista_objects,ddl))
    qualidade_thread = threading.Thread(target=qualidade.mainthread, args=(1,lista_objects,ddl))
    parafusadeira_thread = threading.Thread(target=parafusadeira.mainthread, args=(1,lista_objects,ddl))
    
    thread_list.append(controle_thread)
    thread_list.append(estoque_thread)
    thread_list.append(esteira_thread)
    thread_list.append(torno_thread)
    thread_list.append(qualidade_thread)
    thread_list.append(parafusadeira_thread)
    
    controle_thread.start()
    time.sleep(0.6)
    estoque_thread.start()
    time.sleep(0.6)
    esteira_thread.start()
    time.sleep(0.6)
    torno_thread.start()
    time.sleep(0.6)
    qualidade_thread.start()
    time.sleep(0.6)
    parafusadeira_thread.start()
    #componente_thread.start()
    
    while True:
       indml = input("Proximo comando:> ")
       fita_geral.add_fita(indml)
       if indml == "shut":
           controle.shut = True
           estoque.shut = True
           esteira.shut = True
           torno.shut = True
           qualidade.shut = True
           parafusadeira.shut = True
           break
