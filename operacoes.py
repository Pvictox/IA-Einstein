from cromossomo import Cromossomo
import random
import numpy.random as npr
import fitness
import numpy as np
def mutacao(cromossomo):
    #Pegar primeiro uma casa aleatória
    numero_casa = random.randint(0,4)
    #Setar a característica que vai ser mudada de forma aleatória
    num_caracteristica = random.randint(0,4)
    pos_caracteristica = 0
    if (num_caracteristica == 0): #Mudar a nacionalidade
        mutaAlelo(cromossomo.getNacionalidade())
    elif(num_caracteristica==1):  #Mudar pet
        
        mutaAlelo(cromossomo.getPet())
       
    elif(num_caracteristica==2): #Mudar cor
       
        mutaAlelo(cromossomo.getCor())
        
    elif(num_caracteristica ==3): #Mudar bebida
       
        mutaAlelo(cromossomo.getBebida())
        
    elif(num_caracteristica==4): #Mudar cigarro
       
        mutaAlelo(cromossomo.getCigarro())
       


def mutaAlelo(lista):
    pos_caracteristica = random.randint(0,4)
    chance = random.randint(0,100)
    if(pos_caracteristica == 0):
        swapSucessor(lista=lista, posicao=pos_caracteristica)
    elif(pos_caracteristica == 4):
        swapAntecessor(lista=lista, posicao=pos_caracteristica)
    else:
        if (chance <=50):
            swapAntecessor(lista=lista, posicao=pos_caracteristica)
        else:
            swapSucessor(lista=lista, posicao=pos_caracteristica)
        


def swapAntecessor(lista, posicao):
    aux = lista[posicao-1] 
    lista[posicao-1] = lista[posicao]
    lista[posicao] = aux 

def swapSucessor(lista, posicao):
    aux = lista[posicao+1] 
    lista[posicao+1] = lista[posicao]
    lista[posicao] = aux 




def roletaCromossomo(population):
    for c in population:
        if (c.getPontos() == 0):
            c.addConsolacao()       
    max = sum([c.getPontos()for c in population])
    selection_probs = [c.getPontos()/max for c in population]
    for c in population:
        if (c.getPontos() == 0.5):
            c.removeConsolacao(0)
        
    pai_Selecionado = population[npr.choice(len(population), p=selection_probs)]
     
    return pai_Selecionado, selection_probs




def retornaUltimosAlelos(aleloFilho, listaPai):
    values = listaPai[3:]
    for value in values:
        aleloFilho.append(value)
    return aleloFilho

def retornaPrimeirosAlelos(aleloFilho, listaMae):
    values = listaMae[:3]
    for value in values:
        aleloFilho.append(value) 
    return aleloFilho


#Pegar bebida e Cigarro do pai 
# Nacionalidade, pet, cor da mãe

# depois para ou outro filho fazer o inverso
def crossover(cromossomoPai, cromossomoMae):
    aleloFilhoCigarro = []
    aleloFilhoBebida = []
    aleloFilhoCor = []
    aleloFilhoPet = []
    aleloFilhoNacionalidade= []
    


    aleloFilhoBebida = cromossomoPai.getBebida()
    aleloFilhoCigarro = cromossomoPai.getCigarro()
    aleloFilhoCor = cromossomoMae.getCor()
    aleloFilhoNacionalidade = cromossomoMae.getNacionalidade()
    aleloFilhoPet = cromossomoMae.getPet()
    

    primeiroFilho = Cromossomo(aleloFilhoNacionalidade, aleloFilhoPet, aleloFilhoCor, aleloFilhoBebida, aleloFilhoCigarro)

    aleloFilhoCigarro = []
    aleloFilhoBebida = []
    aleloFilhoCor = []
    aleloFilhoPet = []
    aleloFilhoNacionalidade= []

    aleloFilhoBebida = cromossomoMae.getBebida()
    aleloFilhoCigarro = cromossomoMae.getCigarro()
    aleloFilhoCor = cromossomoPai.getCor()
    aleloFilhoNacionalidade = cromossomoPai.getNacionalidade()
    aleloFilhoPet = cromossomoPai.getPet()
    segundoFilho = Cromossomo(aleloFilhoNacionalidade, aleloFilhoPet, aleloFilhoCor, aleloFilhoBebida, aleloFilhoCigarro)

   
    return primeiroFilho, segundoFilho
    



