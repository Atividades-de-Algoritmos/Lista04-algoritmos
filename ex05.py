#
# entrada
valorTotalCompra = float(input("Digite o valor total da compra: "))
print("-----------------------------------------------------")
print("Forma de pagamento:")
print("0 - à vista no dinheiro")
print("1 - à vista no cartão")
print("2 - em até 2x no cartão")
print("3 - em até 3x no cartão")
print('-----------------------------------------------------')
formaPagamento = int(input("Digite a forma de pagamento: "))

#processamento e saida
if formaPagamento == 0: # se for 0
    print("pagamento a vista no dinheiro")
    if valorTotalCompra <= 100:
        print("desconto de 5%")
        print(f"O valor da compra é {valorTotalCompra} e o valor do desconto é {valorTotalCompra * 0.05}")
        print(f"valor a ser pago é {valorTotalCompra - (valorTotalCompra * 0.05)}")
    elif valorTotalCompra > 100 and valorTotalCompra <= 500:
        print("desconto de 10%")
        print(f"O valor da compra é {valorTotalCompra} e o valor do desconto é {valorTotalCompra * 0.10}")
        print(f"valor a ser pago é {valorTotalCompra - (valorTotalCompra * 0.10)}")
    else:
        print("desconto de 15%")
        print(f"O valor da compra é {valorTotalCompra} e o valor do desconto é {valorTotalCompra * 0.15}")
        print(f"valor a ser pago é {valorTotalCompra - (valorTotalCompra * 0.15)}")
elif formaPagamento == 1: # se for 1
    print("pagamento a vista no cartão")
    if valorTotalCompra <= 100:
        print("desconto de 5%")
        print(f"O valor da compra é {valorTotalCompra} e o valor do desconto é {valorTotalCompra * 0.05}")
        print(f"valor a ser pago é {valorTotalCompra - (valorTotalCompra * 0.05)}")
    elif valorTotalCompra > 100 and valorTotalCompra <= 500:
        print("desconto de 10%")
        print(f"O valor da compra é {valorTotalCompra} e o valor do desconto é {valorTotalCompra * 0.10}")
        print(f"valor a ser pago é {valorTotalCompra - (valorTotalCompra * 0.10)}")
    else:
        print("desconto de 15%")
        print(f"O valor da compra é {valorTotalCompra} e o valor do desconto é {valorTotalCompra * 0.15}")
        print(f"valor a ser pago é {valorTotalCompra - (valorTotalCompra * 0.15)}")
elif formaPagamento == 2: # se for 2
    print("pagamento em até 2x no cartão")
    print("juros de 5%")
    print(f"O valor da compra é {valorTotalCompra} e o valor com juros é {valorTotalCompra * 1.05}")
    valorParcelado = valorTotalCompra + (valorTotalCompra * 0.05)
    print("parcela 1:", valorParcelado / 2) # saída da primeira parcela
    print("parcela 2:", valorParcelado / 2) # saída da segunda parcela
elif formaPagamento == 3: # se for 3
    print("pagamento em até 3x no cartão")
    print("juros de 5%")
    print(f"O valor da compra é {valorTotalCompra} e o valor com juros é {valorTotalCompra * 1.05}")
    valorParcelado = valorTotalCompra + (valorTotalCompra * 0.05)
    print("parcela 1:", valorParcelado / 3) # saída da primeira parcela
    print("parcela 2:", valorParcelado / 3) # saída da segunda parcela
    print("parcela 3:", valorParcelado / 3) # saída da terceira parcela
else: # se não for nenhuma das opções acima
    print("Forma de pagamento inválida")  # saída
print("Fim do programa")
