# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
#
#entrada
nota1 = float(input("Digite a primeira nota1: ")) # entrar com a nota 1
nota2 = float(input("Digite a segunda nota2: ")) # entrar com a nota 2
nota3 = float(input("Digite a terceira nota3: ")) # entrar com a nota 3

# processamento e saída
media = (nota1 + nota2 + nota3) / 3 # calcula a média

if (media < 40): # se a média for menor que 40
    print(f"{media} - conceito E") # imprime que o conceito é E
elif (media >= 40 and media < 60): # se a média for maior ou igual a 40 e menor que 60
    print(f"{media} - conceito D") # imprime que o conceito é D
elif (media >= 60 and media < 75): # se a média for maior ou igual a 60 e menor que 75
    print(f"{media} - conceito C") # imprime que o conceito é C
elif (media >= 75 and media < 90): # se a média for maior ou igual a 75 e menor que 90
    print(f"{media} - conceito B") # imprime que o conceito é B
else: # se a média for maior ou igual a 90
    print(f"{media} - conceito A") # imprime que o conceito é A