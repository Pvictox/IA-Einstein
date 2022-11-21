from cromossomo import Cromossomo
import random
import numpy.random as npr
import fitness
import populacao
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
    pos_caracteristica_1 = random.randint(0,4) #0
    pos_caracteristica_2 = random.randint(0,4) # 3
    while (pos_caracteristica_2 == pos_caracteristica_1):
        pos_caracteristica_2 = random.randint(0,4)
    
    carac1 = lista[pos_caracteristica_1]
    carac2 = lista[pos_caracteristica_2]

    lista[pos_caracteristica_1] = carac2
    lista[pos_caracteristica_2] = carac1

        


def swapAntecessor(lista, posicao):
    aux = lista[posicao-1] 
    lista[posicao-1] = lista[posicao]
    lista[posicao] = aux 

def swapSucessor(lista, posicao):
    aux = lista[posicao+1] 
    lista[posicao+1] = lista[posicao]
    lista[posicao] = aux 



def select_parents(population):
    fitness_values = []
    for c in population:
        fitness_values.append(c.getPontos())
    parents = []
    total = sum(fitness_values)
    norm_fitness_values = [x/total for x in fitness_values]

    #find cumulative fitness values for roulette wheel selection
    cumulative_fitness = []
    start = 0
    for norm_value in norm_fitness_values:
        start+=norm_value
        cumulative_fitness.append(start)

    population_size = len(population)
    for count in range(population_size+1):
        random_number = random.uniform(0, 1)
        individual_number = 0
        for score in cumulative_fitness:
            if(random_number<=score):
                parents.append(population[individual_number])
                break
            individual_number+=1
    return parents




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
# def crossover(cromossomoPai, cromossomoMae):
#     aleloFilhoCigarro = []
#     aleloFilhoBebida = []
#     aleloFilhoCor = []
#     aleloFilhoPet = []
#     aleloFilhoNacionalidade= []
    


#     aleloFilhoBebida = cromossomoPai.getBebida()
#     aleloFilhoCigarro = cromossomoPai.getCigarro()
#     aleloFilhoCor = cromossomoMae.getCor()
#     aleloFilhoNacionalidade = cromossomoMae.getNacionalidade()
#     aleloFilhoPet = cromossomoMae.getPet()
    

#     primeiroFilho = Cromossomo(aleloFilhoNacionalidade, aleloFilhoPet, aleloFilhoCor, aleloFilhoBebida, aleloFilhoCigarro)

#     aleloFilhoCigarro = []
#     aleloFilhoBebida = []
#     aleloFilhoCor = []
#     aleloFilhoPet = []
#     aleloFilhoNacionalidade= []

#     aleloFilhoBebida = cromossomoMae.getBebida()
#     aleloFilhoCigarro = cromossomoMae.getCigarro()
#     aleloFilhoCor = cromossomoPai.getCor()
#     aleloFilhoNacionalidade = cromossomoPai.getNacionalidade()
#     aleloFilhoPet = cromossomoPai.getPet()
#     segundoFilho = Cromossomo(aleloFilhoNacionalidade, aleloFilhoPet, aleloFilhoCor, aleloFilhoBebida, aleloFilhoCigarro)

   
#     return primeiroFilho, segundoFilho


def aplicaCaracteristicas(filho, pai, mae, quantPai, quantMae):
    aleloNacionalidade = []
    aleloPet = []
    aleloCor = []
    aleloBebida = []
    aleloCigarro = []
    while (quantPai != 0):
        chance = random.randint(0,100)
        if (chance <=20 and len(aleloNacionalidade) == 0):
            aleloNacionalidade = pai.getNacionalidade()
            quantPai-=1
        elif((chance>20 and chance<=40) and len(aleloPet) == 0):
            aleloPet = pai.getPet()
            quantPai-=1
        elif((chance>40 and chance<=60) and len(aleloCor) == 0):
            aleloCor = pai.getCor()
            quantPai-=1
        elif((chance>60 and chance<=80) and len(aleloBebida) == 0):
            aleloBebida = pai.getBebida()
            quantPai-=1
        elif (len(aleloCigarro) == 0):
            aleloCigarro = pai.getCigarro()
            quantPai-=1
    
    while (quantMae != 0):
        chance = random.randint(0,100)
        if (chance <=20 and len(aleloNacionalidade) == 0):
            aleloNacionalidade = mae.getNacionalidade()
            quantMae-=1
        elif((chance>20 and chance<=40) and len(aleloPet) == 0):
            aleloPet = mae.getPet()
            quantMae-=1
        elif((chance>40 and chance<=60) and len(aleloCor) == 0):
            aleloCor = mae.getCor()
            quantMae-=1
        elif((chance>60 and chance<=80) and len(aleloBebida) == 0):
            aleloBebida = mae.getBebida()
            quantMae-=1
        elif (len(aleloCigarro) == 0):
            aleloCigarro = mae.getCigarro()
            quantMae-=1
    
    cromossomo_filho = Cromossomo(nacionalidade=aleloNacionalidade, pet=aleloPet, corCasa=aleloCor, bebida=aleloBebida, cigarro=aleloCigarro)
    return cromossomo_filho    
        


def crossover(pais, taxa, tamanho):
    random.shuffle(pais)
    numeros_pares = round(taxa/2)
    populacao_crossover = []
    flag = False
    for par in range(numeros_pares):
       
            tamanho = len(pais)
            indice_pai = random.randrange(tamanho)
            indice_mae = random.randrange(tamanho)
            while (indice_mae == indice_pai):
                indice_mae = random.randrange(tamanho)
            
            pai = pais[indice_pai]
            mae = pais[indice_mae]
            primeiroFilho = None
            segundoFilho = None
            if (pai.getSobrevivente != True and mae.getSobrevivente != True):
                primeiroFilho = aplicaCaracteristicas(primeiroFilho, pai=pai, mae=mae, quantPai=3, quantMae=2)
                segundoFilho = aplicaCaracteristicas(segundoFilho, pai=pai, mae=mae, quantPai=2, quantMae=3)
                
                populacao_crossover.append(primeiroFilho)
                
                populacao_crossover.append(segundoFilho)
                
                pais.remove(pai)
                pais.remove(mae)
             
        
    if (len(pais) > 0):
        for pai in pais:
            populacao_crossover.append(pai)
    
    return populacao_crossover

def imigracao(pop, quantDeImigrantes, tamanho):
    imigrantes = populacao.criarPopulacao(quantDeImigrantes-1)
    return imigrantes
    
    
    
    
    
    
    

# def imigracao(population,taxaImagracao):
#     sorted(population, key=lambda elm: elm.getPontos())
#     qtd_imigricao=int((len(population)*taxaImagracao)/100)
#     population=population[qtd_imigricao:]
#     pop =populacao.criarPopulacao(qtd_imigricao)
#     population+=pop
#     return population



def sobrevivencia(populacao, quantDeSobreviventes):
    populacao.sort(key=lambda x:x.getPontos(), reverse=True)
    sobreviventes = []
    for i in range(quantDeSobreviventes):
        if (sobreviventes.count(populacao[i]) == 0):
            populacao[i].setSobrevivente(True)
            sobreviventes.append(populacao[i])
    #sobreviventes = populacao[:quantDeSobreviventes]
    return sobreviventes

# def sobrevivencia(population,taxaSob):
#     sorted(population, key=lambda elm: elm.getPontos())
#     qtd_sobrivencia=int((len(population)*taxaSob)/100)
#     print("Qaunt sobrevivencia: ", qtd_sobrivencia)
#     sobrivivente=population[-qtd_sobrivencia:]
#     #population+=sobrivivente
#     return sobrivivente

def criarPop(pop,tamPop):
    pop = populacao.criarPopulacao(tamPop)
    for cromossomo in pop:
        cromossomo = fitness.calcularFitness(cromossomo= cromossomo)
    return pop




