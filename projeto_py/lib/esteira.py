class Esteira:
    def __init__(self):
        self.automato = Automato()#controle.txt
        self.ultimaFita_len = 0
        self.shut = False

    def mainthread(self,blop,obj_list):
        #reler fita
        #pegar self.automato e avaliar fita
        while not self.shut:
            if len(obj_list[0].fita_list) > self.ultimaFita_len:
                print("esteira reading updates")
                self.ultimaFita_len = len(obj_list[0].fita_list)
        print("FML")
        time.sleep(3)

    #===========================

    def esteira_get(self):
        return self.movimento

    def parar(self):
        self.movimento = False

    def mover(self):
        self.movimento = True

    def print_ab(self):
        return ("esteira")