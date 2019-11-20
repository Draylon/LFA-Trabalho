class Automato:
    def __init__(self,dir):
        funcaoprograma = []
        f = open(dir,"r+")
        fl = f.readlines()
        inicial = fl[0].strip()
        estados = fl[1].strip()
        transicoes = fl[2].strip()

        for i in range(len(fl)-4):
            if len(fl[i+3].strip()) > 0:
                proc_transic = fl[i+3].strip().split("->")
                p_1 = proc_transic[0].split(",")
                for i in range(len(p_1)):
                    p_2 = p_1[i].split(";")
                    p_3 = p_2[1].split("&")
                    #funcaoprograma.append({"de": p_2[0],"simbolo":p_2[1],"para":transicoes[1]})
                    try:
                        funcaoprograma.append([p_2[0].strip(),p_3[0].strip(),p_3[1].strip(),proc_transic[1].strip()])
                    except IndexError:
                        funcaoprograma.append([p_2[0].strip(),p_3[0].strip(),"",proc_transic[1].strip()])
                    
        terminais = fl[len(fl)-1].strip()
        f.close()
        self.estados = estados
        self.transicoes = transicoes
        self.FP = funcaoprograma
        self.inicial = inicial
        self.terminais = terminais
    
    def print_ff(self):
        print(self.inicial)
        print(self.estados)
        print(self.FP)
        print(self.terminais)
    
    def avaliar_fita(self,fita,mode):
        terminais_alcancados = []
        c_estado = self.inicial
        fita_saida = []
        break_transicao = False
        for item in fita.fita_list:
            if mode == "estado_final" and item not in self.transicoes:
                continue
            progresso=False

            for i in self.FP:
                if c_estado == i[0] and item == i[1]:
                    #print(c_estado,"com",item,"indo para",i[2],end="\n")
                    if i[2] != "":
                        fita_saida.append(i[2])
                    c_estado = i[3]
                    progresso=True
                    break

            if mode == "fita_saida" and not progresso:
                fita_saida.append(item)
                continue

            if not progresso and mode == "estado_final":
                break_transicao=True
                break
        
        if mode == "estado_final":
            if not break_transicao:
                return c_estado
            else:
                return ""
        elif mode == "fita_saida":
            return fita_saida

if __name__ == "__main__":
    import sys,os
    sys.path.append(os.path.dirname("../"))
    sys.path.append(os.path.dirname(".."))
    from projeto_py.mecanica.fita import *
    d=Automato(sys.argv[1])
    print(d.avaliar_fita(Fita("peca1,ayy,peca1,peca1,peca2"),"estado_final"))
    print(d.avaliar_fita(Fita("peca1,ayy,peca1,peca1,peca2"),"fita_saida"))