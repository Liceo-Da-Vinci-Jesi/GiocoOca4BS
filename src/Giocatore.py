from PIL import Image

class Giocatore:
    def __init__(self,nome,path):
        self.posizione = 0
        self.nome = nome
        self.iconPath = path
        self.corrette = 0
        self.sbagliate = 0
        
    def __str__(self):
        return "Giocatore "+self.nome+" nella casella "+str(self.posizione)

    def muoviGiocatore(self,x):
        self.posizione += x
        return
