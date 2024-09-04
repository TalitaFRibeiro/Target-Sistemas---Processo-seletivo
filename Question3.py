import json
# Abrindo o arquivo dados.json, onde está a tabela
with open("Dados/dados.json", encoding = 'utf-8') as dados_json:
    dados = json.load(dados_json)


def faturamento(): 
    #Essa função soma todos os faturamentos do mês, que não são
    # zeros e conta quantos dias de rendimentos tiveram
    a = [] 
    soma = 0
    cont = 0 # Contador de dias de rendimento
    minimo = 999999  #Mínimo inicial
    maximo = 0 #Máximo inicial
    for faturamento in dados:
        valor = faturamento['valor']
        dia = faturamento['dia']
        
        if(valor > 0):
            soma+= valor
            cont+= 1
            if (valor < minimo):
                minimo = valor
                diamin = faturamento['dia'] 

            else:
                if(valor > maximo):
                    maximo = valor
                    diamax = faturamento['dia']
            

    media = soma/cont
    print(f'O menor valor de faturamento foi R$ {round(minimo,2)} no dia {diamin}.\n')
    print(f'O valor máximo de faturamento foi R$ {round(maximo,2)} no dia {diamax}.\n')
    conta_dias(media)
    

def conta_dias(media):
    # Conta quantos dias foram superiores a média mensal
    cont = 0
    for faturamento in dados:
        valor = faturamento['valor']
        if(valor > media):
            cont+= 1
    print(f'Número de dias no mês em que o valor de faturamento diário foi superior a média mensal: {cont} dias.')


## main ##

faturamento()
