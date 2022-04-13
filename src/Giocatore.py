class Giocatore:
    def __init__(self,nome,icon):
        self.posizione = 0
        self.nome = nome
        self.icona = icon

    def __str__(self):
        return "Giocatore "+self.nome+" nella casella "+str(self.posizione)

    def muoviGiocatore(self,x):
        self.posizione+=x
        return