#
# entrada
valorTotalCompra = float(input("Digite o valor total da compra: "))
print("-----------------------------------------------------")
print("Forma de pagamento:")
print("0 - à vista no dinheiro, desconto 10%")
print("1 - à vista no cartão, desconto 5%")
print("2 - em até 2x no cartão, sem juros")
print("3 - em até 3x no cartão, juros de 5%")
print('-----------------------------------------------------')
formaPagamento = int(input("Digite a forma de pagamento: "))

#processamento e saida
if formaPagamento == 0: # se for 0
    valorTotalCompra = valorTotalCompra * 0.9
    print("pagamento a vista no dinheiro")
    print("desconto de 10%")
    print(f"O valor total da compra é {valorTotalCompra}")  # saída do valor total da compra
elif formaPagamento == 1: # se for 1
    print("pagamento a vista no cartão")
    print("desconto de 5%")
    valorTotalCompra = valorTotalCompra * 0.95
    print(f"O valor total da compra é {valorTotalCompra}")  # saída do valor total da compra
elif formaPagamento == 2: # se for 2
    print("pagamento em até 2x no cartão")
    print("sem juros")
    print(f"O valor total da compra é {valorTotalCompra}")  # saída do valor total da compra
    print("parcela 1:", valorTotalCompra / 2) # saída da primeira parcela
    print("parcela 2:", valorTotalCompra / 2) # saída da segunda parcela
elif formaPagamento == 3: # se for 3
    print("pagamento em até 3x no cartão")
    print("juros de 5%")
    print(f"O valor total da compra é {valorTotalCompra}")  # saída do valor total da compra
    valorTotalCompra = valorTotalCompra * 1.05
    print(f"O valor total da compra com juros é {valorTotalCompra}")  # saída do valor total da compra
    print("parcela 1:", valorTotalCompra / 3) # saída da primeira parcela
    print("parcela 2:", valorTotalCompra / 3) # saída da segunda parcela
    print("parcela 3:", valorTotalCompra / 3) # saída da terceira parcela
else: # se não for nenhuma das opções acima
    print("Forma de pagamento inválida")  # saída
print("Fim do programa")
