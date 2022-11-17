'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
vitoria = 0
while True:
    computador = randint(0, 9)
    print('=-' * 30)
    print('VAMOS JOGAR PAR OU IMPAR?')
    print('=-' * 30)
    pi = str(input('PAR OU IMPAR? [P / I] ')).strip().upper()
    while not pi in 'PI':
        pi = str(input('PAR OU IMPAR? [P / I] ')).strip().upper()[0]
    jogador = int(input('Diga um valor: '))
    print('-=' * 30)
    s = jogador + computador
    if pi == 'P':
        if s % 2 == 0:
            print('-' * 30)
            print('VOCÊ GANHOU')
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {s}, deu PAR!')
            print('-' * 30)
            vitoria += 1
        else:
            print('-' * 30)
            print('VOCÊ PERDEU - GAME OVER')
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {s}, deu IMPAR!')
            print('-' * 30)
            break
    if pi == 'I':
        if s % 2 == 1:
            print('-' * 30)
            print('VOCÊ GANHOU')
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {s}, deu PAR!')
            print('-' * 30)
            vitoria += 1
        else:
            print('-' * 30)
            print('VOCÊ PERDEU - GAME OVER')
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {s}, deu IMPAR!')
            print('-' * 30)
            break
print(f'Você ganhou {vitoria} vezes!')