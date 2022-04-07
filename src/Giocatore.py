class Giocatore:
    def __init__(self,nome):
        self.posizione = 1
        self.nome = nome
        self.icona = ""

    def __str__(self):
        return "Giocatore "+self.nome+" nella casella "+str(self.posizione)

    def muoviGiocatore(self,x):
        self.posizione+=x
        return