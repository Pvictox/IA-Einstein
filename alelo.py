import random

def criarAlelo(listaX):
    
    while(len(listaX) < 5):
             
        numero_escolhido = random.randint(1,5)
        if (listaX.__contains__(numero_escolhido) == False):
            listaX.append(numero_escolhido)
        
    
    return listaX
