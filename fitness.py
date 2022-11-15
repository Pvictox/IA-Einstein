from cromossomo import Cromossomo
from conjEnum.enumNacionalidade import enumNac
from conjEnum.enumCor import enumCor
from conjEnum.enumPet import enumPet

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
    
    
            
