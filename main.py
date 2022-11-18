import alelo
import populacao
from cromossomo import Cromossomo
import fitness
popCromossomos = populacao.criarPopulacao(1)
fitness.calcularFitness(cromossomo=popCromossomos[0])
print(popCromossomos[0].getPontos())
# for cromossomo in popCromossomos:
#     print(cromossomo.getGenotipo())
#     print(cromossomo.getFenotipo())

# cro = Cromossomo(nacionalidade=[1,2,3,4,5],pet=[], corCasa=[], bebida=[], cigarro=[])
# fitness.calcularFitness(cromossomo=cro)
# print(cro.getPontos())