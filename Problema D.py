#adiciona uma aresta ao grafo
def add(grafo, a, b):
    try:
        grafo[a].append(b)
    except:
        grafo[a] = [b]
    try:
        grafo[b].append(a)
    except:
        grafo[b] = [a]
    return grafo

#processa o grafo
def percorrer(grafo):
    #começa da primeira areta
    visitados = ['1']
    pilha = ['1']

    #inicializa as variaveis de utilildade
    cont = 0
    anterior = {}

    #enquanto a pilha não estiver vazia, continua rodando
    while pilha:
        #pega o ultimo item adicionado na pilha
        u = pilha.pop()

        #marca que o item foi percorrido
        if u not in visitados:
            visitados.append(u)

        #percorre os seus caminhos
        for v in grafo[u][::-1]:
            #adiciona o item como anterior de seu caminho
            anterior[v] = u

            #verfica se o caminho ja não ira ser processado
            if v not in pilha:
                #verifica se o caminho já não foi visitado/processado
                if v not in visitados:
                    #se não foi, coloca ele na fila de processamento
                    pilha.append(v)
                else:
                    #se foi, verifica se ele não é seu anterior
                    if v != anterior[u]:
                        #se não é, adiciona mais uma mancha ao contador
                        cont +=1

    #retorna a quantidade de manchas contadas
    return cont
    
#inicializa o grafo das manchas
grafo = {}
#le a quantidade de arestas e a quantidade de caminhos
N, M = list(map(int, input().split()))

#le todos os caminhos...
for _ in range(M):
    a, b = input().split()
    #e adiciona no grafo
    add(grafo, a, b)
#envia o grafo para ser processado e escreve o valor retornado
print(percorrer(grafo))
        
    
'''
caso de teste 1:
4 5
1 2
2 3
2 4
3 4
3 1
'''

'''
caso de teste 2:
26 38
1 2
1 15
2 3
2 17
3 25
3 4
4 5
5 6
5 25
25 23
23 24
23 22
24 18
24 17
17 16
16 15
16 14
15 14
14 13
13 12
13 18
18 19
19 20
19 21
20 12
20 9
20 21
21 22
21 8 
8 9 
8 7
9 10
10 11
11 12
7 26
7 6
6 26
26 22
'''
