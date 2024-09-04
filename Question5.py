def invertendo(frase): #Invertendo a frase original
        frase_inv = ''
        tamanho = len(frase)
        for letra in range(tamanho):
            #Percorrendo a string,concatenando as letras de trás 
            # com as letras no formato normal de leitura
            frase_inv += frase[(tamanho-1)-letra] 
        print(f'{frase_inv}')
        
    

def captando_frase(): # Capiturando a frase
    frase = input('Digite a frase:\n')
    invertendo(frase)


## main ##

captando_frase()
