def painel(comp, voce, emp):
    print("""
    ----------------------------------------------------------
                                                PLACAR
                     Jogo da véIA             X | O | EMPATES
                                              {} | {} |    {}

                               """.format(len(voce), len(comp), len(emp)))

def repetiu(col, linhaStr):
    coordenadas = col+linhaStr
    if coordenadas not in escolhas:
        jogada.append(coordenadas)
        prosseguir = 's'
        return(prosseguir)
    else:
        invalido = ('Opção inválida')
        mensagem.append(invalido)
        jogada.append(0)
        prosseguir = 'n'
        return(prosseguir)

def jogo(coord, x, o):
    col = input('Informe a coluna: ')
    linhaStr= input('Informe a linha: ')
    if col not in letras:
        prosseguir = 'n'
        invalido = ('Coluna Inválida')
        mensagem.append(invalido)
        jogada.append(0)
        return(coord)
    if linhaStr not in num:
        prosseguir = 'n'
        invalido = ('Linha Inválida')
        mensagem.append(invalido)
        jogada.append(0)
        return(coord)
    linha = int(linhaStr)
    prosseguir = repetiu(col, linhaStr)
    if prosseguir == 's':
        if col == 'a':
            colA[linha-1] = x
        elif col == 'b':
            colB[linha-1] = x
        elif col == 'c':
            colC[linha-1] = x
        coord += 1
        return(coord)
    else:
        return(coord)

def escrever_mensagem(q, comp, voce):
    if q == "X":
        vencedor = ("PARABÉNS MEU CARO.")
        voce.append(q)
        mensagem.append(vencedor)
    else:
        vencedor = ("HAHAHA VOCÊ PERDEU.")
        comp.append(q)
        mensagem.append(vencedor)

def analiseCol(a, b, c, q, comp, voce):
    for i in range(0,3):
        if q in colA[i]:
            a += 1
        if a == 3:
            escrever_mensagem(q, comp, voce)
            return(a)
    for i in range(0,3):
        if colB[i] == q:
            b += 1
        if b == 3:
            escrever_mensagem(q, comp, voce)
            return(b)
    for i in range(0,3):
        if q == colC[i]:
            c += 1
        if c == 3:
            escrever_mensagem(q, comp, voce)
            return(c)
def analiseLinha(q, comp, voce):
    for i in range(0,3):
        if colA[i] == q:
            if colB[i] == q:
                if colC[i] == q:
                    escape = 3
                    escrever_mensagem(q, comp, voce)
                    return(escape)
def analiseVertical1(q, comp, voce):
    if colA[0] == q:
        if colB[1] == q:
            if colC[2] == q:
                escape = 3
                escrever_mensagem(q, comp, voce)
                return(escape)
def analiseVertical2(q, comp, voce):
    if colC[0] == q:
        if colB[1] == q:
            if colA[2] == q:
                escape = 3
                escrever_mensagem(q, comp, voce)
                return(escape)
def escolhas_disponiveis(dado, opcao, jogador):
    if len(jogador) > 0 and len(jogador) < 3:
        escolha = []
        for valor in opcao:
            if valor not in dado:
                escolha.append(valor)
        return(escolha)

def analisar_opcoes(dado, opcao, jogador):
    if len(jogador) > 0 and len(jogador) < 3:
        if len(jogador) == 1:
            if jogador[0] == 'o':
                esc = escolhas_disponiveis(dado, opcao, jogador)
                bruto.append(esc)
            if jogador[0] == 'x':
                esc = escolhas_disponiveis(dado, opcao, jogador)
                antijogada.append(esc)
        elif len(jogador) == 2:
            if jogador[0] == 'o' and jogador[1] == 'o':
                esc = escolhas_disponiveis(dado, opcao, jogador)
                ataque.append(esc[0])
            elif jogador[0] == 'x' and jogador[1] == 'x':
                esc = escolhas_disponiveis(dado, opcao, jogador)
                defesa.append(esc[0])

def filtro_continuacao(cont, jogador, opcoes, escolhas):
    process = []
    a = 0
    while a < len(cont):
        for i in cont[a]:
            process.append(i)
        a += 1
    obje = collections.Counter(process)
    frenq = obje.values()
    ordem = list(collections.OrderedDict.fromkeys(process))
    b = 0
    if jogador == 'o':
        for i in frenq:
            if i == 2:
                xeque.append(ordem[b])
                break
            b += 1
        for i in frenq:
            if i == 1:
                c = randint(0,len(ordem)-1)
                continuacao.append(ordem[c])
                break
    else:
        b = 0
        for i in frenq:
            if i == 2:
                contra_cheque.append(ordem[b])
            b += 1
    for valor in opcoes:
        if valor not in escolhas:
            disponiveis.append(valor)
def salvar_jogadas(jogo, jogad):
    jogada = jogo[0]
    jogador = jogad
    if jogada == 'a1':
        jog1.append(jogador)
        jog4.append(jogador)
        jog7.append(jogador)
        dados1.append(jogada)
        dados4.append(jogada)
        dados7.append(jogada)
    if jogada == 'a2':
        jog1.append(jogador)
        jog5.append(jogador)
        dados1.append(jogada)
        dados5.append(jogada)
    if jogada == 'a3':
        jog1.append(jogador)
        jog6.append(jogador)
        jog8.append(jogador)
        dados1.append(jogada)
        dados6.append(jogada)
        dados8.append(jogada)
    if jogada == 'b1':
        jog2.append(jogador)
        jog4.append(jogador)
        dados2.append(jogada)
        dados4.append(jogada)
    if jogada == 'b2':
        jog2.append(jogador)
        jog5.append(jogador)
        jog7.append(jogador)
        jog8.append(jogador)
        dados2.append(jogada)
        dados5.append(jogada)
        dados7.append(jogada)
        dados8.append(jogada)
    if jogada == 'b3':
        jog2.append(jogador)
        jog6.append(jogador)
        dados2.append(jogada)
        dados6.append(jogada)
    if jogada == 'c1':
        jog3.append(jogador)
        jog4.append(jogador)
        jog8.append(jogador)
        dados3.append(jogada)
        dados4.append(jogada)
        dados8.append(jogada)
    if jogada == 'c2':
        jog3.append(jogador)
        jog5.append(jogador)
        dados3.append(jogada)
        dados5.append(jogada)
    if jogada == 'c3':
        jog3.append(jogador)
        jog6.append(jogador)
        jog7.append(jogador)
        dados3.append(jogada)
        dados6.append(jogada)
        dados7.append(jogada)

def primeiras_rodadas(defesa, rodada, escolhas, opc7, opc8, contra_cheque, antijogada):
    cantos = ['a1', 'a3', 'c1', 'c3']
    meio = ['a2', 'b3', 'b1', 'c2']
    diagonal = 1
    disp = []
    decisao = ''
    if rodada == 0:
        c = randint(0,len(cantos)-1)
        decisao = cantos[c]
        if decisao not in opc7:
            diagonal = 2
    elif rodada == 1:
        if escolhas[0] == 'b2':
            c = randint(0,len(cantos)-1)
            decisao = cantos[c]
        else:
            decisao = 'b2'
    elif rodada == 2:
        if diagonal == 1:
            for x in opc7:
                if x not in escolhas:
                    disp.append(x)
                    if disp not in escolhas:
                        decisao = disp[0]
        else:
            for x in opc8:
                if x not in escolhas:
                    disp.append(x)
                    if disp not in escolhas:
                        decisao = disp[0]
    elif rodada == 3:
        print(antijogada)
        print(contra_cheque)
        if len(defesa) == 0:
            if len(contra_cheque) != 1:
                if escolhas[1] == 'b2':
                    a = 1
                    while a == 1:
                        c = randint(0,len(meio)-1)
                        metade = meio[c]
                        if metade not in escolhas:
                            decisao = metade
                            a = 2
                else:
                    a = 1
                    while a == 1:
                        c = randint(0,len(cantos)-1)
                        metade = cantos[c]
                        if metade not in escolhas:
                            decisao = metade
                            a = 2
            else:
                decisao = contra_cheque[0]
    if decisao != "":
        print("Estratégia")
    return decisao



def tomar_decisao(dados1, dados2, dados3, dados4, dados5, dados6, dados7, dados8, opc1, opc2, opc3, opc4, opc5, opc6, opc7, opc8, jog1, jog2, jog3, jog4, jog5, jog6, jog7, jog8, ataque, defesa, xeque, bruto, continuacao, opcoes, escolhas, rodada, antijogada, contra_cheque, disponiveis):
    analisar_opcoes(dados1, opc1, jog1)
    analisar_opcoes(dados2, opc2, jog2)
    analisar_opcoes(dados3, opc3, jog3)
    analisar_opcoes(dados4, opc4, jog4)
    analisar_opcoes(dados5, opc5, jog5)
    analisar_opcoes(dados6, opc6, jog6)
    analisar_opcoes(dados7, opc7, jog7)
    analisar_opcoes(dados8, opc8, jog8)
    filtro_continuacao(bruto, 'o', opcoes, escolhas)
    filtro_continuacao(antijogada, 'x', opcoes, escolhas)
    estrategia = ''
    decisao = ''
    if rodada >= 0 and rodada <=3:
        estrategia = primeiras_rodadas(defesa, rodada, escolhas, opc7, opc8, contra_cheque, antijogada)
    if estrategia != '':
        if estrategia[0] not in escolhas:
            decisao = estrategia
    else:
        if len(ataque) > 0:
            if ataque[0] not in escolhas:
                decisao = ataque[0]
                print('ataque')
        else:
            if len(defesa) > 0:
                if defesa[0] not in escolhas:
                    decisao = defesa[0]
                    print('defesa')
            else:
                if len(xeque) > 0:
                    if xeque[0] not in escolhas:
                        decisao = xeque[0]
                        print('xeque')
                else:
                    if len(contra_cheque) > 0:
                        if contra_cheque[0] not in escolhas:
                            decisao = contra_cheque[0]
                            print('Contra xeque')
                    else:
                        if len(continuacao) > 0:
                            if continuacao[0] not in escolhas:
                                decisao = continuacao[0]
                                print('Continuação')
        if decisao == '':
            print('Empate')
            decisao = disponiveis[0]

    jogada.append(decisao)
    return decisao


def salvar_decisao(rodada, decis):
    col = decis[0]
    linha = decis[1]
    if linha == '1':
        linha = 1
    elif linha == '2':
        linha = 2
    elif linha == '3':
        linha = 3
    if col == 'a':
        colA[linha-1] = 'O'
    elif col == 'b':
        colB[linha-1] = 'O'
    elif col == 'c':
        colC[linha-1] = 'O'
    rodada += 1
    return(rodada)

def jogadorX(rodada, a, b, c, o, x):
    print('''

                              SUA VEZ

        ''')
    rodada = jogo(rodada, x, o)
    return rodada

def jogadorO(rodada, x, o, a, b, c, dados1, dados2, dados3, dados4, dados5, dados6, dados7, dados8, opc1, opc2, opc3, opc4, opc5, opc6, opc7, opc8, jog1, jog2, jog3, jog4, jog5, jog6, jog7, jog8, ataque, defesa, xeque, bruto, continuacao, opcoes, escolhas, antijogada, contra_cheque, disponiveis):
    print('''
                        VEZ DO COMPUTADOR
                          ''')
    sleep(1)
    decis = tomar_decisao(dados1, dados2, dados3, dados4, dados5, dados6, dados7, dados8, opc1, opc2, opc3, opc4, opc5, opc6, opc7, opc8, jog1, jog2, jog3, jog4, jog5, jog6, jog7, jog8, ataque, defesa, xeque, bruto, continuacao, opcoes, escolhas, rodada, antijogada, contra_cheque, disponiveis)
    rodada = salvar_decisao(rodada, decis)
    return rodada

from random import randint
from time import sleep
import collections
novamente = 1
emp = [] ##### PLACAR
voce = []
comp = []
while novamente == 1 or novamente == 2:
    mensagem = []
    traco = ['_ |', '_ ']
    colunas = ["A ", "  B ", "  C "]
    colA = [' ']*3
    colB = [' ']*3
    colC = [' ']*3
    opcoes = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    escolhas = []
    letras = ['a', 'b', 'c']
    num = ['1', '2', '3']
    a = 0
    b = 0
    c = 0
    rodada = 0
    saida = 0
    x = "X"
    o = "O"
    opc1 = ['a1','a2','a3']
    opc2 = ['b1','b2','b3']
    opc3 = ['c1','c2','c3']
    opc4 = ['a1','b1','c1']
    opc5 = ['a2','b2','c2']
    opc6 = ['a3','b3','c3']
    opc7 = ['a1','b2','c3']
    opc8 = ['c1','b2','a3']
    dados1 = []
    dados2 = []
    dados3 = []
    dados4 = []
    dados5 = []
    dados6 = []
    dados7 = []
    dados8 = []
    jog1 = []
    jog2 = []
    jog3 = []
    jog4 = []
    jog5 = []
    jog6 = []
    jog7 = []
    jog8 = []
    while rodada < 9:
        painel(comp, voce, emp)
        print('\t \t \t',' ',"".join(colunas))
        for i in range(0,3):
            print('\t \t \t',i+1, colA[i],'|', colB[i], '|', colC[i])
            print('\t \t \t',' ',traco[0], traco[0], traco[1])
        if len(mensagem) > 0:
            print(mensagem[0])
            mensagem = []
        jogada = []
        if novamente == 1:
            if rodada % 2 == 0:
                jogad = 'x'
                rodada = jogadorX(rodada, a, b, c, o, x)
                ancol = analiseCol(a, b, c, x, comp, voce)
                anlinha = analiseLinha(x, comp, voce)
                anVert1 = analiseVertical1(x, comp, voce)
                anvert2 = analiseVertical2(x, comp, voce)
                if ancol == 3 or anlinha == 3 or anVert1 == 3 or anvert2 == 3:
                    saida = 3
            else:
                jogad = 'o'
                ataque = []
                defesa = []
                bruto = [] #filtro
                xeque = []
                antijogada = []
                contra_cheque = []
                continuacao = []
                disponiveis = []
                rodada = jogadorO(rodada, x, o, a, b, c, dados1, dados2, dados3, dados4, dados5, dados6, dados7, dados8, opc1, opc2, opc3, opc4, opc5, opc6, opc7, opc8, jog1, jog2, jog3, jog4, jog5, jog6, jog7, jog8, ataque, defesa, xeque, bruto, continuacao, opcoes, escolhas, antijogada, contra_cheque, disponiveis)
                ancol = analiseCol(a, b, c, o, comp, voce)
                anlinha = analiseLinha(o, comp, voce)
                anVert1 = analiseVertical1(o,comp, voce)
                anvert2 = analiseVertical2(o, comp, voce)
                if ancol == 3 or anlinha == 3 or anVert1 == 3 or anvert2 == 3:
                    saida = 3
                print('                               ',jogada[0])
        elif novamente == 2:
            if rodada % 2 == 0:
                jogad = 'o'
                ataque = []
                defesa = []
                bruto = [] #filtro
                xeque = []
                antijogada = []
                contra_cheque = []
                continuacao = []
                disponiveis = []
                rodada = jogadorO(rodada, x, o, a, b, c, dados1, dados2, dados3, dados4, dados5, dados6, dados7, dados8, opc1, opc2, opc3, opc4, opc5, opc6, opc7, opc8, jog1, jog2, jog3, jog4, jog5, jog6, jog7, jog8, ataque, defesa, xeque, bruto, continuacao, opcoes, escolhas, antijogada, contra_cheque, disponiveis)
                ancol = analiseCol(a, b, c, o, comp, voce)
                anlinha = analiseLinha(o,comp, voce)
                anVert1 = analiseVertical1(o, comp, voce)
                anvert2 = analiseVertical2(o,comp, voce)
                if ancol == 3 or anlinha == 3 or anVert1 == 3 or anvert2 == 3:
                    saida = 3
                print('                               ',jogada[0])
            else:
                jogad = 'x'
                rodada = jogadorX(rodada, a, b, c, o, x)
                ancol = analiseCol(a, b, c, x, comp, voce)
                anlinha = analiseLinha(x, comp, voce)
                anVert1 = analiseVertical1(x, comp, voce)
                anvert2 = analiseVertical2(x, comp, voce)
                if ancol == 3 or anlinha == 3 or anVert1 == 3 or anvert2 == 3:
                    saida = 3
        if jogada[0] != 0:
            escolhas.append(jogada[0])
            salvar_jogadas(jogada, jogad)
        if rodada == 9:
            if saida != 3:
                empate = ("Parece que empatamos não vejo a hora de jogarmos novamente. ")
                emp.append(saida)
                painel(comp, voce, emp)
                print('\t \t \t',' ',"".join(colunas))
                for i in range(0,3):
                    print('\t \t \t',i+1, colA[i],'|', colB[i], '|', colC[i])
                    print('\t \t \t',' ',traco[0], traco[0], traco[1])
                print(empate)
        if saida == 3:
            rodada = 9
            painel(comp, voce, emp)
            print('\t \t \t',' ',"".join(colunas))
            for i in range(0,3):
                print('\t \t \t',i+1, colA[i],'|', colB[i], '|', colC[i])
                print('\t \t \t',' ',traco[0], traco[0], traco[1])
            if len(mensagem) > 0:
                print(mensagem[0])
    chave = novamente
    novamente = int(input("Digite 1 para jogar novamente "))
    if novamente == 1:
        if chave == 1:
            novamente = 2
        else:
            novamente = 1
