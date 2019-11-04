import os
import sys
import logging
import threading
import time

sys.path.append(os.path.dirname("../"))
sys.path.append(os.path.dirname(".."))

from projeto_py.lib.componente import *
from projeto_py.lib.estoque import *
from projeto_py.lib.esteira import *
from projeto_py.lib.manutencao import *
from projeto_py.lib.peca import *
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
    esteira = Esteira()
    #torno = Torno()
    #qualidade = Qualidade()
    #manutencao = Manutencao()
    peca = Peca()
    componente = Componente()
    fita = Fita()

                     #0      1      2       3      4         5           6
    lista_objects = [fita,estoque,esteira,"ayylmao"]#,torno,qualidade,manutencao,componente]

    estoque_thread = threading.Thread(target=estoque.mainthread, args=(1,lista_objects))
    esteira_thread = threading.Thread(target=esteira.mainthread, args=(1,lista_objects))
    #torno_thread = threading.Thread(target=torno.mainthread, args=(lista_objects))
    #qualidade_thread = threading.Thread(target=qualidade.mainthread, args=(lista_objects))
    #manutencao_thread = threading.Thread(target=manutencao.mainthread, args=(lista_objects))
    #componente_thread = threading.Thread(target=componente.mainthread, args=(lista_objects))
    
    estoque_thread.start()
    esteira_thread.start()
    #torno_thread.start()
    #qualidade_thread.start()
    #manutencao_thread.start()
    #componente_thread.start()
    print("inicializado")
    time.sleep(5)
    fita.add_fita("peca1")
    print("gravado na fita")
    time.sleep(6)
    fita.add_fita("shut")
    #while x.isAlive():
    #   print("Ayy Lmao")
    #   indml = input()
    #   print(indml)
    # x.join()

