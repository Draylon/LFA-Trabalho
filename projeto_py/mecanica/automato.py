class Automato:
    def __init__(self,estados,funcaoprograma,inicial,terminais):
        self.estados = estados
        self.FP = funcaoprograma
        self.inicial = inicial
        self.terminais = terminais


    
    def avaliar_fita(self,fita):
        terminais_alcancados = []
        c_estado = [self.inicial]
        for item in fita.fita_list:
            cn_s = []
            for i in c_estado:
                cn_s.append(FP[c_estado][item])
            c_estado = cn_s
            
        for i in c_estado:
            if i in self.terminais:
                terminais_alcancados.append(i)
        return terminais_alcancados