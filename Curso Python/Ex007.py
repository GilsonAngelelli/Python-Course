#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

l1 = float(input('Primeiro Segmento: '))
l2 = float(input('Segundo Segmento: '))
l3 = float(input('Terceiro Segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('O triangulo existe!')
    if l1 == l2 == l3:
        print('EQUILATERO!')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('O triangulo não existe!')
