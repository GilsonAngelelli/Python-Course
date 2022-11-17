'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
computador = randint(0, 11)
print('PENSEI EM UM NÚMERO ENTRE 0 E 10.')
print('SERÁ QUE VOCÊ CONSEGUE ADIVINHAR QUAL FOI?')
print('-=' * 25)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('MENOS')
        else: print('MAIS')
print('ACERTOU NA {}ª TENTATIVA.' .format(palpites))


