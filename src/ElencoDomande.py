import csv
#calcola tutte le domande presenti nel file "domandeItaliano.csv" e le divide in dizionari
#con chiavi l'argomento principale; i rispettivi valori sono liste con elementi della domanda
#(dovrebbero essere presenti più di una domanda per argomento)
#es: {'Machiavelli': [('Machiavelli', "Dov'Ã¨ nato NiccolÃ² Machiavelli?", 'Jesi', 'Firenze', 'Ancona', 'Roma', 'B'), ('Machiavelli', 'Cosa ha scritto Machiavelli?', 'Gerusalemme Liberata', 'Il Principe', 'Divina Commedia', 'Orlando Furioso', 'B')}
def load():
    file = open("domandeItaliano.csv","r")
    lettore = csv.DictReader(file)
    tutteLeDomande = {}
    for riga in lettore:
        #if riga["argomento"] not in self.artistiPresenti:
        #    self.artistiPresenti.append(riga["argomento"])
        #    self.tutteLeDomande[riga["argomento"]] = []
        #if riga["argomento"] in self.artistiPresenti:
        if riga["argomento"] not in tutteLeDomande:
            tutteLeDomande[riga["argomento"]] = []
        tutteLeDomande[riga["argomento"]].append((riga["argomento"], riga["domanda"], riga["rispostaA"],riga["rispostaB"], riga["rispostaC"], riga["rispostaD"],riga["rispostaEsatta"]))
        #print(riga["argomento"])
        #print(tutteLeDomande)
    file.close()
    return tutteLeDomande


class ElencoDomande:
    def __init__(self):
        self.listaDomande = load()
        return
