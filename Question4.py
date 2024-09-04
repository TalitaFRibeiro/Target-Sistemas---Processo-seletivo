def percentual(lista,soma): 
    #Calculando o percentual de cada Estado
    for estado in lista:
        valor = lista[estado]
        porcentagem = (valor*100)/soma
        #Mostrando o percentual para cada Estado
        print(f'Estado: {estado} \tPorcentagem: {round(porcentagem,2)}%\n')

def criando_lista_estados():
    #Criando o dicionário com os valores e os Estados
    lista_faturamento ={"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53 }
    return lista_faturamento

def somar(lista_faturamento):
    #Somando o valor total faturado
    soma = 0
    for estado in lista_faturamento:
        valor = lista_faturamento[estado]
        soma = soma + valor
    return soma


## main ##

lista = criando_lista_estados()
somatotal = somar(lista)
percentual(lista,somatotal)

