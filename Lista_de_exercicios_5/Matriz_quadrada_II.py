"""
Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e construa a matriz 
de acordo com o exemplo abaixo.

Entrada

A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. O final da 
entrada é marcado por um valor de ordem igual a zero (0).

Saída

Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. (os valores das matrizes devem ser 
formatados em um campo de tamanho 3 justificados à direita e separados por espaço. Após o último caractere de cada linha da matriz 
não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.
"""
# subs
def matrizGerada(larg):
    matriz = []
    for i in range(larg):
        linha = [1] * larg
        matriz.append(linha)
    return matriz

def operarNaMatriz(vs):
    for i in range(len(vs)):
        for j in range(len(vs)):
            vs[i][j] += max(i, j) - min(i, j)

# entradas
larguraDaMatriz = int(input())
# processos
while larguraDaMatriz != 0:
    matriz          = matrizGerada(larguraDaMatriz)
    operarNaMatriz(matriz)
    for i in range(larguraDaMatriz):
        for j in range(larguraDaMatriz - 1):
            print("%3d "%matriz[i][j], end="")
        print("%3d"%matriz[i][larguraDaMatriz - 1])
    print()
    larguraDaMatriz = int(input())