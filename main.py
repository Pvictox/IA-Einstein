import alelo
import populacao
from cromossomo import Cromossomo
import fitness
import operacoes



popCromossomos = populacao.criarPopulacao(4)
for c in popCromossomos:
    fitness.calcularFitness(c)

for c in popCromossomos:
    print("Index: "+str(popCromossomos.index(c))+" | Pontos: "+str(c.getPontos()))


#Lógica da roleta -> Quando eu selecionar o pai eu removo ele da população para evitar que ele seja selecionado novamente. Depois do processo de escolha eu adiciono ele na pop dnovo
cPai,probs = operacoes.roletaCromossomo(population=popCromossomos)
print(probs)
popCromossomos.remove(cPai)
cMae,probs = operacoes.roletaCromossomo(population=popCromossomos)
print(probs)

popCromossomos.append(cPai)

print("Gen: "+str(cPai.getGenotipo())+"|| Pontos: "+str(cPai.getPontos()))
print("Gen: "+str(cMae.getGenotipo())+"|| Pontos "+str(cMae.getPontos()))


print(" ============================== ")
for c in popCromossomos:
    print("Index: "+str(popCromossomos.index(c))+" | Pontos: "+str(c.getPontos())+" | Aptidao: "+str(c.getAptidao()))

#operacoes.mutacao(popCromossomos[0])
# fitness.calcularFitness(cromossomo=popCromossomos[0])
# print(popCromossomos[0].getPontos())

# for cromossomo in popCromossomos:
#     print(cromossomo.getGenotipo())
#     print(cromossomo.getFenotipo())

# cro = Cromossomo(nacionalidade=[1,2,3,4,5],pet=[], corCasa=[], bebida=[], cigarro=[])
# fitness.calcularFitness(cromossomo=cro)
# print(cro.getPontos())