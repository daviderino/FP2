#92446 David Alexandre Barreiro Baptista

# ===== ADTs - Abstract Data Types =====#

# === Celula === #
# Representacao interna {'v': v} onde v e o valor numerico correspondente ao estado da celula
# Tem como objetivo representar o estado de uma celula do qubit

# Construtores

# cria_celula: {-1, 0, 1} -> celula
def cria_celula(v):
    '''Recebe um argumento correspondente ao valor da celula. Caso o argumento seja valido devolve um elemento
    do tipo celula na forma {'v': v} correspondendo ao valor da celula'''
    if v in (-1, 0, 1):
        return {'v': v}
    else:
        raise ValueError('cria_celula: argumento invalido.')

# Seletores

# obter_valor: celula -> {-1, 0, 1}
def obter_valor(c):
    '''Recebe uma celula e devolve o valor numerico associado a mesma'''
    return c['v']

# Modificadores

# inverte_estado: celula -> celula
def inverte_estado(c):
    '''Recebe uma celula e inverte o seu estado, devolvendo a celula invertida. Isto e, uma celula ativa torna se
    inativa, uma celula inativa torna se ativa e uma incerta permanece incerta'''
    if obter_valor(c) == 1:
        c['v'] = 0
    elif obter_valor(c) == 0:
        c['v'] = 1
    return c

# Reconhecedores

# eh_celula: universal -> logico
def eh_celula(arg):
    '''Recebe um argumento qualquer e devolve True caso seja do tipo celula. Caso nao seja devolve False'''
    return isinstance(arg, dict) and len(arg) == 1 and 'v' in arg and isinstance(arg['v'], int) and obter_valor(arg) in (-1, 0, 1)

# Testes

# celulas_iguais: celula -> logico
def celulas_iguais(c1, c2):
    '''Recebe duas celulas e devolve True se as celulas estiverem no mesmo estado'''
    return eh_celula(c1) and eh_celula(c2) and obter_valor(c1) == obter_valor(c2)

# Transformadores

# celula_para_str: celula -> string
def celula_para_str(c):
    '''Recebe uma celula e devolve a cadeia de caracteres que representa o seu respetivo estado'''
    if obter_valor(c) == -1:
        return 'x'
    else:
        return str(obter_valor(c))

# === Coordenada === #
# Representacao interna: (l, c) onde l corresponde ao valor da linha e c corresponde ao valor da coluna. Ambos os valores
# apenas se podem encontrar entre 0 e 2 (inteiro). Usado para representar a posicao de uma celula no tabuleiro

# Construtores

#cria_coordenada: N2 -> coordenada
def cria_coordenada(l, c):
    '''Recebe um par de inteiros correspondente a uma linha e a uma coluna, e devolve uma variavel do tipo
    coordenada caso os valores inseridos sejam validos. Recorre a funcao auxiliar coordenada() para efetuar
    a validacao'''
    if coordenada(l) and coordenada(c):
        return (l, c)
    else:
        raise ValueError('cria_coordenada: argumentos invalidos.')

# Seletores

# coordenada_linha: coordenada -> N
def coordenada_linha(c):
    '''Devolve o numero natural correspondente linha da coordenada c'''
    return c[0]

# coordenada_coluna: coordenada -> N
def coordenada_coluna(c):
    '''Devolve o numero natural correspondente coluna da coordenada c'''
    return c[1]

# Reconhecedores

# eh_coordenada: universal -> logico
def eh_coordenada(arg):
    '''Recebe um argumento de qualquer tipo e devolve True caso seja do tipo coordenada. Caso nao seja devolve False'''
    return isinstance(arg, tuple) and len(arg) == 2 and (coordenada(arg[0]) and coordenada(arg[1]))

# Testes

# coordenadas_iguais: coordenada x coordenada -> logico
def coordenadas_iguais(c1, c2):
    '''Recebe duas coordenadas e devolve True se representarem a mesma posicao, caso nao sejam devolve False'''
    return eh_coordenada(c1) and eh_coordenada(c2) and c1 == c2

# Transformadores

# coordenada_para_str: coordenada -> string
def coordenada_para_str(c):
    '''Devolve uma string que representa a coordenada recebida'''
    return '(' +  str(coordenada_linha(c)) + ', ' + str(coordenada_coluna(c)) + ')'

# Funcao auxiliar
def coordenada(n):
    '''Efetua a verificacao se um dado inteiro e uma coordenada. Devolve True caso seja, False caso nao seja'''
    return isinstance(n, int) and n in (0, 1, 2)

# === Tabuleiro === #
# Representacao interna: {coordenada: celula, (n vezes)}. A chave corresponde a coordenada de uma dada celula, correspondendo
# esta celula ao valor. E usado para representar um tabuleiro.

# Construtores

# tabuleiro_inicial: {} -> tabuleiro
def tabuleiro_inicial():
    '''Devolve o valor de tabuleiro correspondente ao tabuleiro inicial'''
    return str_para_tabuleiro('((-1, -1, -1), (0,0, -1), (0, -1))')

# str_para_tabuleiro: string -> tabuleiro
def str_para_tabuleiro(s):
    '''Recebe uma string contendo o tabuleiro e convertendo a mesma para tuplo e efetuando a verificacao
    se e um tabuleiro valido. Caso seja devolve o mesmo tabuleiro ja na sua forma de tabuleiro, caso nao seja
    gera um erro'''

    if isinstance(s, str):
        s = eval(s)
        t = {}
        if isinstance(s, tuple) and len(s) == 3 and len(s[0]) == 3 and len(s[1]) == 3 and len(s[2]) == 2:
            for small_set in s:
                if not isinstance(small_set, tuple):
                    raise ValueError('str_para_tabuleiro: argumento invalido.')
            n = 0

            while n <= 2:
                c = 0
                if n == 2:
                    m = 1
                else:
                    m = 2
                while c <= m:
                    if isinstance(s[n][c], int) and s[n][c] in (-1, 0, 1):
                        if m == 1:
                            t[cria_coordenada(n, c+1)] = cria_celula(s[n][c])
                        else:
                            t[cria_coordenada(n, c)] = cria_celula(s[n][c])
                    else:
                        raise ValueError('str_para_tabuleiro: argumento invalido.')
                    c += 1
                n += 1
            return t
        else:
            raise ValueError('str_para_tabuleiro: argumento invalido.')
    else:
        raise ValueError('str_para_tabuleiro: argumento invalido.')

# Seletores

#tabuleiro_dimensao: tabuleiro -> N
def tabuleiro_dimensao(t):
    '''Recebe um dado tabuleiro e devolve o numero de linhas/colunas'''
    res = 0

    # Percorre todos os elementos e atribui a variavel res o valor do maior indice da linha encontrada. Incrementa 1
    # de modo a corrigir o facto de comecar a contar do 0
    for val in t:
        if coordenada_linha(val) >= res:
            res = coordenada_linha(val)
            res += 1

    return res

# tabuleiro_celula: tabuleiro x coordenada -> celula
def tabuleiro_celula(t, coor):
    '''Recebe um tabuleiro e uma dada coordenada, devolvendo o calor da celula correspondente a esse valor. Efetua
    a dada correcao caso receba uma coordenada da linha 2, isto e, subtrai 1 ao valor da coluna para aceder ao
    valor correto na tabela que comeca com o indice 0, que nao corresponde a uma coordenada'''
    return t[coor]

# Modificadores

# tabuleiro_substitui_celula: tabuleiro x celula x coordenada -> tabuleiro
def tabuleiro_substitui_celula(t, cel, coor):
    '''Recebe um tabuleiro, uma coordenada e uma celula. Troca a celula na dada coordenada pela celula recebida
    Converte a tabela recebida para uma lista de modo a poder alterar os seus valores'''
    if (eh_tabuleiro(t) and eh_coordenada(coor) and eh_celula(cel)) and (not coordenadas_iguais(coor, cria_coordenada(2,0))):
        t[coor] = cel
        return t
    else:
        raise ValueError('tabuleiro_substitui_celula: argumentos invalidos.')

# tabuleiro_inverte_estado: tabuleiro x coordenada -> tabuleiro
def tabuleiro_inverte_estado(t, coor):
    '''Recebe um tabuleiro e uma dada coordenada, e efetua a troca do valor do qubit nada dada coordenada. Recorre
    a funcoes auxiliares para transformar o tabuleiro numa lista de modo a poder efetuar as trocas'''
    if (eh_coordenada(coor) and eh_tabuleiro(t)) and coor != cria_coordenada(2, 0):
        t[coor] = inverte_estado(t[coor])

        return t
    else:
        raise ValueError('tabuleiro_inverte_estado: argumentos invalidos.')

# Reconhecedores

# eh_tabuleiro: universal -> logico
def eh_tabuleiro(arg):
    '''Recebe um valor de qualquer tipo, e devolve True caso seja do tipo tabuleiro, False caso nao seja'''
    if not isinstance(arg, dict) or tabuleiro_dimensao(arg) != 3 or len(arg) != 8:
        return False

    # Verifica individualmente se o dicionario recebido tem coordenadas como chaves e celulas como valores
    for val in arg:
        if not eh_coordenada(val) or not eh_celula(arg[val]):
            return False

    return True

# Testes

# tabuleiros_iguais: tabuleiro x tabuleiro -> logico
def tabuleiros_iguais(t1, t2):
    '''Devolve verdadeiro no caso de ambos os tabuleiros recebidos serem iguais. Se nao forem devolve False'''
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2

# Reconhecedores

# tabuleiro_para_str: tabuleiro -> string
def tabuleiro_para_str(t):
    '''Recebe o tabuleiro que vai escrever,e devolve a string que representa o tabuleiro recebido. Cria uma lista que
    vai usar para representar os valores do tabuleiro recebido e devolve uma string com o tabuleiro representado'''

    tab_res = []

    # Itera por todos os elementos do tabuleiro e adiciona a uma lista para ser feito o respetivo output
    for l in range(0, 3):
        # A divisao inteira consiste na correcao do valor da coluna na linha 2 (comeca em 1 e nao em 0)
        for c in range(0 + (l // 2), 3):
            tab_res.append(celula_para_str(tabuleiro_celula(t, cria_coordenada(l, c))))

    return '+-------+\n|...' \
           + tab_res[2] + '...|\n|..' \
           + tab_res[1] + '.' \
           + tab_res[5] + '..|\n|.' \
           + tab_res[0] + '.' \
           + tab_res[4] + '.' \
           + tab_res[7] + '.|\n|..' \
           + tab_res[3] + '.' \
           + tab_res[6] + '..|\n+-------+'

# Operacoes de alto nivel

# Funcoes auxiliares

# aplica_porta: tabuleiro x int x {'E', 'D'} -> tabuleiro
def aplica_porta(t, v_porta, lado):
    ''' Recebe um tabuleiro, um valor correspondente a porta e o valor do lado. Efetua a dada inversao de estado
    das celulas do tabuleiro, a porta e o lado fornecido'''
    if lado == 'E':
        for i in range(0, 3):
            coor = cria_coordenada(v_porta, i)
            t = tabuleiro_inverte_estado(t, coor)
    else:
        for i in range(2, -1, -1):
            coor = cria_coordenada(i, 2 - v_porta)
            t = tabuleiro_inverte_estado(t, coor)
    return t

# Funcoes principais

# porta_x: tabuleiro x {'E', 'D'} -> tabuleiro
def porta_x(t, p):
    '''Recebe um tabuleiro e um caracter correspondente ao lado a efetuar a operacao. Efetua a operacao da porta x, isto
     e, inverte os qubits da diagonal interior. Utiliza uma funcao auxiliar para aplicar a porta'''
    if eh_tabuleiro(t) and isinstance(p, str) and p in ('E', 'D'):
        return aplica_porta(t, 1, p)
    else:
        raise ValueError('porta_x: argumentos invalidos.')

# porta_z: tabuleiro x {'E', 'D'} -> tabuleiro
def porta_z(t, p):
    '''Recebe um tabuleiro e um caracter correspondente ao lado a efetuar a operacao. Efetua a operacao da porta z, isto
     e, inverte os qubits da diagonal superior.  Utiliza uma funcao auxiliar para aplicar a porta'''
    if eh_tabuleiro(t) and isinstance(p, str) and p in ('E', 'D'):
        return aplica_porta(t, 0, p)
    else:
        raise ValueError('porta_z: argumentos invalidos.')

# porta_h: tabuleiro x {'E', 'D'} -> tabuleiro
def porta_h(t, p):
    '''Recebe um tabuleiro e um caracter correspondente ao lado a efetuar a operacao. Efetua a operacao da porta h, isto
     e, troca as posicoes dos qubits nas diagonais'''
    if eh_tabuleiro(t) and isinstance(p, str) and p in ('E', 'D'):
        tab_copy = {}

        # cria uma copia do tabuleiro para facilitar na aplicacao da porta
        for val in t:
            tab_copy[val] = t[val]

        # Verifica qual o lado e efetua um ciclo que cria pares de coordenadas e efetua a respetiva troca no tabuleiro
        # principal (o recebido como input)
        if p == 'E':
            for c in range(0, 3):
                coor1 = cria_coordenada(0, c)
                coor2 = cria_coordenada(1, c)
                tabuleiro_substitui_celula(t, tabuleiro_celula(tab_copy, coor1), coor2)
                tabuleiro_substitui_celula(t, tabuleiro_celula(tab_copy, coor2), coor1)
        else:
            for l in range(0, 3):
                coor1 = cria_coordenada(l, 1)
                coor2 = cria_coordenada(l, 2)
                tabuleiro_substitui_celula(t, tabuleiro_celula(tab_copy, coor1), coor2)
                tabuleiro_substitui_celula(t, tabuleiro_celula(tab_copy, coor2), coor1)

        return t
    else:
        raise ValueError('porta_h: argumentos invalidos.')

# hello_quantum: string -> logico
def hello_quantum(objetivo):
    '''Recebe uma string com o tabuleiro final e o numero de jogadas. Permite jogar o jogo, escrevendo varias mensagens
    consoante a fase do jogo. Recebe input do utilizador e escreve os tabuleiros na janela '''
    tabuleiro_final = (objetivo[0:-2])
    tabuleiro_final = str_para_tabuleiro(tabuleiro_final)
    jogadas_max = eval(objetivo[-1])
    jogadas_atuais = 0

    if (eh_tabuleiro(tabuleiro_final)):
        t = tabuleiro_inicial()

        # Mensagens iniciais
        print('Bem-vindo ao Hello Quantum!')
        print('O seu objetivo e chegar ao tabuleiro:')
        print(tabuleiro_para_str(tabuleiro_final))
        print('Comecando com o tabuleiro que se segue:')
        print(tabuleiro_para_str(t))

        # Ciclo que vai recebendo o input do utilizador e efetuando as trocas no tabuleiro ate chegar as jogadas maximas
        while (jogadas_atuais != jogadas_max):
            porta = input('Escolha uma porta para aplicar (X, Z ou H): ')
            lado = input('Escolha um qubit para analisar (E ou D): ')

            if (porta == 'X'):
                t = porta_x(t, lado)
            elif (porta == 'Z'):
                t = porta_z(t, lado)
            elif (porta == 'H'):
                t = porta_h(t, lado)

            jogadas_atuais += 1

            print(tabuleiro_para_str(t))

        # Envia a mensagem relativa ao numero de jogadas e verifica se o numero de jogadas corresponde ao valor inserido
        if (tabuleiros_iguais(t, tabuleiro_final)):
            print('Parabens, conseguiu converter o tabuleiro em ' + str(jogadas_atuais) + ' jogadas!')
            return True
        else:
            return False
