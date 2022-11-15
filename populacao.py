from cromossomo import Cromossomo
import alelo
def criarPopulacao(numIndividuos):
    listCromossomos = []
    while (len(listCromossomos) < numIndividuos):
        listNacionalidade = []
        listCor = []
        listPet = []
        listBebida = []
        listCigarro = []
        listNacionalidade = alelo.criarAlelo(listaX=listNacionalidade)
        listPet = alelo.criarAlelo(listaX=listPet)
        listCor = alelo.criarAlelo(listaX=listCor)
        listBebida = alelo.criarAlelo(listaX=listBebida)
        listCigarro = alelo.criarAlelo(listaX=listCigarro)
        c1 = Cromossomo(listNacionalidade, listPet, listCor, listBebida, listCigarro)
        listCromossomos.append(c1)
        

    return listCromossomos

