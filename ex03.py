
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
#
# entrada
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
sexo = input("Digite o seu sexo: ")

# processamento e saida
if (sexo == "M" or sexo == "m"): # se for m ou M
    ideal = (72.7 * altura) - 58 # calcula o peso ideal
    if (peso > ideal): # se o peso for maior que o ideal
        print(f"Você está acima do peso ideal") # imprime que está acima do peso ideal
    elif (peso < ideal): # se o peso for menor que o ideal
        print(f"Você está abaixo do peso ideal") # imprime que está abaixo do peso ideal
    print(f"O seu peso ideal é {ideal}, seu peso atual é {peso}") # imprime o peso ideal e o peso atual
elif (sexo == "F" or sexo == "f"): # se for f ou F
    ideal = (62.1 * altura) - 44.7 # calcula o peso ideal
    if (peso > ideal): # se o peso for maior que o ideal
        print(f"Você está acima do peso ideal") # imprime que está acima do peso ideal
    elif (peso < ideal): # se o peso for menor que o ideal
        print(f"Você está abaixo do peso ideal") # imprime que está abaixo do peso ideal
    print(f"O seu peso ideal é {ideal}, seu peso atual é {peso}") # imprime o peso ideal e o peso atual
