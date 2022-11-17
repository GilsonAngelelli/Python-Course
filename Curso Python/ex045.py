num = list()
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
    else:
        print('Valor repetido!')
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r in 'Nn':
        break
num.sort()
print(f'Você digitou os valores {num}')