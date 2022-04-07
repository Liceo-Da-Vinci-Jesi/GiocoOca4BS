import wx,random

class Domanda:
    def __init__(self,argomento,domanda = "",rispostaA = "",rispostaB = "",rispostaC = "",rispostaD = "",rispostaEsatta = ""):
        self.argomento = argomento
        self.domanda = domanda
        self.rispostaA = rispostaA
        self.rispostaB = rispostaB
        self.rispostaC = rispostaC
        self.rispostaD = rispostaD
        self.rispostaEsatta = rispostaEsatta
    def __str__(self):
        return self.argomento + self.domanda + self.rispostaA + self.rispostaB + self.rispostaC + self.rispostaD + self.rispostaEsatta

class FinestraDomanda(wx.Frame):
    def __init__(self,Domanda):
        super().__init__(None, title="Domanda")
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.rispostaEsatta = Domanda.rispostaEsatta
        hTesto = wx.BoxSizer(wx.HORIZONTAL)
        testo = wx.StaticText(panel,label = Domanda.domanda)
        hTesto.Add(testo,proportion = 1,flag = wx.ALL,border = 5)
        vbox.Add(hTesto,proportion = 1,flag = wx.ALL|wx.ALIGN_CENTER,border = 5)
        hPulsanti = wx.BoxSizer(wx.HORIZONTAL)
        self.PulsanteA = wx.Button(panel,label = "A: " + Domanda.rispostaA,id = 1)
        self.PulsanteB = wx.Button(panel, label="B: " + Domanda.rispostaB,id = 2)
        self.PulsanteC = wx.Button(panel, label="C: " + Domanda.rispostaC,id = 3)
        self.PulsanteD = wx.Button(panel, label="D: " + Domanda.rispostaD,id = 4)
        self.PulsanteA.Bind(wx.EVT_BUTTON,self.Risposto)
        self.PulsanteB.Bind(wx.EVT_BUTTON,self.Risposto)
        self.PulsanteC.Bind(wx.EVT_BUTTON,self.Risposto)
        self.PulsanteD.Bind(wx.EVT_BUTTON,self.Risposto)
        self.listaPulsanti = (self.PulsanteA,self.PulsanteB,self.PulsanteC,self.PulsanteD)
        hPulsanti.Add(self.PulsanteA,proportion = 1,flag = wx.ALL,border = 5)
        hPulsanti.Add(self.PulsanteB,proportion = 1,flag = wx.ALL,border = 5)
        hPulsanti.Add(self.PulsanteC,proportion = 1,flag = wx.ALL,border = 5)
        hPulsanti.Add(self.PulsanteD,proportion = 1,flag = wx.ALL,border = 5)
        vbox.Add(hPulsanti,proportion = 0,flag = wx.ALL|wx.EXPAND,border = 5)
        panel.SetSizer(vbox)
        vbox.Fit(self)
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
        self.Bind(wx.EVT_ICONIZE,self.nonIconizzare)


    def nonIconizzare(self,event):
        self.Iconize(False)
        return
    def nonChiudi(self,event):
        return
    def Risposto(self,event):
        ID = event.GetId()
        if self.listaPulsanti[ID-1].GetLabel()[0] == self.rispostaEsatta:
            self.valore = True
        else:
            self.valore = False
        self.Destroy()
        return


#
def scegliDomandaDaFare(tipologia,lista):
    #print(lista)
    possibili = []
    for n in lista:
        if n == tipologia:
            #print(lista[n])
            possibili.append(lista[n])
            break
        #print("N")
    domanda = random.choice(possibili[0])
    #DA RIMUOVERE # SE NUMERO DI DOMANDE SUFFICIENTI
    #lista[n].remove(domanda)
    #print(lista)
    return Domanda(domanda[0],domanda[1],domanda[2],domanda[3],domanda[4],domanda[5],domanda[6])

if __name__ == "__main__":
    import ElencoDomande
    domande = ElencoDomande.ElencoDomande().listaDomande
    app = wx.App()
    domandaDaFare = domande["Machiavelli"][0]
    window = FinestraDomanda(domandaDaFare)
    window.Show()
    app.MainLoop()