
class Node:
    def __init__(self, x, y, custo_g, custo_h, pai=None):
        self.x = x
        self.y = y
        self.custo_g = custo_g
        self. custo_h = custo_h
        self.custo_f = custo_g + custo_h
        self.pai = pai

    def __lt__(self, outro):
        return self.custo_f < outro.custo_f