valor = []
cont = 0
pares = list()
impares = list()
while True:
    valor.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? '))
    if cont in 'Nn':
        break
for i, v in enumerate(valor):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista completa é {valor}')
print(f'Os valores pares são {pares}')
print(f'Os valores impares são {impares}')


