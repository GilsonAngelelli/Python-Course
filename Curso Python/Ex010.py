#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''SUAS OPÇÕES
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('=' * 25)
print('Computador jogou {}' .format(itens[computador]))
print('jogador jogou {}' .format(itens[jogador]))
print('=' * 25)
if computador == 0: # jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ GANHOU')
    elif jogador == 2:
        print('VOCÊ PERDEU')
    else:print('JOGADA INVALIDA'
        )
elif computador == 1: # jogou PAPEL
    if jogador == 0:
        print('VOCÊ PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ GANHOU')
    else:
        print('JOGADA INVALIDA')
elif computador == 2: # jogou TESOURA
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')