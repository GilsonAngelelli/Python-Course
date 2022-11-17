'''endo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

termo = int(input('Qual o primeiro termo? '))
razão = int(input('Qual a Razão? '))
decimo = + (10 - 1) * razão
print(decimo)
pa = termo
while termo < decimo + razão:
    print(termo, end= '')
    if termo < decimo:
        print(' - ', end= '')
    else:
        print(' = FIM ', end= '') 
    termo += razão
    
    