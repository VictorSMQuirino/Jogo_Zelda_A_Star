import pygame

class Janela:
    def __init__(self, altura, largura):
        self.largura = largura
        self.altura = altura
        self.janela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Jogo Zelda")
        self.clock = pygame.time.Clock()

    def atualizar(self):
        pygame.display.flip()
        self.clock.tick(60)

    def desenhar_mapa(self, mapa):
        for y in range(len(mapa)):
            for x in range (len(mapa[0])):
                if mapa[y][x] == "g":
                    pygame.draw.rect(self.janela, (124, 252, 0), pygame.Rect(x*15, y*15, 15, 15)) 
                elif mapa[y][x] == "a":
                    pygame.draw.rect(self.janela, (240, 230, 140), pygame.Rect(x*15, y*15, 15, 15))
                elif mapa[y][x] == "f":
                    pygame.draw.rect(self.janela, (34, 139, 34), pygame.Rect(x*15, y*15, 15, 15))
                elif mapa[y][x] == "m":
                    pygame.draw.rect(self.janela, (205, 133, 63), pygame.Rect(x*15, y*15, 15, 15))
                elif mapa[y][x] == "w":
                    pygame.draw.rect(self.janela, (0, 0, 255), pygame.Rect(x*15, y*15, 15, 15))
                pygame.draw.rect(self.janela, (0, 0, 0), pygame.Rect(x*15, y*15, 15, 15), 1)

    def desenhar_dungeon(self, mapa):
        for y in range(len(mapa)):
            for x in range(len(mapa[0])):
                if mapa[y][x] == "g":
                    pygame.draw.rect(self.janela, (211, 211, 211), pygame.Rect(x*15, y*15, 15, 15)) 
                else:
                    pygame.draw.rect(self.janela, (128, 128, 128), pygame.Rect(x*15, y*15, 15, 15))
                pygame.draw.rect(self.janela, (0, 0, 0), pygame.Rect(x*15, y*15, 15, 15), 1)     

    def desenhar_caminho(self, mapa, caminho, cor):
        tempo = pygame.time.Clock()
        for z in range(len(caminho)):
            for x in range(len(mapa)):
                for y in range(len(mapa[x])):
                    if (x, y) == caminho[z]:
                        pygame.draw.rect(self.janela, cor, pygame.Rect(x*15, y*15, 15, 15))
                        pygame.display.update()
                        tempo.tick(10)

    def desenhar_sprite(self, sprite, posicao):
        self.janela.blit(sprite, posicao)

    def limpar(self):
        self.janela.fill((255, 255, 255))    