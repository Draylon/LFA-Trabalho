import os
import sys
import logging
import threading
import time

sys.path.append(os.path.dirname("../"))
sys.path.append(os.path.dirname(".."))

from projeto_py.lib.componente import *
from projeto_py.lib.esteira import *
from projeto_py.lib.manutencao import *
from projeto_py.lib.peca import *
from projeto_py.lib.qualidade import *
from projeto_py.lib.torno import *

def thread_function(name,dlp):
    logging.info("Thread %s: starting", name)
    print(dlp.print_ab())
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

def produzir_peca(tipo_peca):
    peca = Peca()
    return peca

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig( format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,produzir_peca(1)))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
