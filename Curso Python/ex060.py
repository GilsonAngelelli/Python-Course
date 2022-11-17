time = []
jog = {}
partidas = []
while True:
    jog.clear()
    jog['Nome'] = str(input('Nome do Jogador: '))
    vezes = int(input(f'Quandas partidas {jog["Nome"]} jogou? ' ))
    partidas.clear()
    for c in range(1, vezes + 1):
        partidas.append(int(input(f'QUando gols na partida {c}? ')))
    jog['Gols'] = partidas[:]
    jog['Total'] = sum(partidas)
    time.append(jog.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if resp == 'N':
        break
print('-' * 40)
print('cod ', end='')
for i in jog.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:<3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogardom com o código {busca}')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'        No jogo {i+1} fez {g} gols')
print('VOLTE SEMPRE')
