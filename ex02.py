#
#entrada
nota1 = float(input("Digite a primeira nota1: "))
nota2 = float(input("Digite a segunda nota2: "))
nota3 = float(input("Digite a terceira nota3: "))

# processamento e saída
media = (nota1 + nota2 + nota3) / 3

if (media < 40):
    print(f"{media} - conceito E")
elif (media >= 40 and media < 60):
    print(f"{media} - conceito D")
elif (media >= 60 and media < 75):
    print(f"{media} - conceito C")
elif (media >= 75 and media < 90):
    print(f"{media} - conceito B")
else:
    print(f"{media} - conceito A")