'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.'''

n1 = int(input('Quantos termo você quer mostrar? '))
t1 = 0
t2 = 1
print('{} - {} ' .format(t1, t2), end='')
cont = 3
while cont <= n1:
    t3 = t1 + t2
    print('- {} ' .format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('- FIM')

