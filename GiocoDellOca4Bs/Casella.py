# classe Casella

class Casella:
    def __init__(self,numero,tipologia):
        self.numero=numero
        self.tipo=tipologia
        return

    def __str__(self):
        return "casella: " + str(self.numero) + ". Tipologia = " + self.tipologia
