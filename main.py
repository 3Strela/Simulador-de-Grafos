from graphics import *
from time import sleep

def modText(var, cor, familia, estilo, tamanho):
    var.setFill(cor)
    var.setFace(familia)
    var.setStyle(estilo)
    var.setSize(tamanho)
    return var

def modNode(var1, cor, var2, familia, estilo, tela):
    var1.setFill(cor)
    var1.setOutline(cor)
    var1.draw(tela)

    var2.setFace(familia)
    var2.setStyle(estilo)
    var2.draw(tela)
    return var1, var2

def grafNormal(tela, tipo):
    arq = open('grafo.txt')
    nodes_arestas_fonte = arq.readline().split()
    ligacoes = arq.readlines()
    arq.close()

    nodes = int(nodes_arestas_fonte[0])
    arestas = int(nodes_arestas_fonte[1])
    fonte = int(nodes_arestas_fonte[2])

    lista_adj = []
    for n in range(nodes+1):
        lista_adj.append([])

    for partes in ligacoes:
        partes.split()
        u = int(partes[0])
        v = int(partes[2])

        lista_adj[u].append(v)
        lista_adj[v].append(u)
    
    posX = 700//nodes
    posY = 500//nodes

    grafo_nodes_desenho = []
    grafo_arestas_desenho = []
    for pai in range(1, nodes+1):
        for filho in lista_adj[pai]:
            aresta = Line(Point(posX*pai - posX + (3*posX//4), posY), Point(posX*filho - posX + (3*posX//4), posY))
            aresta.setFill('gray')
            aresta.draw(tela)
            grafo_arestas_desenho.append(aresta)
        
        desenho = Circle(Point(posX*pai - posX + (3*posX//4), posY), posX//4)
        txt_num = Text(Point(posX*pai - posX + (3*posX//4), posY), str(pai))
        desenho, txt_num = modNode(desenho, 'white', txt_num, 'courier', 'bold', tela)
        grafo_nodes_desenho.append(desenho)
        grafo_nodes_desenho.append(txt_num)


    tela.getMouse()


    tela.getMouse()
    for itens in grafo_nodes_desenho:
        itens.undraw()

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
            sleep(0.3)
            matriz_desenho[pos[0]][pos[1]].setFill(color_rgb(0, 153, 0))
            sleep(0.3)
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
        
def intrucoes(tela):
    
    arq = open('instru.txt')
    txt = arq.read()
    arq.close()

    ind = 0
    ppX = 30
    ppY = 50

    bord = Rectangle(Point(50,480),Point(150,520))
    bord.setFill('gray')
    bord.draw(tela)

    voltar = Text(Point(100, 500),'Voltar')
    voltar = modText(voltar, 'white', 'courier', 'bold', 18)
    voltar.draw(tela)

    excluir = [bord, voltar]

    pos_mouse = tela.checkMouse()
    while True:
        pos_mouse = tela.checkMouse()
        if ind < len(txt):
            if txt[ind] == '\n':
                ppY += 20
                ppX = 30
            elif txt[ind] == ' ':
                ppX += 10
            else:
                tt = Text(Point(ppX, ppY), txt[ind])
                tt.setFill('white')
                tt.setFace('courier')
                tt.setStyle('bold')
                tt.draw(tela)
                excluir.append(tt)
                ppX += 10
        ind += 1
        if pos_mouse != None and pos_mouse.getX() >= 80 and pos_mouse.getX() <= 270 and pos_mouse.getY() >= 480 and pos_mouse.getY() <= 520:
            break

    bord.setFill('blue')
    sleep(0.5)

    for itens in excluir:
        itens.undraw()

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

        if pos_mouse != None and pos_mouse.getX() >= 80 and pos_mouse.getX() <= 270 and pos_mouse.getY() >= 480 and pos_mouse.getY() <= 520:
            menu[5].setFill('blue')
            sl_nm = 0
            menu_on = False
            sleep(0.5)
            menu[5].setFill('gray')
        if pos_mouse != None and pos_mouse.getX() >= 610 and pos_mouse.getX() <= 690 and pos_mouse.getY() >= 480 and pos_mouse.getY() <= 520:
            menu[6].setFill('red')
            sl_nm = -1
            menu_on = False
            sleep(0.5)
            menu[5].setFill('gray')

    for itens in menu:
        itens.undraw()
    for itens in menu_resto:
        itens.undraw()

    return sl_tp, sl_nm

def main():
    tela = GraphWin('Grafos Simulador', 800, 600)
    tela.setBackground('black')

    titulo = Text(Point(400,70),'Simulador de Grafos')
    titulo = modText(titulo,'orange','courier', 'bold', 26)

    r1 = Rectangle(Point(160,180),Point(240,220))
    r1.setFill('gray')
    r2 = Rectangle(Point(560,180),Point(640,220))
    r2.setFill('gray')
    r3 = Rectangle(Point(80,480),Point(270,520))
    r3.setFill('gray')
    r4 = Rectangle(Point(610,480),Point(690,520))
    r4.setFill('gray')

    tt_dfs = Text(Point(200, 200),'DFS')
    tt_dfs = modText(tt_dfs, 'white', 'courier', 'bold', 18)

    tt_bfs = Text(Point(600, 200),'BFS')
    tt_bfs = modText(tt_bfs, 'white', 'courier', 'bold', 18)

    instru = Text(Point(175, 500), 'Instruções')
    instru = modText(instru, 'white', 'courier', 'bold', 20)
    
    sair = Text(Point(650, 500), 'Sair')
    sair = modText(sair, 'white', 'courier', 'bold', 20)


    menu = [titulo, r1, r2, tt_dfs, tt_bfs, r3, r4, instru, sair]

    lupi = True
    while lupi:
        busca_tp, tip = menuSelect(tela, menu)

        if tip == 0:
            intrucoes(tela)
        elif tip == 1:
            grafNormal(tela, busca_tp)
        elif tip == 2:
            grafMatriz(tela, busca_tp)
        else:
            break

    tela.close()

if __name__ == "__main__":
    main()