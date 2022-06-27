#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 26/06/2022
#
# 1. Recebe um valor do usuário e retorna se é impar ou par.

# Entrada de dados

valor1 = int(input("Digite um valor: ")) # Solicitando um número inteiro do usuário

# processamento e saída de dados

if valor1 % 2 == 0: # se o valor for par, vai imprimir o resultado
    print(f"O valor {valor1} é par") 

else: # se for o valor for impar, vai imprimir o resultado
    print("O valor é impar") 

print("fim do programa") # Informando ao usuário que o programa terminou


# extra 01

# Entrada de dados (Mesma do anterior)

# Processamento e saída de dados

# Se for apenas para verificar o valor é impar, não precisa de else

if not(valor1 % 2) == 0: # Se não for par, ou seja, se for impar
    print(f"O valor {valor1} é impar") # saída
