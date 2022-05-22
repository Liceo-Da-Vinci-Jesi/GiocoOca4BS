import csv

# ---------------------------------
import os
module_dir = os.path.dirname(__file__)
# ---------------------------------

#calcola tutte le domande presenti nel file "domandeItaliano.csv" e le divide in dizionari
#con chiavi l'argomento principale (tipo di domanda); i rispettivi valori sono liste con tuple di elementi della domanda (tipo/domanda/rispostaA/rispostaB/rispostaC/rispostaEsatta/eventualeTesto)
#es: {luoghiAutobiografici': [('luoghiAutobiografici', 'Quando nacque Giacomo a Recanati?', '29 giugno 1798', '29 giugno 1788', '19 giugno 1798', '29 giugno 1798', ''), ('luoghiAutobiografici', 'Dove si trova palazzo Leopardi?', 'Rione Monte Morello', 'Monte Tabor', 'Porto Recanati', 'Rione Monte Morello', '')]}
def load():
    file = open( os.path.join(module_dir,"domandeItaliano.csv") ,"r")
    lettore = csv.DictReader(file,delimiter = "/")
    tutteLeDomande = {}
    for riga in lettore:
        for n in riga:
            if type(riga[n]) != type(None):
                riga[n] = aggiustaCaratteriStrani(riga[n])
        if riga["argomento"] not in tutteLeDomande:
            tutteLeDomande[riga["argomento"]] = []
        if riga["eventualeTesto"] != "" and type(riga["eventualeTesto"]) != type(None):
            riga["eventualeTesto"] = mettiACapo(riga["eventualeTesto"])
        tutteLeDomande[riga["argomento"]].append((riga["argomento"], riga["domanda"], riga["rispostaA"],riga["rispostaB"], riga["rispostaC"],riga["rispostaEsatta"],riga["eventualeTesto"]))
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
    # 000 è un elemento del testo da sostituire con un banale \n; anzichè 000 andava bene qualsiasi altro carattere/sequenza ben individuabile e che non interferirebbe in qualche modo con il testo
    testo = testo.replace("000","\n")
    return testo

class ElencoDomande:
    def __init__(self):
        self.listaDomande = load()
        return

if __name__ == "__main__":
    a = ElencoDomande()
    print(a.listaDomande)
    for n in a.listaDomande:
        print(n)
    #    for b in a.listaDomande[n]:
    #        print(b,"\n")
