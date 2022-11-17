#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

s = 0
cont = 0
for c in range(1, 500,):
    if c % 3 ==0:
        s += c
        cont = cont + 1
print('O total de multiplos de 3 no intervalo de 0 a 500 são {} e somados equivalem à {}.' .format(cont, s))
