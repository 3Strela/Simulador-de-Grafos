from graphics import *
from time import sleep


def modText(var, cor, familia, estilo, tamanho):
    var.setFill(cor)
    var.setFace(familia)
    var.setStyle(estilo)
    var.setSize(tamanho)
    return var

def menuSelect(tela, menu):
    for itens in menu:
        itens.draw(tela)

    selecao_tp = True
    selecao_nm = True
    confirma = True
    sl_tp = -1
    sl_nm = -1

    menu_on = True
    menu_resto = []
    while menu_on:
        pos_mouse = tela.checkMouse()
        
        if selecao_tp:
            selecionou_tp = -1
            if pos_mouse != None:
                if pos_mouse.getX()>= 160 and pos_mouse.getX()<= 240 and pos_mouse.getY()>= 180 and pos_mouse.getY()<= 220:
                    selecionou_tp = 1
                elif pos_mouse.getX()>= 560 and pos_mouse.getX()<= 640 and pos_mouse.getY()>= 180 and pos_mouse.getY()<= 220:
                    selecionou_tp = 2

            if selecionou_tp == 1:
                sl_tp = 1
                menu[1].setFill('green')
                menu[2].setFill('gray')
            elif selecionou_tp == 2:
                sl_tp = 2
                menu[1].setFill('gray')
                menu[2].setFill('green')

            if sl_tp != -1 and selecao_nm:
                r3 = Rectangle(Point(140, 280), Point(260, 320))
                r3.setFill('gray')
                r3.draw(tela)
                menu_resto.append(r3)
                r4 = Rectangle(Point(540, 280), Point(660, 320))
                r4.setFill('gray')
                r4.draw(tela)
                menu_resto.append(r4)

                tt_normal = Text(Point(200, 300),'Normal')
                tt_normal = modText(tt_normal, 'white', 'courier', 'bold', 18)
                tt_normal.draw(tela)
                menu_resto.append(tt_normal)

                tt_matriz = Text(Point(600, 300),'Matriz')
                tt_matriz = modText(tt_matriz, 'white', 'courier', 'bold', 18)
                tt_matriz.draw(tela)
                menu_resto.append(tt_matriz)
                
                selecao_nm = False
            
            selecionou_nm = -1
            if sl_tp != -1:
                if pos_mouse != None:
                    if pos_mouse.getX()>= 140 and pos_mouse.getX()<= 260 and pos_mouse.getY()>= 280 and pos_mouse.getY()<= 320:
                        selecionou_nm = 1
                    elif pos_mouse.getX()>= 540 and pos_mouse.getX()<= 660 and pos_mouse.getY()>= 280 and pos_mouse.getY()<= 320:
                        selecionou_nm = 2
          
            if selecionou_nm == 1:
                sl_nm = 1
                r3.setFill('green')
                r4.setFill('gray')
            elif selecionou_nm == 2:
                sl_nm = 2
                r3.setFill('gray')
                r4.setFill('green')
      
            if sl_nm != -1 and confirma:
                r5 = Rectangle(Point(300, 340), Point(500, 380))
                r5.setFill('gray')
                r5.draw(tela)
                menu_resto.append(r5)

                tt_confirma = Text(Point(400, 360),'Confirmar')
                tt_confirma = modText(tt_confirma, 'white', 'courier', 'bold', 20)
                tt_confirma.draw(tela)
                menu_resto.append(tt_confirma)

                confirma = False
            
            if sl_nm != -1:
                if pos_mouse != None:
                    if pos_mouse.getX()>= 300 and pos_mouse.getX()<= 500 and pos_mouse.getY()>= 340 and pos_mouse.getY()<= 380:
                        r5.setFill('green')
                        sleep(0.5)

                        menu[1].setFill('gray')
                        menu[2].setFill('gray')

                        menu_on = False

    for itens in menu:
        itens.undraw()
    for itens in menu_resto:
        itens.undraw()

    return sl_tp, sl_nm

def grafNormal(tela, tipo):
    txt = Text(Point(400,70),'Informe as informações antes de prosseguir')
    txt = modText(txt,'yellow','courier', 'bold', 26)

    nodos = int(input('Informe a quantidade de Nodos: '))
    arestas = int(input('Informe a quantidade de Arestas: '))
    
    grafo = []
    for i in range(nodos):
        grafo.append([])

    for i in range(arestas):
        ent = input(f'Informe a {i+1} ligação: ')
        grafo[int(ent[0])].append(int(ent[1]))

    posX = 800//nodos
    posY = 600//nodos

    grafo_desenho = []

def grafMatriz(tela, tipo):
    
    arq = open('matriz.txt')
    pos = arq.readline().split()
    pre_matriz = arq.readlines()
    arq.close()

    matriz = []
    visitados = []
    linhas = int(pos[0])
    colunas = int(pos[1])
    ponto_ini = (-1, -1)    
    ll = 0
    for lin in pre_matriz:
        aux = []
        v_ax = []
        cc = 0
        for pnt in lin:
            if pnt != ' ' and pnt != '\n':
                if pnt == 'i':
                    ponto_ini = (ll, cc)    
                cc += 1
                v_ax.append(False)
                aux.append(pnt)
        ll += 1
        visitados.append(v_ax)
        matriz.append(aux)

    posX = 700//colunas
    posY = 500//linhas
    
    matriz_desenho = []
    for i in range(linhas):
        aux = []
        for j in range(colunas):
            if matriz[i][j] != '#':
                desenho = Rectangle(Point( posX*j+20, posY*i+20) , Point( posX*j+20+posX, posY*i+20+posY ))
                desenho.setFill(color_rgb(184, 184, 148))
                desenho.draw(tela)
                aux.append(desenho)
            else:
                desenho = Rectangle(Point( posX*j+20, posY*i+20) , Point( posX*j+20+posX, posY*i+20+posY ))
                desenho.setFill(color_rgb(51, 51, 51))
                desenho.draw(tela)
                aux.append(desenho)
        matriz_desenho.append(aux)
    
    
    matriz_desenho[ponto_ini[0]][ponto_ini[1]].setFill(color_rgb(255, 102, 0))
    visitados[ponto_ini[0]][ponto_ini[1]] = True

    ll = [1, -1, 0, 0]
    cc = [0, 0, 1, -1]

    tela.getMouse()

    if tipo == 1:
        pilha = [ponto_ini]
        while len(pilha) > 0:
            pos = pilha[-1]
            pilha.pop(-1)
            
            matriz_desenho[pos[0]][pos[1]].setFill(color_rgb(255, 102, 0))
            
            for cordenadas in range(4):
                lin = pos[0] + ll[cordenadas]
                col = pos[1] + cc[cordenadas]

                if lin >= 0 and lin <= linhas-1 and col >= 0 and col <= colunas-1:
                    if  (matriz[lin][col] == '.' or matriz[lin][col] == 'f') and not(visitados[lin][col]):
                        visitados[lin][col] = True
                        pilha.append((lin,col))
            sleep(0.5)
            matriz_desenho[pos[0]][pos[1]].setFill(color_rgb(0, 153, 0))
            sleep(0.5)
    else:
        fila = [ponto_ini]
        while len(fila) > 0:
            pos = fila[0]
            fila.pop(0)
            
            matriz_desenho[pos[0]][pos[1]].setFill(color_rgb(255, 102, 0))
            
            for cordenadas in range(4):
                lin = pos[0] + ll[cordenadas]
                col = pos[1] + cc[cordenadas]

                if lin >= 0 and lin <= linhas-1 and col >= 0 and col <= colunas-1:
                    if  (matriz[lin][col] == '.' or matriz[lin][col] == 'f') and not(visitados[lin][col]):
                        visitados[lin][col] = True
                        fila.append((lin,col))
            sleep(0.5)
            matriz_desenho[pos[0]][pos[1]].setFill(color_rgb(0, 153, 0))
            sleep(0.5)

    tela.getMouse()

    for partes in matriz_desenho:
        for cedulas in partes:
            cedulas.undraw()
        
def main():
    tela = GraphWin('Grafos Simulador', 800, 600)
    tela.setBackground('black')

    titulo = Text(Point(400,70),'Simulador de Grafos')
    titulo = modText(titulo,'orange','courier', 'bold', 26)

    r1 = Rectangle(Point(160,180),Point(240,220))
    r1.setFill('gray')
    r2 = Rectangle(Point(560,180),Point(640,220))
    r2.setFill('gray')

    tt_dfs = Text(Point(200, 200),'DFS')
    tt_dfs = modText(tt_dfs, 'white', 'courier', 'bold', 18)

    tt_bfs = Text(Point(600, 200),'BFS')
    tt_bfs = modText(tt_bfs, 'white', 'courier', 'bold', 18)

    menu = [titulo, r1, r2, tt_dfs, tt_bfs]

    lupi = True
    while lupi:
        busca_tp, tip = menuSelect(tela, menu)

        if tip == 1:
            grafNormal(tela, busca_tp)
        elif tip == 2:
            grafMatriz(tela, busca_tp)

    tela.close()

if __name__ == "__main__":
    main()