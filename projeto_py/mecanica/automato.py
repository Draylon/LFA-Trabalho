class Automato:
    def __init__(self,dir):
        funcaoprograma = []
        f = open(dir,"r+")
        fl = f.readlines()
        inicial = fl[0].strip()
        estados = fl[1].strip()
        for i in range(len(fl)-3):
            transicoes = fl[i+2].split("->")
            p_1 = transicoes[0].split(",")
            for i in range(len(p_1)):
                p_2 = p_1[i].split(";")
                #funcaoprograma.append({"de": p_2[0],"simbolo":p_2[1],"para":transicoes[1]})
                funcaoprograma.append([p_2[0].strip(),p_2[1].strip(),transicoes[1].strip()])
        terminais = fl[len(fl)-1].strip()
        f.close()
        self.estados = estados
        self.FP = funcaoprograma
        self.inicial = inicial
        self.terminais = terminais
    
    def print_ff(self):
        print(self.inicial)
        print(self.estados)
        print(self.FP)
        print(self.terminais)
    
    def avaliar_fita(self,fita):
        terminais_alcancados = []
        c_estado = self.inicial
        for item in fita.fita_list:
            progresso=False
            for i in self.FP:
                if c_estado == i[0] and item == i[1]:
                    #print(c_estado,"com",item,"indo para",i[2],end="\n")
                    c_estado = i[2]
                    progresso=True
                    break
            if not progresso:
                break
            
        for i in c_estado:
            if i in self.terminais:
                terminais_alcancados.append(i)
        return terminais_alcancados


if __name__ == "__main__":
    import sys,os
    sys.path.append(os.path.dirname("../"))
    sys.path.append(os.path.dirname(".."))
    from fita import *
    d=Automato(sys.argv[1])
    print("".join(d.avaliar_fita(Fita("a,a,b"))))