'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

jog = {}
partidas = []
jog['Nome'] = str(input('Nome do Jogador: '))
vezes = int(input(f'Quandas partidas {jog["Nome"]} jogou? ' ))
for c in range(1, vezes + 1):
    partidas.append(int(input(f'QUando gols na partida {c}? ')))
jog['Gols'] = partidas[:]
jog['Total'] = sum(partidas)
print('-=' * 40)
print(jog)
print('-=' * 40)
print(f'O campo nome tem valir {jog["Nome"]}!')
print(f'O campo gols tem o valor {jog["Gols"]}!')
print(f'O campo total tem o valor {jog["Total"]}!')
print('-=' * 40)
for c in range(0, vezes):
    print(f'   => Na partida {c+1}, fez {jog["Gols"][c]} gols!')
print(f'Foi um total de {jog["Total"]} gols!')

