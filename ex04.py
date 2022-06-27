#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 26/06/2022
#
# 4. Desenvolva um programa em linguagem Python que recebe   
# como entrada a quantidade total de pessoas em uma          
# determinada cidade(população). Logo após, solicite ao      
# usuário quantas destas pessoas foram vacinadas com os      
# imunizantes Coronavac, Astrazeneca, Pfizer e Janssen. Com  
# estas informações, apresente em tela um pequeno relatório  
# que exibe o total de pessoas vacinadas na cidade, o        
# percentual de pessoas já vacinadas na cidade e os          
# percentuais de utilização de cada imunizante em relação ao 
# número de pessoas já vacinadas. Além disso, apresente uma  
# análise em relação ao ritmo de vacinação desta cidade,     
# conforme a tabela a seguir:                                
#                                                            
# #-------------------------#----------------------------#   
# | Percentual de vacinação |     Ritmo de Vacinação     |   
# #-------------------------#----------------------------#   
# | 0% até 15% (inclusive)  | Ritmo Lento                |   
# | 15% até 40% (inclusive) | Ritmo Mediano              |   
# | 40% até 60% (inclusive) | Ritmo Bom                  |   
# | 60% a 100%              | Ritmo Acelerado            |   
# #-------------------------#----------------------------#   

# Entrada de dados

totalPessoas = int(input("Digite a quantidade de pessoas da cidade: ")) # Solicitando a quantidade de pessoas da cidade
quantCoronavac = int(input("Digite a quantidade de coronavac: ")) # Solicitando a quantidade de pessoas vacinadas com o imunizante coronavac
quantAstrazeneca = int(input("Digite a quantidade de astrazeneca: ")) # Solicitando a quantidade de pessoas vacinadas com o imunizante astrazeneca
quantPfizer = int(input("Digite a quantidade de Pfizer: ")) # Solicitando a quantidade de pessoas vacinadas com o imunizante Pfizer
quantJanssen = int(input("Digite a quantidade de janssen: ")) # Solicitando a quantidade de pessoas vacinadas com o imunizante janssen
quantVacinados = quantCoronavac + quantAstrazeneca + quantPfizer + quantJanssen # Calculando a quantidade de pessoas vacinadas

# Tratando erros

if quantVacinados > totalPessoas: # Se a quantidade de vacinados for maior que o número da população executa o que está indentado.
    print('Erro nas informações prestadas, Motivo: Número de vacinados é maior do que a da população')

elif totalPessoas < 0 or quantCoronavac < 0 or quantAstrazeneca < 0 or quantPfizer < 0 or quantJanssen < 0: # Se qualquer informação prestada for abaixo de zero.
    print('Erro nas informações prestadas, Motivo: Número de pessoas abaixo de zero')
    
else: # Se não atender nenhuma condição de cima, será executado a identação e o código segue normalmente.
    pass # Ignora e executa o processamento dos dados. Definição -> "pass significa passar"

# Processamento de dados

porcentagemVacinados = (quantVacinados * 100) / totalPessoas # Calculando a porcentagem de pessoas vacinadas
porcentCoronavac = (quantCoronavac * 100) / quantVacinados # Calculando a porcentagem de pessoas vacinadas com o imunizante coronavac
porcentAstrazeneca = (quantAstrazeneca * 100) / quantVacinados # Calculando a porcentagem de pessoas vacinadas com o imunizante astrazeneca
porcentPfizer = (quantPfizer * 100) / quantVacinados # Calculando a porcentagem de pessoas vacinadas com o imunizante Pfizer
porcentJanssen = (quantJanssen * 100) / quantVacinados # Calculando a porcentagem de pessoas vacinadas com o imunizante janssen

# Saída de dados

print(f"\nporcentagem de pessoas que foram vacinadas: {porcentagemVacinados}%") # Exibindo a porcentagem de pessoas que foram vacinadas
print(f"total de vacinados: {quantVacinados}") # Exibindo a quantidade de pessoas que foram vacinadas
print(f"A porcentagem de pessoas que foram vacinadas com Coronavac é {porcentCoronavac}%") # Exibindo a porcentagem de pessoas que foram vacinadas com o imunizante coronavac
print(f"A porcentagem de pessoas que foram vacinadas com Astrazeneca é {porcentAstrazeneca}%") # Exibindo a porcentagem de pessoas que foram vacinadas com o imunizante astrazeneca
print(f"A porcentagem de pessoas que foram vacinadas com Pfizer é {porcentPfizer}%") # Exibindo a porcentagem de pessoas que foram vacinadas com o imunizante Pfizer
print(f"A porcentagem de pessoas que foram vacinadas com janssen é {porcentJanssen}%") # Exibindo a porcentagem de pessoas que foram vacinadas com o imunizante janssen

# Verificando o ritmo

if (porcentagemVacinados >= 0 and porcentagemVacinados < 15): # Verificando se a porcentagem de pessoas que foram vacinadas é menor que 15%
    print("Ritmo: Lento") # Exibindo o ritmo de vacinação

elif (porcentagemVacinados >= 15 and porcentagemVacinados < 40): # Verificando se a porcentagem de pessoas que foram vacinadas é maior ou igual à 15% e menor que 40%
    print("Ritmo: Mediano") # Exibindo o ritmo de vacinação

elif (porcentagemVacinados >= 40 and porcentagemVacinados < 60): # Verificando se a porcentagem de pessoas que foram vacinadas é maior ou igual à 40% e menor que 60%
    print("Ritmo: Bom") # Exibindo o ritmo de vacinação

elif (porcentagemVacinados >= 60 and porcentagemVacinados <= 100): # Verificando se a porcentagem de pessoas que foram vacinadas é maior ou igual à 60% e menor ou igual à 100%
    print("Ritmo: Acelerado") # Exibindo o ritmo de vacinação

print("\nfim do programa") # Informando ao usuário que o programa chegou ao fim.

print('')

# Exemplo extra: 01 formatando números com a biblioteca math.

print('-----------------------------------------------------')
print("extra 01")

# importando math e usando a função trunc() que elimina todas as casas após a vírgula, função floor() que arredonda para baixo e a função ceil() arredonda para cima.
import math # Importando a biblioteca math

porcentCoronavac = math.trunc(porcentCoronavac) # trunc() está eliminando todas as casas decimais da porcentagem de pessoas que foram vacinadas com o imunizante Coronavac.
print(f"A porcentagem de pessoas que foram vacinadas com Coronavac é {porcentCoronavac}%") # Imprimindo a porcentagem de pessoas que foram vacinadas com o imunizante Coronavac.

porcentAstrazeneca = math.floor(porcentAstrazeneca) # floor() está arredondando para baixo a porcentagem de pessoas que foram vacinadas com o imunizante Astrazeneca.
print(f"A porcentagem de pessoas que foram vacinadas com Astrazeneca é {porcentAstrazeneca}%") # Imprimindo a porcentagem de pessoas que foram vacinadas com o imunizante astrazeneca

porcentPfizer = math.ceil(porcentPfizer) # ceil() está arredondando para cima a porcentagem de pessoas que foram vacinadas com o imunizante Pfizer.
print(f"A porcentagem de pessoas que foram vacinadas com Pfizer é {porcentPfizer}%") # Imprimindo a porcentagem de pessoas que foram vacinadas com o imunizante Pfizer.

porcentJanssen = math.ceil(porcentJanssen) # Arredondando para cima a porcentagem de pessoas que foram vacinadas com o imunizante janssen
print(f"A porcentagem de pessoas que foram vacinadas com janssen é {porcentJanssen}%") # Exibindo a porcentagem de pessoas que foram vacinadas com o imunizante janssen

print('-----------------------------------------------------') # Exibindo a linha
print("fim dos exemplos extras") # Exibindo o fim do exemplo extra
