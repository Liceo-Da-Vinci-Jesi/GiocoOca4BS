import csv,time
#calcola tutte le domande presenti nel file "domandeItaliano.csv" e le divide in dizionari
#con chiavi l'argomento principale; i rispettivi valori sono liste con elementi della domanda
#(dovrebbero essere presenti più di una domanda per argomento)
#es: {'Machiavelli': [('Machiavelli', "Dov'Ã¨ nato NiccolÃ² Machiavelli?", 'Jesi', 'Firenze', 'Ancona', 'Roma', 'B'), ('Machiavelli', 'Cosa ha scritto Machiavelli?', 'Gerusalemme Liberata', 'Il Principe', 'Divina Commedia', 'Orlando Furioso', 'B')}
def load():
    file = open("domandeItaliano.csv","r")
    lettore = csv.DictReader(file,delimiter = "/")
    tutteLeDomande = {}
    for riga in lettore:
        #if riga["argomento"] not in self.artistiPresenti:
        #    self.artistiPresenti.append(riga["argomento"])
        #    self.tutteLeDomande[riga["argomento"]] = []
        #if riga["argomento"] in self.artistiPresenti:
        for n in riga:
            if type(riga[n]) != type(None):
                riga[n] = aggiustaCaratteriStrani(riga[n])
        if riga["argomento"] not in tutteLeDomande:
            tutteLeDomande[riga["argomento"]] = []
        if riga["eventualeTesto"] != "" and type(riga["eventualeTesto"]) != type(None):
            riga["eventualeTesto"] = mettiACapo(riga["eventualeTesto"])
        tutteLeDomande[riga["argomento"]].append((riga["argomento"], riga["domanda"], riga["rispostaA"],riga["rispostaB"], riga["rispostaC"],riga["rispostaEsatta"],riga["eventualeTesto"]))
        #print(riga["argomento"])
        #print(tutteLeDomande)
    file.close()

    return tutteLeDomande
def aggiustaCaratteriStrani(testo):
    testo = testo.replace("Ã¹","ù")
    testo = testo.replace("Ã¨","è")
    testo = testo.replace("Ãˆ", "È")
    testo = testo.replace("Ã²", "ò")
    testo = testo.replace("Ã¨", "è")
    testo = testo.replace("â€™", "'")
    testo = testo.replace("Ã¬", "ì")
    testo = testo.replace("Ã", "à")
    testo = testo.replace("Ã©", "é")
    testo = testo.replace("Â°", "°")
    testo = testo.replace("â€¦", "...")
    testo = testo.replace("à©", "é")
    return testo
def mettiACapo(testo):
    testo = testo.replace("000","\n")
    return testo

class ElencoDomande:
    def __init__(self):
        self.listaDomande = load()
        return

if __name__ == "__main__":
    a = ElencoDomande()
