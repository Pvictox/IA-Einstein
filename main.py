import alelo
import populacao
from cromossomo import Cromossomo
import fitness
import operacoes
import random

TAXA_CROSSOVER = 90
TAXA_MUTACAO = 1
TAXA_IMIGRACAO = 15
TAXA_SOBREVIVENCIA = 10
TAM_POP = 1000
NUM_GEN = 5000

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
     
     quantSobreviventes = (TAM_POP*TAXA_SOBREVIVENCIA)//100
     sobreviventes = operacoes.sobrevivencia(populacao=pop, quantDeSobreviventes=quantSobreviventes)

     # for c in sobreviventes:
     #     print("Pontos: "+str(c.getPontos())+" | Genotipo"+ str(c.getGenotipo())) 
     # print("============================")
     # for c in pop:
     #     print("Index: "+str(pop.index(c))+" | Genotipo"+ str(c.getGenotipo())) 
     # print("============================")
     prox_pop = []
     
     pais = operacoes.select_parents(population=pop)
     popCrossover = operacoes.crossover(pais=pais, taxa=numFilhos, tamanho=TAM_POP)
     
     prox_pop = popCrossover[:numFilhos]
     popCrossover = []
     
     
     
    
     
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

     prox_pop.sort(key=lambda x:x.getPontos(), reverse=True)

     print("GERAÇÃO: "+str(geracao)+" | Melhor fitness: "+str(prox_pop[0].getPontos()))
     # # if (geracao == NUM_GEN):
     # #      print(prox_pop[0].getFenotipo())
    
     # #Sobrevivência
     # #....
     for c in sobreviventes:
          if (prox_pop.count(c) == 0):
               prox_pop.append(c)
     
     sobreviventes = []

     # #Imigração
     # #...
     imig = (TAXA_IMIGRACAO*TAM_POP)//100
     
     imigrantes = operacoes.imigracao(pop=prox_pop, quantDeImigrantes=imig, tamanho=TAM_POP ) 
     pop = []
     pop = prox_pop
     pop.sort(key=lambda x:x.getPontos())
     for i in range(len(imigrantes)):
          pop[i] = imigrantes[i]

     # if (geracao == 50):
     #      for c in pop:
     #           print("Index: "+str(pop.index(c))+" | Genotipo"+ str(c.getGenotipo())) 
     #      print("============================")
     #      geracao = NUM_GEN

