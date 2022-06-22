#
#entrada
# quantidade de pessoas da cidade
totalPessoas = int(input("Digite a quantidade de pessoas da cidade: "))
# quantidade de pessoas que foram vacinadas com Coronavac
quantCoronavac = int(input("Digite a quantidade de coronavírus: "))
# quantidade de pessoas que foram vacinadas com Astrazeneca
quantAstrazeneca = int(input("Digite a quantidade de astrazeneca: "))
# quantidade de pessoas que foram vacinadas com Pfizer
quantPfizer = int(input("Digite a quantidade de Pfizer: "))
# quantidade de pessoas que foram vacinadas com janssen
quantJanssen = int(input("Digite a quantidade de janssen: "))

# processamento
# quantidade de vacinados
quantVacinados = quantCoronavac + quantAstrazeneca + quantPfizer + quantJanssen
porcentagemVacinados = (quantVacinados * 100) / totalPessoas
# calcula a porcentagem de pessoas que foram vacinadas com Coronavac
porcentCoronavac = (quantCoronavac * 100) / quantVacinados
# calcula a porcentagem de pessoas que foram vacinadas com Astrazeneca
porcentAstrazeneca = (quantAstrazeneca * 100) / quantVacinados
# calcula a porcentagem de pessoas que foram vacinadas com Pfizer
porcentPfizer = (quantPfizer * 100) / quantVacinados
# calcula a porcentagem de pessoas que foram vacinadas com janssen
porcentJanssen = (quantJanssen * 100) / quantVacinados

# saída
print(f"porcentagem de pessoas que foram vacinadas: {porcentagemVacinados}%")
print(f"total de vacinados: {quantVacinados}")
print(f"A porcentagem de pessoas que foram vacinadas com Coronavac é {porcentCoronavac}%")
print(f"A porcentagem de pessoas que foram vacinadas com Astrazeneca é {porcentAstrazeneca}%")
print(f"A porcentagem de pessoas que foram vacinadas com Pfizer é {porcentPfizer}%")
print(f"A porcentagem de pessoas que foram vacinadas com janssen é {porcentJanssen}%")

# ritmo
if (porcentagemVacinados >= 0 and porcentagemVacinados < 15):
    print("Ritmo: Lento")
elif (porcentagemVacinados >= 15 and porcentagemVacinados < 40):
    print("Ritmo: Mediano")
elif (porcentagemVacinados >= 40 and porcentagemVacinados < 60):
    print("Ritmo: Bom")
elif (porcentagemVacinados >= 60 and porcentagemVacinados <= 100):
    print("Ritmo: Acelerado")

print("Fim do programa")

# extra 01
print('-----------------------------------------------------')
print("extra 01")
# caso queira arredondar o valor da porcentagem
# import math e use a função trunc() arrendoda para baixo ou floor() arredonda para baixo, ceil() arredonda para cima
import math
porcentCoronavac = math.trunc(porcentCoronavac)
print(f"A porcentagem de pessoas que foram vacinadas com Coronavac é {porcentCoronavac}%")
porcentAstrazeneca = math.floor(porcentAstrazeneca)
print(f"A porcentagem de pessoas que foram vacinadas com Astrazeneca é {porcentAstrazeneca}%")
porcentPfizer = math.ceil(porcentPfizer)
print(f"A porcentagem de pessoas que foram vacinadas com Pfizer é {porcentPfizer}%")
porcentJanssen = math.ceil(porcentJanssen)
print(f"A porcentagem de pessoas que foram vacinadas com janssen é {porcentJanssen}%")
