'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.'''

num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')

while True:
    while True:
        a = int(input('Digite um número entre 0 e 10: '))
        if a <= 10 and a >= 0:
            break
        print('Tente novamente!', end=' ')
    print(f'Você escolheu o número {num[a]}!')
    cont = str(input('Quer continuar? [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
print('Programa encerrado')
        
