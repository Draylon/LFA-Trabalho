class Esteira:
    def __init__(self):
        self.movimento = False
        
    def mainthread(self,blop,obj_list):
        print("ayy esteira\n")

    def processo(self,fita):
        for a in fita:
            print(a)

    def esteira_get(self):
        return self.movimento

    def parar(self):
        self.movimento = False

    def mover(self):
        self.movimento = True

    def print_ab(self):
        return ("esteira")