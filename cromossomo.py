from conjEnum.enumNacionalidade import enumNac
from conjEnum.enumPet import enumPet
from conjEnum.enumBebida import enumBebida
from conjEnum.enumCigarro import enumCigarro
from conjEnum.enumCor import enumCor
class Cromossomo:

    #Nacionalidade
    #Pet
    #Cor da casa
    #bebida
    #cigarro
    def __init__(self, nacionalidade, pet, corCasa, bebida, cigarro):
        self.nacionalidade = nacionalidade
        self.pet = pet
        self.corCasa = corCasa
        self.bebida = bebida
        self.cigarro = cigarro
        self.pontos = 0
    


    

    def getGenotipo(self):
        return "Nacionalidade: "+str(self.nacionalidade)+" | Pet: "+str(self.pet)+" | Cor = "+str(self.corCasa)+" | Bebida = "+str(self.bebida)+" | Cigarro = "+str(self.cigarro)


    def removeConsolacao(self, valor):
        self.pontos = valor
      
      

    def addConsolacao(self):
        self.pontos +=0.5
       
      

    def addPonto(self):
        self.pontos+=1
      
       
    
    def getPontos(self):
        return self.pontos
    
    def getNacionalidade(self):
        return self.nacionalidade
    
    def getCor(self):
        return self.corCasa
    
    def getPet(self):
        return self.pet
    
    def getBebida(self):
        return self.bebida
    
    def getCigarro(self):
        return self.cigarro
        
    def getFenotipo(self):
        #Nacionalidade
        for num in self.nacionalidade:
            if (num != None):
                numCasa = self.nacionalidade.index(num)+1
                print("===================== Casa "+str(numCasa)+" ==================")
                print("Cor: "+enumCor(self.corCasa[numCasa-1]).name)
                print("Nacionalidade: "+enumNac(num).name)
                print("Bebida: "+enumBebida(self.bebida[numCasa-1]).name)
                print("Cigarro: "+enumCigarro(self.cigarro[numCasa-1]).name)
                print("Pet: ", enumPet(self.pet[numCasa-1]).name)
                


        