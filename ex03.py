#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 26/06/2022
#
# 3. Elabore um programa em linguagem Python que calcule     
# valor do seu peso ideal de uma determinada pessoa e informe
# se o seu peso atual é o ideal, ou se o seu peso está abaixo
# ou acima do valor ideal calculado. Para isso, o usuário    
# deve informar a sua altura e o seu peso. O cálculo do peso 
# ideal dependerá do sexo informado:                         
#                                                            
#     • Para homens: (72.7 * h) – 58                         
#     • Para mulheres: (62.1 * h) – 44.7                     
#                                                            
# Observação. Utilize os caracteres “M” ou “m” para          
# representar o sexo masculino e os caracteres “F” ou “f”    
# para representar o sexo feminino.                          

# Entrada

altura = float(input("Digite a sua altura: ")) # Solicitando a altura do usuário
peso = float(input("Digite o seu peso: ")) # Solicitando o peso do usuário
sexo = input("Digite o seu sexo: ") # Solicitando o sexo do usuário

# Processamento e saída

if (sexo == "M" or sexo == "m"): # Se o usuário for do sexo masculino
    ideal = (72.7 * altura) - 58 # Calculamos o peso ideal do usuário
    if (peso > ideal): # se o peso do usuário for maior que o peso ideal
        print(f"Você está acima do peso ideal") # Informamos que o usuário está acima do peso ideal
    
    elif (peso < ideal): # Caso contrário, se o peso do usuário for menor que o peso ideal
        print(f"Você está abaixo do peso ideal") # Informamos que o usuário está abaixo do peso ideal
    print(f"O seu peso ideal é {ideal}, seu peso atual é {peso}") # Informamos o peso ideal e o peso atual do usuário

elif (sexo == "F" or sexo == "f"): # Caso a usuária for do sexo feminino
    ideal = (62.1 * altura) - 44.7 # Calculamos o peso ideal da usuária
    if (peso > ideal): # se o peso da usuária for maior que o peso ideal
        print(f"Você está acima do peso ideal") # Informamos que a usuária está acima do peso ideal
    
    elif (peso < ideal): # Caso contrário, se o peso da usuária for menor que o peso ideal
        print(f"Você está abaixo do peso ideal") # Informamos que a usuária está abaixo do peso ideal
    print(f"O seu peso ideal é {ideal}, seu peso atual é {peso}") # Informamos o peso ideal e o peso atual da usuária

print("fim do programa") # Informando ao usuário que o programa terminou
