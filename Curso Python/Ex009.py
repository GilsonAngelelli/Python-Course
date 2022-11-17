#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

print('===============LOJA GILSON ANGELELLI===============')
compra = int(input('QUal o valor da compra? '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = compra * 0.90
elif opcao == 2:
    total = compra * 0.95
elif opcao == 3:
    total = compra
    parcela = total / 2
    print('Sua compra será divida em duas parcelas de R${:.2f}.' .format(parcela))
elif opcao == 4:
    total = compra * 1.2
    totparc = int(input('Quantas Parcelas? '))
    parcela = total / totparc
    print('Sua compra será divida em {} parcelas de R${:.2f}.' .format(totparc, parcela))
else:
    print('Opção invalida, tente novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f}!'.format(compra, total))
