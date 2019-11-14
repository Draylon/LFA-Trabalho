class Fita:
    def __init__(self,string):
        self.fita_list = []
        self.valid = True
        if len(string) > 0:
            for i in range(len(string.split(","))):
                self.fita_list.append(string.split(",")[i])
    def switch_valid(self):
        if self.valid:
            self.valid = False
        else:
            self.valid=True

    def add_fita(self,elm):
        self.fita_list.append(elm)

    def endoftape(self,index):
        if index[0] == len(self.fita_list):
            return True
        else:
            return False
    
    def fita_len(self):
        return len(self.fita_list)

#=================================================

def index_up(prg):
    prg.insert(0,prg[0] + 1)
    prg.pop(1)

def set_index():
    fml =[]
    fml.append(0)
    return fml

def index_current(index):
    return index[0]
