from cromossomo import Cromossomo
from conjEnum.enumNacionalidade import enumNac
from conjEnum.enumCor import enumCor
from conjEnum.enumPet import enumPet
from conjEnum.enumBebida import enumBebida

def calcularFitness(cromossomo):
    # 1) O norueguês vive na primeira casa
    if (enumNac(cromossomo.getNacionalidade()[0]).name == "NORUEGUES"):
        cromossomo.addPonto()
    
    # 2) O inglês vive na casa Vermelha
    for num_Nacionalidade in cromossomo.getNacionalidade():
        if (enumNac(num_Nacionalidade).name == "INGLES"):
            indexDaCasa = cromossomo.getNacionalidade().index(num_Nacionalidade)
            if (enumCor(cromossomo.getCor()[indexDaCasa]).name == "VERMELHA"):
                cromossomo.addPonto()
    
    # 3) O sueco tem cachorros como animais de estimação
    for num_Nacionalidade in cromossomo.getNacionalidade():
        if (enumNac(num_Nacionalidade).name == "SUECO"):
            indexDaCasa = cromossomo.getNacionalidade().index(num_Nacionalidade)
            if (enumPet(cromossomo.getCor()[indexDaCasa]).name == "CACHORROS"):
                cromossomo.addPonto()
    
    # 4) O dinamarquês bebe chá
    for num_Nacionalidade in cromossomo.getNacionalidade():
        if (enumNac(num_Nacionalidade).name == "DINAMARQUES"):
            indexDaCasa = cromossomo.getNacionalidade().index(num_Nacionalidade)
            if (enumBebida(cromossomo.getCor()[indexDaCasa]).name == "CHA"):
                cromossomo.addPonto()
    
    # 5) A casa VERDE fica ao lado esquedo da casa branca
        # Se a casa verde for a de num 5 (indice == 4) indica que não tem como ela ficar a esquerda da branca pq não tem mais casas
        for num_Cor in cromossomo.getCor():
            if (enumCor(num_Cor).name == "VERDE"):
                indexDaCasa = cromossomo.getCor().index(num_Nacionalidade)
                if ( indexDaCasa != 4): #Existe casa a direita
                    if (enumCor(indexDaCasa+1).name == "BRANCA"):
                        cromossomo.addPonto()
                    
    
            
