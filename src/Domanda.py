import wx,random
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
    def __init__(self,Domanda,giocatore):
        super().__init__(None, title="Domanda - "+giocatore.nome)
        panel = wx.Panel(self)
        self.rispostaEsatta = Domanda.rispostaEsatta
        risposte = [Domanda.rispostaA, Domanda.rispostaB, Domanda.rispostaC]
        random.shuffle(risposte)
        for n in risposte:
            if n == self.rispostaEsatta:
                self.IdCorretto = risposte.index(n) + 1
        self.PulsanteA = wx.Button(panel, label="A: " + risposte[0], id=1)
        self.PulsanteB = wx.Button(panel, label="B: " + risposte[1], id=2)
        self.PulsanteC = wx.Button(panel, label="C: " + risposte[2], id=3)
        if Domanda.testo != "":
            #crea questo tipo di finestra se la domanda necessita di uno spazio apposito dove riportare una parte di testo
            box = wx.BoxSizer(wx.HORIZONTAL)
            textCtrl = wx.TextCtrl(panel,style = wx.TE_MULTILINE|wx.TE_READONLY)
            textCtrl.SetValue(Domanda.testo)
            box.Add(textCtrl,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 10)
            vboxDestra = wx.BoxSizer(wx.VERTICAL)
            testoDomanda = wx.StaticText(panel,style = wx.TE_CENTRE)
            partiDomanda = Domanda.domanda.split()
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
            hTesto.Add(testo,proportion = 1,flag = wx.ALL,border = 5)
            box.Add(hTesto,proportion = 1,flag = wx.ALL|wx.ALIGN_CENTER,border = 5)
            hPulsanti = wx.BoxSizer(wx.HORIZONTAL)
            hPulsanti.Add(self.PulsanteA,proportion = 1,flag = wx.ALL,border = 5)
            hPulsanti.Add(self.PulsanteB,proportion = 1,flag = wx.ALL,border = 5)
            hPulsanti.Add(self.PulsanteC,proportion = 1,flag = wx.ALL,border = 5)
            box.Add(hPulsanti,proportion = 0,flag = wx.ALL|wx.EXPAND,border = 5)
        #self.PulsanteA.Bind(wx.EVT_BUTTON, self.esitoRisposta)
        #self.PulsanteB.Bind(wx.EVT_BUTTON, self.esitoRisposta)
        #self.PulsanteC.Bind(wx.EVT_BUTTON, self.esitoRisposta)
        self.listaPulsanti = (self.PulsanteA, self.PulsanteB, self.PulsanteC)
        panel.SetSizer(box)
        box.Fit(self)
        self.timer = wx.Timer(self)
        #adatta al meglio le dimensioni della finestra in base alla domanda
        dimensioni = self.GetSize()
        if dimensioni[0] <= 423:
            self.SetMaxSize((423, dimensioni[1]))
            self.SetMinSize((423,dimensioni[1]))
            self.SetSize((423,dimensioni[1]))
        else:
            self.SetMaxSize(dimensioni)
            self.SetMinSize(dimensioni)
            self.SetSize(dimensioni)
        dimensioni = self.GetSize()
        if dimensioni[1] <= 125:
            self.SetMaxSize((dimensioni[0], 125))
            self.SetMinSize((dimensioni[0],125))
            self.SetSize((dimensioni[0],125))
        else:
            self.SetMaxSize(dimensioni)
            self.SetMinSize(dimensioni)
            self.SetSize(dimensioni)
        self.Refresh()
        self.Hide()
        self.Show()
        self.Bind(wx.EVT_CLOSE,self.nonChiudi)
        self.Centre()
        
    def esitoRisposta(self,ID):
        if ID == self.IdCorretto:
            #print("corretto")
            return True
        return False
    
    def nonChiudi(self,event):
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
    domandaDaFare = scegliDomandaDaFare("luoghiAutobiografici",domande)
    window = FinestraDomanda(domandaDaFare,player)
    window.Show()
    app.MainLoop()