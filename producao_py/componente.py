class Esteira:
    def __init__(self, aa, bb):
        self.aa1 = aa
        self.bb1 = bb

    def print_ab(self):
        return (self.aa1 + self.bb1)

p1 = Esteira("Auto", "mato")
print (p1.print_ab())