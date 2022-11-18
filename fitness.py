from cromossomo import Cromossomo
from conjEnum.enumNacionalidade import enumNac
from conjEnum.enumCor import enumCor
from conjEnum.enumPet import enumPet
from conjEnum.enumBebida import enumBebida
from conjEnum.enumCigarro import enumCigarro

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
            if (enumPet(cromossomo.getPet()[indexDaCasa]).name == "CACHORROS"):
                cromossomo.addPonto()
    
    # 4) O dinamarquês bebe chá
    for num_Nacionalidade in cromossomo.getNacionalidade():
        if (enumNac(num_Nacionalidade).name == "DINAMARQUES"):
            indexDaCasa = cromossomo.getNacionalidade().index(num_Nacionalidade)
            if (enumBebida(cromossomo.getBebida()[indexDaCasa]).name == "CHA"):
                cromossomo.addPonto()
    
    # 5) A casa VERDE fica ao lado esquedo da casa branca
        # Se a casa verde for a de num 5 (indice == 4) indica que não tem como ela ficar a esquerda da branca pq não tem mais casas
        for num_Cor in cromossomo.getCor():
            if (enumCor(num_Cor).name == "VERDE"):
                indexDaCasa = cromossomo.getCor().index(num_Cor)
                if ( indexDaCasa != 4): #Existe casa a direita
                    if (enumCor(indexDaCasa+1).name == "BRANCA"):
                        cromossomo.addPonto()
    
    # 6) O homem que vive na casa VERDE bebe CAFE
    for numCor in cromossomo.getCor():
        if (enumCor(num_Cor).name == "VERDE"):
            indexDaCasa = cromossomo.getCor().index(num_Cor)
            if (enumBebida(cromossomo.getBebida()[indexDaCasa]).name == "'CAFE"):
                cromossomo.addPonto()
    
    # 7) O homem que fuma PALL_MALL cria PASSAROS
    for num_Cigarro in cromossomo.getCigarro():
        if (enumCigarro(num_Cigarro).name == "PALL_MALL"):
            indexDaCasa = cromossomo.getCigarro().index(num_Cigarro)
            if (enumPet(cromossomo.getPet()[indexDaCasa]).name == "PASSAROS"):
                cromossomo.addPonto()
    
    # 8) O homem que vive na casa AMARELA fuma DUNHILL
    for numCor in cromossomo.getCor():
        if (enumCor(numCor).name == "AMARELA"):
            indexDaCasa = cromossomo.getCor().index(numCor)
            if (enumCigarro(cromossomo.getCigarro()[indexDaCasa]).name == "DUNHILL"):
                cromossomo.addPonto()
    
    # 9) O homem que vive na casa do MEIO bebe LEITE
            # Casa do meio => indice == 2
    if(enumBebida(cromossomo.getBebida()[2]).name == "LEITE"):
        cromossomo.addPonto()
    
    # 10) O homem que fuma BLENDS vive ao lado do que tem GATOS
            # Se indice == 0 não tem como checar a esqueda, se indice == 4 não tem como checar a direita
    for numCigaro in cromossomo.getCigarro():
        if (enumCigarro(num_Cigarro).name == "BLENDS"):
            indexDaCasa = cromossomo.getCigarro().index(num_Cigarro)
            if (indexDaCasa == 0):
                if (enumPet(cromossomo.getPet()[indexDaCasa+1]).name == "GATOS"):
                    cromossomo.addPonto()
            elif(indexDaCasa == 4):
                if (enumPet(cromossomo.getPet()[indexDaCasa-1]).name == "GATOS"):
                    cromossomo.addPonto()
            else:
                if (enumPet(cromossomo.getPet()[indexDaCasa+1]).name == "GATOS" or enumPet(cromossomo.getPet()[indexDaCasa-1]).name == "GATOS"):
                    cromossomo.addPonto()

    # 11) O homem que cria CAVALOS vive ao lado do que fuma Dunhill
            # Mesmo esquema do 10)
    for numPet in cromossomo.getPet():
        if (enumPet(numPet).name == "CAVALOS"):
            indexDaCasa = cromossomo.getPet().index(numPet)
            if (indexDaCasa == 0):
                if (enumCigarro(cromossomo.getCigarro()[indexDaCasa+1]).name == "DUNHILL"):
                    cromossomo.addPonto()
            elif(indexDaCasa == 4):
                if (enumCigarro(cromossomo.getCigarro()[indexDaCasa-1]).name == "DUNHILL"):
                    cromossomo.addPonto()
            else:
                if (enumCigarro(cromossomo.getCigarro()[indexDaCasa+1]).name == "DUNHILL" or enumCigarro(cromossomo.getCigarro()[indexDaCasa-1]).name == "DUNHILL"):
                    cromossomo.addPonto()

    # 12) O homem que fuma BLUEMASTER bebe CERVEJA
    for num_Cigarro in cromossomo.getCigarro():
        if (enumCigarro(num_Cigarro).name == "BLUEMASTER"):
            indexDaCasa = cromossomo.getCigarro().index(num_Cigarro)
            if (enumBebida(cromossomo.getBebida()[indexDaCasa]).name == "CERVEJA"):
                cromossomo.addPonto() 
    
    # 13) O ALEMÃO fuma PRINCE
    for num_Nacionalidade in cromossomo.getNacionalidade():
        if (enumNac(num_Nacionalidade).name == "ALEMAO"):
            indexDaCasa = cromossomo.getNacionalidade().index(num_Nacionalidade)
            if (enumCigarro(cromossomo.getCigarro()[indexDaCasa]).name == "PRINCE"):
                cromossomo.addPonto()

    # 14) O NORUEGUES vive ao lado da casa AZUL
        # Mesma coisa do 10) e do 11)
    for numNaciona in cromossomo.getNacionalidade():
        if (enumNac(numNaciona).name == "NORUEGUES"):
            indexDaCasa = cromossomo.getNacionalidade().index(num_Cigarro)
            if (indexDaCasa == 0):
                if (enumCor(cromossomo.getCor()[indexDaCasa+1]).name == "AZUL"):
                    cromossomo.addPonto()
            elif(indexDaCasa == 4):
                if (enumCor(cromossomo.getCor()[indexDaCasa-1]).name == "AZUL"):
                    cromossomo.addPonto()
            else:
                if (enumCor(cromossomo.getCor()[indexDaCasa+1]).name == "AZUL" or enumCor(cromossomo.getCor()[indexDaCasa-1]).name == "AZUL"):
                    cromossomo.addPonto()                

    # 15) O homem que fuma BLENDS é vizinho do que bebe AGUA
            #Mesma coisa de: O homem que vive ao lado de quem fuma BLENDS bebe AGUA   
    for numCigaro in cromossomo.getCigarro():
        if (enumCigarro(num_Cigarro).name == "BLENDS"):
            indexDaCasa = cromossomo.getCigarro().index(num_Cigarro)
            if (indexDaCasa == 0):
                if (enumBebida(cromossomo.getBebida()[indexDaCasa+1]).name == "AGUA"):
                    cromossomo.addPonto()
            elif(indexDaCasa == 4):
                if (enumBebida(cromossomo.getBebida()[indexDaCasa-1]).name == "AGUA"):
                    cromossomo.addPonto()
            else:
                if (enumBebida(cromossomo.getBebida()[indexDaCasa+1]).name == "AGUA" or enumBebida(cromossomo.getBebida()[indexDaCasa-1]).name == "AGUA"):
                    cromossomo.addPonto()
