import alelo
import populacao
from cromossomo import Cromossomo
import fitness
import operacoes
import random

TAXA_CROSSOVER = 90
TAXA_MUTACAO = 1
TAXA_IMIGRACAO = 3
TAXA_SOBREVIVENCIA = 6
TAM_POP = 100
NUM_GEN = 1

prox_pop = []

geracao = 0
pop = populacao.criarPopulacao(TAM_POP)
for cromossomo in pop:
     cromossomo = fitness.calcularFitness(cromossomo= cromossomo)


while (geracao < NUM_GEN):
     geracao+=1

     #Crossover Metodo
     numFilhos = (TAM_POP*TAXA_CROSSOVER)//100
     i =0


     while(i < numFilhos//2):
          
          pai, probs = operacoes.roletaCromossomo(population=pop)
          pop.remove(pai)
          mae, probs = operacoes.roletaCromossomo(population=pop)
          pop.append(pai)
          filho1, filho2 = operacoes.crossover(cromossomoPai=pai, cromossomoMae=mae)
          prox_pop.append(filho1)
          if (i != numFilhos-1):
               prox_pop.append(filho2)
          i+=1

     #Mutacao
     numMutados = (TAM_POP*TAXA_MUTACAO)/100
     i=0
     while (i < numMutados):
          indiceCromossomo = random.randint(0,len(prox_pop)-1)
          operacoes.mutacao(prox_pop[indiceCromossomo])
          i+=1
     
     #Avaliação
     for cromossomo in prox_pop:
          cromossomo_avaliado = fitness.calcularFitness(cromossomo=cromossomo)
          if (cromossomo_avaliado != None):
               print("***** RESPOSTA ENCONTRADA *****")
               print("Geração: ", geracao)
               print("Genótipo: ", cromossomo_avaliado.getGenotipo())
               print("Fenótipo: ", cromossomo_avaliado.getFenotipo())
               exit()
     
     #Sobrevivência
     #....


     #Imigração
     #...
     

     
#print(len(prox_pop))