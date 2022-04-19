class Giocatore:
    def __init__(self,nome,icon):
        self.posizione = 0
        self.nome = nome
        self.icona75 = icon.resize((75,75))
        self.icona50 = icon.resize((50, 50))
        self.icona24 = icon.resize((24,24))
        self.corrette = 0
        self.sbagliate = 0
    def __str__(self):
        return "Giocatore "+self.nome+" nella casella "+str(self.posizione)

    def muoviGiocatore(self,x):
        self.posizione+=x
        return