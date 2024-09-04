def fibi(n): 
    # Gerando os números da sequência de fibonacci até aparecer     # um número maior do que ele na sequência 
    n = n + 1
    listafib = []
    for i in range(n):
        if(i==0):
            listafib.append(0)
        elif(i==1):
            listafib.append(1)
        else:
            temp = listafib[i-1] + listafib[i-2]
            listafib.append(temp)
            if(temp>=n):
                break
    return listafib

def procura(vetor,n): #Procurando o número de fibonacci no vetor
    piso = 0
    teto = len(vetor)-1
    while(piso<=teto):
        meio = (piso + teto)//2;

        if(n>vetor[meio]):
            piso = meio + 1
        elif(n == vetor[meio]):
            return "Pertence a sequência!"
        else:
            teto = meio - 1
    return "Não pertence a sequência!"
    
##### Main ######

num = int(input("Qual o número que deseja verificar se está na sequência de fibonacci? "))
resp = procura(fibi(num),num)
print(f'{resp}\n')
