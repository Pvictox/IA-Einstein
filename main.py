import alelo
import populacao
from cromossomo import Cromossomo
import fitness
import operacoes
import random

TAXA_CROSSOVER = 80
TAXA_MUTACAO = 1
TAXA_IMIGRACAO = 10
TAXA_SOBREVIVENCIA = 20
TAM_POP = 4000
NUM_GEN = 2000

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

     prox_pop = []
     
     pais = operacoes.select_parents(population=pop)
     popCrossover = operacoes.crossover(pais=pais, taxa=numFilhos, tamanho=TAM_POP)
     
     prox_pop = popCrossover[:numFilhos]
     popCrossover = []
     
     # while(i < numFilhos//2):
     #      pai, probs = operacoes.roletaCromossomo(population=pop)
     #      #pai = operacoes.selectOne(population=pop)
     #      pop.remove(pai)
     #      operacoes.select_parents(population=pop)
     #      mae, probs = operacoes.roletaCromossomo(population=pop)
     #      #mae = operacoes.selectOne(population=pop)
     #      pop.append(pai)
     #      #pop.remove(mae)
          
     #      filho1, filho2 = operacoes.crossover(cromossomoPai=pai, cromossomoMae=mae)
     #      prox_pop.append(filho1)
     #      prox_pop.append(filho2)
     #      i+=1
     
    
     
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
          prox_pop.append(c)
     
     sobreviventes = []

     # #Imigração
     # #...
     operacoes.imigracao(pop=prox_pop, quantDeImigrantes=(TAXA_IMIGRACAO*TAM_POP)//100, tamanho=TAM_POP ) 
     pop = []
     pop = prox_pop

     # for c in pop:
     #     print("Index: "+str(pop.index(c))+" | Genotipo"+ str(c.getGenotipo())) 
     # print("============================")

# print(" ============= SAIU DAS OPERAÇOS ============= ")
# for c in pop:
#        #print("Index: "+str(pop.index(c))+" | Pontos: "+ str(c.getPontos()))
#        print("Index: "+str(pop.index(c))+" | Genotipo"+ str(c.getGenotipo()))

# print(len(pop))
# pop.sort(key=lambda x:x.getPontos(), reverse=True)

# print("====== Maior pontuacao =======")
# print(pop[0].getPontos())
# print("============ Ordenou ============== ")
# for c in pop:
#        print("Index: "+str(pop.index(c))+" | Pontos: "+ str(c.getPontos()))

#print(len(prox_pop))
