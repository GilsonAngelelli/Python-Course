'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da palmeiras.'''

time1 = ('América-MG', 'Athletico', 'Atlético-GO', 'Atlético-MG', 'Avaí',  'Botafogo', 'Bragantino', 'Ceará', 'Corinthians', 'Coritiba', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Juventude', 'Internacional', 'Palmeiras', 'Santos', 'São Paulo')
print(f' Os cinco primeiros times são {time1[:5]}')
print(f'Os últimos quatro são {time1[16:]}')
print(f'{sorted(time1)}')
print({time1.index('Palmeiras')+1})

