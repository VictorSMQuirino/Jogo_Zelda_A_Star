from node import Node

class Agente:
    def __init__(self, pos_inicial, mapa):
        self.pos = pos_inicial
        self.mapa = mapa
        self.caminho = []

    def verifica_dungeon(self, dungeon):
        if dungeon == (24, 1):
            return [(14, 25), (15, 19)]
        elif dungeon == (39, 17):
            return [(13, 25), (13, 2)]
        else:
            return [(14, 26), (13, 3)]
    
    def distancia_manhattan(self, ponto1, ponto2):
        return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])
    
    def a_star(self, mapa, inicio, final):
        linhas, colunas = mapa.shape
        heap = []
        visitados = set()
        no_inicial = Node(inicio[0], inicio[1], 0, self.distancia_manhattan(inicio, final))
        #heapq.heappush(heap, no_inicial)
        heap.append(no_inicial)

        while heap:
            #no_atual = heapq.heappop(heap)
            heap = sorted(heap, key=lambda no: no.custo_f)
            no_atual = heap.pop(0)
            visitados.add(no_atual)

            if(no_atual.x, no_atual.y) == final:
                path = []
                while no_atual:
                    path.append((no_atual.x, no_atual.y))
                    no_atual = no_atual.pai
                return path[::-1]

            for vizinho in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = no_atual.x + vizinho[0]
                y = no_atual.y + vizinho[1]

                if (x >= 0 and x < linhas and y >= 0 and y < colunas and not self.verifica_visitado(x, y, visitados) and not self.verifica_heap(x, y, heap) and mapa[x, y] != 0):
                    custo_g = no_atual.custo_g + mapa[x, y]
                    custo_h = self.distancia_manhattan((x, y), final)
                    novo_no = Node(x, y, custo_g, custo_h, no_atual)
                    #heapq.heappush(heap, novo_no)
                    heap.append(novo_no)

        return None

    def verifica_visitado(self, x, y, visitados):
        for no in visitados:
            if no.x == x and no.y == y:
                return True
        return False    
                  
    def verifica_heap(self, x, y, heap):
        for no in heap:
            if no.x == x and no.y == y:
                return True
        return False 
