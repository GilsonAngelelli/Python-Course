n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1 < n2:
    print('{} é menor que {}!' .format(n1, n2))
elif n1 > n2:
    print('{} é maior que {}!' .format(n1, n2))
else:
    print('{} é igual a {}!' .format(n1, n2))