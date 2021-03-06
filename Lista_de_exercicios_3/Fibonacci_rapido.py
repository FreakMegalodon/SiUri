"""
A fórmula de Binet é uma forma de calcular números de Fibonacci.

Sua tarefa é, dado um natural n, calcular o valor de Fibonacci(n) usando a fórmula acima.

Entrada
A entrada é um número natural n (0 < n ≤ 50).

Saída
A saída é o valor de Fibonacci(n) com 1 casa decimal utilizando a fórmula de Binet dada.
"""
#consts
raizDeCinco = 5 ** 0.5
# subs
def Fibonacci(n):
    return (((1 + raizDeCinco) / 2) ** n - ((1 - raizDeCinco) / 2) ** n) / raizDeCinco
# entradas
natural = int(input())
# saidas
print("{:.1f}".format(Fibonacci(natural)))