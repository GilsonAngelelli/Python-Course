valor = []
cont = 0
while True:
    valor.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? '))
    if cont in 'Nn':
        break
print(f'-=' * 30)
print(f'voce digitou {len(valor)} elementos')
valor.sort(reverse = True)
print(f'Os valores em ordem decrecente são {valor}')
if 5 in valor:
    print(f'O valor 5 faz parte da lista')
else:
    print('O valor não foi encontrado')
