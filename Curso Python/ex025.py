'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:'''

from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
c = n
while c > 0:
    print('{}' .format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = {}' .format(factorial(n)), end='')
    c -= 1