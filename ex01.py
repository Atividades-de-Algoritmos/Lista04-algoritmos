#
#entrada
valor1 = int(input("Digite um valor: "))

# processamento e saída
if valor1 % 2 == 0:
    print(f"O valor {valor1} é par") # saída
else:
    print("O valor é impar")  # saída

print("Fim do programa")


print('-----------------------------------------------------')
# extra 01
# se for apenas para verificar o valor é impar, não precisa de else
if not(valor1 % 2) == 0:
    print(f"O valor {valor1} é impar") # saída
