'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

num =  c = 0
print('-=' * 30)
num = int(input('Quer ver a tabuada de qual número? '))
print('-=' * 30)
while True:
    for c in range(0, 10):
        c += 1
        print(f'{num} x {c} = {c*num}')
    else:
        print('-=' * 30)
        num = int(input('Quer ver a tabuada de qual número? '))
        print('-=' * 30)
    if num < 0:
        break
print('PROGRAMA DE TABUADA ENCERRADO')