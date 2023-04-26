import pygame
from janela import Janela
from agente import Agente
from node import Node
import numpy as np

with open("mapa.txt", "r") as m:
    #mapa = np.loadtxt(m, dtype=str)
    mapa = [list(line.strip()) for line in m.readlines()]

with open("dungeon_1.txt", "r") as d:
    dungeon_1 = [list(line.strip()) for line in d.readlines()]

with open("dungeon_2.txt", "r") as d:
    dungeon_2 = [list(line.strip()) for line in d.readlines()]

with open("dungeon_3.txt", "r") as d:
    dungeon_3 = [list(line.strip()) for line in d.readlines()]

dungeon_explorada = []

janela = Janela(630, 630)

laranja = (255, 69, 0)
amarelo = (218,165,32)

agente = Agente([24, 27], mapa)

dungeons = [(24, 1), (39, 17), (5, 32)]
lost_woods = (6, 5)

spritePersonagem = pygame.image.load("images/linkinho.png")
personagem = {'obj': pygame.Rect(360, 405, 15, 15), 'sprite': spritePersonagem}

spritePendantOfCourage = pygame.image.load("images/PendantOfCourage.png")
pendantOfCourage = {'obj': pygame.Rect(225, 285, 15, 15), 'sprite': spritePendantOfCourage}

spritePendantOfPower = pygame.image.load("images/PendantOfPower.png")
pendantOfPower = {'obj': pygame.Rect(195, 30, 15, 15), 'sprite': spritePendantOfPower}

spritePendantOfWisdom = pygame.image.load("images/PendantOfWisdom.png")
pendantOfWisdom = {'obj': pygame.Rect(195, 45, 15, 15), 'sprite': spritePendantOfWisdom}

custo_total = 0
CUSTOS = {"g": 10, "a": 20, "f": 100, "m": 150, "w": 180, "#": 0}
mapa_custo = []
for i in range(len(mapa)):
    linha = []
    for j in range(len(mapa[i])):
        custo = CUSTOS[mapa[i][j]]
        linha.append(custo)
    mapa_custo.append(linha)

mapa_custo = np.asarray(mapa_custo)
mapa_custo = mapa_custo.transpose()

dungeon_custo1 = []
for i in range(len(dungeon_1)):
    linha = []
    for j in range(len(dungeon_1[i])):
        custo = CUSTOS[dungeon_1[i][j]]
        linha.append(custo)
    dungeon_custo1.append(linha)

dungeon_custo1 = np.asarray(dungeon_custo1)
dungeon_custo1 = dungeon_custo1.transpose()

dungeon_custo2 = []
for i in range(len(dungeon_2)):
    linha = []
    for j in range(len(dungeon_2[i])):
        custo = CUSTOS[dungeon_2[i][j]]
        linha.append(custo)
    dungeon_custo2.append(linha)

dungeon_custo2 = np.asarray(dungeon_custo2)
dungeon_custo2 = dungeon_custo2.transpose()

dungeon_custo3 = []
for i in range(len(dungeon_3)):
    linha = []
    for j in range(len(dungeon_3[i])):
        custo = CUSTOS[dungeon_3[i][j]]
        linha.append(custo)
    dungeon_custo3.append(linha)

dungeon_custo3 = np.asarray(dungeon_custo3)
dungeon_custo3 = dungeon_custo3.transpose()

caminho1 = agente.a_star(mapa_custo, agente.pos, dungeons[0])
caminho2 = agente.a_star(mapa_custo, agente.pos, dungeons[1])
caminho3 = agente.a_star(mapa_custo, agente.pos, dungeons[2])
custo1 = sum([mapa_custo[x][y] for x, y in caminho1])
custo2 = sum([mapa_custo[x][y] for x, y in caminho2])
custo3 = sum([mapa_custo[x][y] for x, y in caminho3])

print("Custo para a primeira dungeon: ")
if(custo1 < custo2 and custo1 < custo3):
    primeiro_caminho = caminho1
    agente.pos = dungeons.pop(0)
    custo_total = custo_total + custo1
    print(custo1)
elif(custo2 < custo3 and custo2 < custo1):
    primeiro_caminho = caminho2
    agente.pos = dungeons.pop(1)
    custo_total = custo_total + custo2
    print(custo2)
else:
    primeiro_caminho = caminho3
    agente.pos = dungeons.pop(2)
    custo_total = custo_total + custo3
    print(custo3)

posicoes = agente.verifica_dungeon(agente.pos)
caminho_dungeon1 = agente.a_star(dungeon_custo1, posicoes[0], posicoes[1])
custo_dungeon = sum([mapa_custo[x][y] for x, y in caminho_dungeon1])
custo_total = custo_total + custo_dungeon * 2
    
caminho1 = agente.a_star(mapa_custo, agente.pos, dungeons[0])
caminho2 = agente.a_star(mapa_custo, agente.pos, dungeons[1])
custo1 = sum([mapa_custo[x][y] for x, y in caminho1])
custo2 = sum([mapa_custo[x][y] for x, y in caminho2])

print("Custo para a segunda dungeon: ")
if(custo1 < custo2):
    segundo_caminho = caminho1
    agente.pos = dungeons.pop(0)
    custo_total = custo_total + custo1
    print(custo1)
else:
    segundo_caminho = caminho2
    agente.pos = dungeons.pop(1)
    custo_total = custo_total + custo2
    print(custo2)

posicoes = agente.verifica_dungeon(agente.pos)
caminho_dungeon2 = agente.a_star(dungeon_custo2, posicoes[0], posicoes[1])
custo_dungeon = sum([mapa_custo[x][y] for x, y in caminho_dungeon2])
custo_total = custo_total + custo_dungeon * 2

print("Custo para a terceira dungeon: ")
terceiro_caminho = agente.a_star(mapa_custo, agente.pos, dungeons[0])
custo1 = sum([mapa_custo[x][y] for x, y in terceiro_caminho])
custo_total = custo_total + custo1
agente.pos = dungeons.pop(0)
print(custo1)

posicoes = agente.verifica_dungeon(agente.pos)
caminho_dungeon3 = agente.a_star(dungeon_custo3, posicoes[0], posicoes[1])
custo_dungeon = sum([mapa_custo[x][y] for x, y in caminho_dungeon3])
custo_total = custo_total + custo_dungeon * 2

quarto_caminho = agente.a_star(mapa_custo, agente.pos, lost_woods)
custo1 = sum([mapa_custo[x][y] for x, y in quarto_caminho])
custo_total = custo_total + custo1
print("Custo para a lost woods: ")
print(custo1)
print("Custo total: ")
print(custo_total)

execucao = True
while execucao:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    janela.limpar()
    janela.desenhar_mapa(mapa)
    janela.desenhar_sprite(personagem["sprite"], personagem["obj"])
    janela.desenhar_caminho(mapa, primeiro_caminho, laranja)
    janela.limpar()
    janela = Janela(420, 420)
    janela.desenhar_dungeon(dungeon_1)
    janela.desenhar_sprite(pendantOfWisdom["sprite"], pendantOfWisdom["obj"])
    janela.desenhar_caminho(dungeon_1, caminho_dungeon1, laranja)
    janela.desenhar_caminho(dungeon_1, caminho_dungeon1[::-1], amarelo)
    janela.limpar()
    janela = Janela(630, 630)
    janela.desenhar_mapa(mapa)
    janela.desenhar_caminho(mapa, segundo_caminho, laranja)
    janela.limpar()
    janela = Janela(420, 430)
    janela.desenhar_dungeon(dungeon_2)
    janela.desenhar_sprite(pendantOfPower["sprite"], pendantOfPower["obj"])
    janela.desenhar_caminho(dungeon_2, caminho_dungeon2, laranja)
    janela.desenhar_caminho(dungeon_2, caminho_dungeon2[::-1], amarelo)
    janela.limpar()
    janela = Janela(630, 630)
    janela.desenhar_mapa(mapa)
    janela.desenhar_caminho(mapa, terceiro_caminho, laranja)
    janela.limpar()
    janela = Janela(420, 420)
    janela.desenhar_dungeon(dungeon_3)
    janela.desenhar_sprite(pendantOfCourage["sprite"], pendantOfCourage["obj"])
    janela.desenhar_caminho(dungeon_3, caminho_dungeon3, laranja)
    janela.desenhar_caminho(dungeon_3, caminho_dungeon3[::-1], amarelo)
    janela.limpar()
    janela = Janela(630, 630)
    janela.desenhar_mapa(mapa)

    janela.desenhar_caminho(mapa, quarto_caminho, laranja)

    #agente.a_star()
    
    #janela_dungeon.desenhar_dungeon(dungeon_1)

    #janela.atualizar()
    execucao = False