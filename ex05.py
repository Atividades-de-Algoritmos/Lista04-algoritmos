#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 26/06/2022
#
# 5. Ao efetuar uma compra em uma determinada loja, o cliente
# pode realizar o pagamento à vista ou a prazo/parcelado no  
# cartão (sem juros). Caso opte por pagar à vista, ele terá  
# um percentual de desconto diferente,dependendo do valor    
# total de sua compra. Ao selecionar o pagamento de forma    
# parcelada, o cliente pode realizara compra em no máximo    
# três parcelas. Sabendo disto,e com o auxílio da tabela     
# apresentada nesta questão, implemente um programa em       
# linguagem Python que recebe do usuário o valor total de sua
# compra e a forma de pagamento por ele desejada. A forma de 
# pagamento pode ser representada por um valor inteiro, em   
# que os números 0 indica pagamento a vista em dinheiro, 1   
# indica pagamento à vista no cartão, 2 o pagamento em duas  
# parcelas e 3 o pagamento em três parcelas. Qualquer outro  
# valor fornecido pelo usuário para a forma de pagamento deve
# ser considerado inválido. Após receber estas informações   
# iniciais, o programa deve exibir para o usuário o valor da 
# compra com desconto, caso a forma de pagamento escolhida   
# tenha sido à vista, ou o valor das parcelas de pagamento,  
# caso a opção tenha sido pela compra a prazo.               
#                                                            
# #--------------------#-----------------#------------------#
# | Forma de Pagamento | Valor da Compra | Desconto / Juros |
# #--------------------#-----------------#------------------#
# |                    | Menos R$ 100,00 | 5% de desconto   |
# |                    #-----------------#------------------#
# |      À Vista.      | Entre R$ 100,00 |      10% de      |
# |   (Opção 0 ou 1)   |   E R$ 500,00   |   de Desconto.   |
# |                    #-----------------#------------------#
# |                    | Acima R$ 500,00 | 15% de desconto  |
# #--------------------#-----------------#------------------#
# | À Prazo(Parcelado) |      Valor      | 5% em Juros para |
# |    No máximo 3x    |    Qualquer.    | Ser Acrescentado |
# #--------------------#-----------------#------------------#

# Entrada de dados

valorCompra = float(input("Digite o valor total da compra: ")) # Solicita o valor da compra

print("-----------------------------------------------------")
print("Forma de pagamento:")
print("0 - à vista no dinheiro")
print("1 - à vista no cartão")
print("2 - em até 2x no cartão")
print("3 - em até 3x no cartão")
print('-----------------------------------------------------')

formaPagamento = int(input("Digite a forma de pagamento: ")) # Solicita a forma de pagar

# Processamento e saída de dados

if formaPagamento == 0: # Se a forma de pagamento for igual a 0 executa o bloco abaixo.
  
  print("pagamento a vista no dinheiro")
  
  if valorCompra <= 100: # Se o valor da compra for menor igual que 100 executa em baixo.
    
    print("desconto de 5%")
    print(f"O valor da compra é {valorCompra} e o valor do desconto é {valorCompra * 0.05}")
    print(f"valor a ser pago é {valorCompra - (valorCompra * 0.05)}")
  
  elif valorCompra > 100 and valorCompra <= 500: # Se for maior que 100 e menor igual 500.
    
    print("desconto de 10%")
    print(f"O valor da compra é {valorCompra} e o valor do desconto é {valorCompra * 0.10}")
    print(f"valor a ser pago é {valorCompra - (valorCompra * 0.10)}")
  
  else: # Se não for nenhuma condição de cima executa o que está indentado.
    
    print("desconto de 15%")
    print(f"O valor da compra é {valorCompra} e o valor do desconto é {valorCompra * 0.15}")
    print(f"valor a ser pago é {valorCompra - (valorCompra * 0.15)}")

elif formaPagamento == 1: # Se a opção de pagamento for igual a 1 executa abaixo.
  
  print("pagamento a vista no cartão")
  
  if valorCompra <= 100: # Se o valor da compra for menor igual que 100 executa em baixo.
    
    print("desconto de 5%")
    print(f"O valor da compra é {valorCompra} e o valor do desconto é {valorCompra * 0.05}")
    print(f"valor a ser pago é {valorCompra - (valorCompra * 0.05)}")
  
  elif valorCompra > 100 and valorCompra <= 500: # Se for maior que 100 e menor igual 500.
    
    print("desconto de 10%")
    print(f"O valor da compra é {valorCompra} e o valor do desconto é {valorCompra * 0.10}")
    print(f"valor a ser pago é {valorCompra - (valorCompra * 0.10)}")
  
  else: # Se não for nenhuma condição de cima executa o que está indentado.
    
    print("desconto de 15%")
    print(f"O valor da compra é {valorCompra} e o valor do desconto é {valorCompra * 0.15}")
    print(f"valor a ser pago é {valorCompra - (valorCompra * 0.15)}")

elif formaPagamento == 2: # Se a forma de pagamento for igual a 2 executa abaixo.
  
  print("pagamento em até 2x no cartão")
  print("juros de 5%")
  print(f"O valor da compra é {valorCompra} e o valor com juros é {valorCompra * 1.05}")
  valorParcelado = valorCompra + (valorCompra * 0.05)
  print("parcela 1:", valorParcelado / 2) # saída da primeira parcela
  print("parcela 2:", valorParcelado / 2) # saída da segunda parcela

elif formaPagamento == 3: # Se a forma do pagamento for igual a 3 executa abaixo.
  print("pagamento em até 3x no cartão")
  print("juros de 5%")
  print(f"O valor da compra é {valorCompra} e o valor com juros é {valorCompra * 1.05}")
  valorParcelado = valorCompra + (valorCompra * 0.05)
  print("parcela 1:", valorParcelado / 3) # saída da primeira parcela
  print("parcela 2:", valorParcelado / 3) # saída da segunda parcela
  print("parcela 3:", valorParcelado / 3) # saída da terceira parcela

else: # se não for nenhuma das opções acima
  print("Forma de pagamento inválida") # saída
print("fim do programa")
