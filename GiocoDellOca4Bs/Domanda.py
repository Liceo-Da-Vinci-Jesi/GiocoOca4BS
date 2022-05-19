import wx,random, wx.adv
import Giocatore


class Domanda:
    def __init__(self,argomento,domanda = "",rispostaA = "",rispostaB = "",rispostaC = "",rispostaEsatta = "",testo = ""):
        self.argomento = argomento
        self.domanda = domanda
        self.rispostaA = rispostaA
        self.rispostaB = rispostaB
        self.rispostaC = rispostaC
        self.rispostaEsatta = rispostaEsatta
        self.testo = testo
    def __str__(self):
        return self.argomento + self.domanda + self.rispostaA + self.rispostaB + self.rispostaC + self.rispostaEsatta + self.testo

class FinestraDomanda(wx.Frame):
    def __init__(self,Domanda,giocatore,tipo):
        super().__init__(None, title="Domanda - "+giocatore.nome + " - " + tipo)
        panel = wx.Panel(self)
        self.suonoChiusura = wx.adv.Sound()
        font13Norm = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        font10Norm = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.rispostaEsatta = Domanda.rispostaEsatta
        risposte = [Domanda.rispostaA, Domanda.rispostaB, Domanda.rispostaC]
        random.shuffle(risposte)
        #attraverso il random mischio la sequenza delle risposte
        #mi salvo però l'id del pulsante che contiene quella esatta
        for n in risposte:
            if n == self.rispostaEsatta:
                self.IdCorretto = risposte.index(n) + 1
        self.PulsanteA = wx.Button(panel, label="A: " + risposte[0], id=1)
        self.PulsanteB = wx.Button(panel, label="B: " + risposte[1], id=2)
        self.PulsanteC = wx.Button(panel, label="C: " + risposte[2], id=3)
        self.listaPulsanti = (self.PulsanteA, self.PulsanteB, self.PulsanteC)
        if Domanda.testo != "":
            #crea questo tipo di finestra se la domanda necessita di uno spazio apposito dove riportare una parte di testo
            box = wx.BoxSizer(wx.HORIZONTAL)
            textCtrl = wx.TextCtrl(panel,style = wx.TE_MULTILINE|wx.TE_READONLY)
            textCtrl.SetValue(Domanda.testo)
            textCtrl.SetFont(font10Norm)
            box.Add(textCtrl,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 10)
            vboxDestra = wx.BoxSizer(wx.VERTICAL)
            testoDomanda = wx.StaticText(panel,style = wx.TE_CENTRE)
            partiDomanda = Domanda.domanda.split()
            #per essere sicuri che la domanda non risulti molto larga, ogni 60 caratteri va a capo
            label = ""
            conta = ""
            for n in partiDomanda:
                if len(conta+n) <= 60:
                    label+= " " + n
                    conta+= " " + n
                else:
                    conta = n
                    label+= "\n"
                    label+=n
            testoDomanda.SetLabel(label)
            testoDomanda.SetFont(font13Norm)
            vboxDestra.Add(testoDomanda,proportion = 1 ,flag = wx.ALIGN_CENTER|wx.ALL,border = 5)
            box.Add(vboxDestra,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
            vboxDestra.Add(self.PulsanteA,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
            vboxDestra.Add(self.PulsanteB,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
            vboxDestra.Add(self.PulsanteC,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
        else:
            #crea questo tipo di finestra se la domanda non necessita di uno spazio apposito dove riportare una parte di testo
            box = wx.BoxSizer(wx.VERTICAL)
            hTesto = wx.BoxSizer(wx.HORIZONTAL)
            testo = wx.StaticText(panel,label = Domanda.domanda)
            testo.SetFont(font13Norm)
            hTesto.Add(testo,proportion = 1,flag = wx.ALL,border = 5)
            box.Add(hTesto,proportion = 1,flag = wx.ALL|wx.ALIGN_CENTER,border = 5)
            hPulsanti = wx.BoxSizer(wx.HORIZONTAL)
            hPulsanti.Add(self.PulsanteA,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
            hPulsanti.Add(self.PulsanteB,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
            hPulsanti.Add(self.PulsanteC,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
            box.Add(hPulsanti,proportion = 0,flag = wx.ALL|wx.EXPAND,border = 5)
        #controllo che anche i label dei pulsanti non siano composto da righe di testo troppo lunghe
        for puls in self.listaPulsanti:
            label = ""
            conta = ""
            for n in puls.GetLabel().split():
                if len(conta + n) <= 35:
                    label += " " + n
                    conta += " " + n
                else:
                    conta = n
                    label += "\n"
                    label += n
            puls.SetLabel(label)
            puls.SetFont(font10Norm)

        n = ("operette","canti","poeticaDeiPaesaggi","luoghiAutobiografici")
        c = ((249,194,68),(241,105,99),(73,154,200),(66,215,132))
        #imposto il colore dello sfondo in base alla tipologia di Casella in cui mi trovo
        panel.SetBackgroundColour(c[n.index(tipo)])

        panel.SetSizer(box)
        #adatta al meglio le dimensioni della finestra in base alla domanda
        box.Fit(self)
        dim = self.GetSize()
        self.SetMinSize(dim)
        self.SetMaxSize((dim[0]+150,dim[1]+100))
        self.timer = wx.Timer(self)
        self.Hide()
        self.Show()
        #la finestra non si deve chiudere e produrra un suono
        self.Bind(wx.EVT_CLOSE,self.nonChiudi)
        self.Centre()
        self.SetIcon(wx.Icon("icone/iconaInfinito.ico"))
        
    def esitoRisposta(self,ID):
        if ID == self.IdCorretto:
            #print("corretto")
            return True
        return False

    def nonChiudi(self,event):
        self.suonoChiusura.Play()
        return

def scegliDomandaDaFare(tipologia,lista):
    possibili = []
    for n in lista:
        if n == tipologia:
            possibili.append(lista[n])
            break
    domanda = random.choice(possibili[0])
    #DA RIMUOVERE # SE NUMERO DI DOMANDE SUFFICIENTI
    lista[n].remove(domanda)
    return Domanda(domanda[0],domanda[1],domanda[2],domanda[3],domanda[4],domanda[5],domanda[6])

if __name__ == "__main__":
    import ElencoDomande
    domande = ElencoDomande.ElencoDomande().listaDomande
    app = wx.App()
    player = Giocatore.Giocatore("Io","a")
    domandaDaFare = scegliDomandaDaFare("poeticaDeiPaesaggi",domande)
    window = FinestraDomanda(domandaDaFare,player,"poeticaDeiPaesaggi")
    window.Show()
    app.MainLoop()