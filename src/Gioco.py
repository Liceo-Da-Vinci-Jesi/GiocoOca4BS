import Domanda, wx,random , time , Lobby , Casella, Giocatore, CampoDaGioco, ElencoDomande

class Gioco:
    def __init__(self):
        self.listaTipoCaselle = []
        self.creaTipoCaselle()
        print(self.listaTipoCaselle[1].tipo)
        self.turnoGiocatore = ""
        self.listaDomande = ElencoDomande.ElencoDomande().listaDomande
        self.listaGiocatori = 0
        self.pulsanteGioca = ""
        self.FinestraLobby = Lobby.Lobby()
        self.FinestraLobby.Show()
        self.FinestraLobby.PIniziaPartita.Bind(wx.EVT_BUTTON,self.IniziaPartita)
        #tabellone = classe Campo da Gioco
        self.tabellone = CampoDaGioco.CampoDaGioco()
        self.tabellone.Hide()
        self.tabellone.PGiocaTurno.Bind(wx.EVT_BUTTON, self.GiocaTurnoDi)
        self.tabellone.PGiocaTurno.Disable()
        self.attesaDomanda = False
        self.tabellone.Bind(wx.EVT_CLOSE,self.chiudiGioco)
        return

    def chiudiGioco(self,event):
        quit()
        return

    def IniziaPartita(self,evt):
        giocatori = []
        for n in self.FinestraLobby.listaToggleButton:
            if n.GetValue():
                giocatori.append(Giocatore.Giocatore((self.FinestraLobby.listaTc[n.GetId()-1]).GetValue()))
        self.FinestraLobby.Destroy()
        self.listaGiocatori = giocatori
        random.shuffle(self.listaGiocatori)
        self.turnoGiocatore = self.listaGiocatori[0]
        self.tabellone.testoTurno.SetLabel(self.turnoGiocatore.nome)
        self.tabellone.Show()
        self.tabellone.PGiocaTurno.Enable()
        #per non far vedere il testo del dado
        #print(self.tabellone.testoTurno.GetBackgroundColour())
        self.tabellone.testoLancioDado.SetOwnForegroundColour((240, 240, 240))
        self.tabellone.testoDado.SetOwnForegroundColour((240,240,240))
        self.AggiornaInformazioni()
        #print(self.listaGiocatori)
        #print(self.turnoGiocatore)
        return

    def AggiornaTurno(self):
        self.tabellone.testoLancioDado.SetLabel("")
        giocatori = self.listaGiocatori
        turnoDi = self.turnoGiocatore
        #ix = index
        ix = giocatori.index(turnoDi)
        if (ix + 2) > len(giocatori):
            self.turnoGiocatore = giocatori[0]
        else:
            self.turnoGiocatore = giocatori[ix+1]
        self.tabellone.testoTurno.SetLabel(self.turnoGiocatore.nome)
        self.tabellone.PGiocaTurno.Enable()
        return

    def GiocaTurnoDi(self,event):
        if not self.attesaDomanda:
            dado = self.tiraDado()
            self.tabellone.testoDado.SetLabel(str(dado))
            for n in range(dado):
                if self.listaGiocatori[self.listaGiocatori.index(self.turnoGiocatore)].posizione + 1 > 42:
                    print(self.turnoGiocatore.nome," HAI VINTO!!!")
                    quit()
                else:
                    self.listaGiocatori[self.listaGiocatori.index(self.turnoGiocatore)].muoviGiocatore(1)
                    self.AggiornaInformazioni()
                    time.sleep(0.5)
            #print(self.listaGiocatori[self.listaGiocatori.index(self.turnoGiocatore)])
            #print(self.listaGiocatori[self.listaGiocatori.index(self.turnoGiocatore)])
            time.sleep(1)
            if self.listaTipoCaselle[self.turnoGiocatore.posizione-1].tipo == "":
                self.tabellone.testoDado.Hide()
                self.AggiornaTurno()
                return
            if self.listaTipoCaselle[self.turnoGiocatore.posizione-1].tipo == "jolly":
                return
            ############### Apertura finestra domanda
            self.tabellone.PGiocaTurno.Disable()
            self.attesaDomanda = True
            domanda = Domanda.scegliDomandaDaFare(self.listaTipoCaselle[self.turnoGiocatore.posizione-1].tipo,self.listaDomande)
            self.finestraDomanda = Domanda.FinestraDomanda(domanda,self.turnoGiocatore)
            self.finestraDomanda.Show()
            self.finestraDomanda.PulsanteA.Bind(wx.EVT_BUTTON, self.Risposto)
            self.finestraDomanda.PulsanteB.Bind(wx.EVT_BUTTON, self.Risposto)
            self.finestraDomanda.PulsanteC.Bind(wx.EVT_BUTTON, self.Risposto)
            return
        return
    def Risposto(self,event):
        self.tabellone.PGiocaTurno.Enable()
        self.attesaDomanda = False
        ID = event.GetId()
        #if self.finestraDomanda.listaPulsanti[ID - 1].GetLabel()[0] == self.finestraDomanda.rispostaEsatta:
        if self.finestraDomanda.esitoRisposta(ID):
            #print("ESATTO")
            self.finestraDomanda.Destroy()
        else:
            self.finestraDomanda.Destroy()
            self.tabellone.testoDado.Hide()
            self.AggiornaTurno()

        return
    def tiraDado(self):
        self.tabellone.testoLancioDado.SetOwnForegroundColour((0, 0, 0))
        self.tabellone.testoDado.SetOwnForegroundColour((0,0,0))
        self.tabellone.testoDado.Show()
        self.tabellone.testoLancioDado.Show()
        self.tabellone.testoLancioDado.SetLabel("Lancio del\ndado")
        for n in range(3):
            self.tabellone.testoLancioDado.SetLabel(self.tabellone.testoLancioDado.GetLabel()+".")
            self.tabellone.testoDado.SetLabel(str(random.randint(1,6)))
            time.sleep(0.5)
        uscito = random.randint(1,6)
        self.tabellone.testoDado.SetLabel(str(uscito))
        self.tabellone.testoLancioDado.SetLabel("E' Uscito:")
        return uscito

    def AggiornaInformazioni(self):
        contaGiocatori = 0
        #aggiorna i label dei pulsanti della griglia per una comprensione migliore di ciò che sta succedendo
        posGiocatori = []
        #print(self.listaGiocatori)
        for n in self.listaGiocatori:
            posGiocatori.append([n.nome,n.posizione])
        conta = 0
        for n in self.listaTipoCaselle:
            conta+=1
            giocatoriDaAggiungere = ""
            for i in posGiocatori:
                if i[1] == conta:
                    giocatoriDaAggiungere+="\n "+i[0]
                    contaGiocatori+=1
            self.tabellone.grigliaPulsanti[conta-1].SetLabel(str(conta) + "\n"+n.tipo + giocatoriDaAggiungere)
        return

    def creaTipoCaselle(self):
        listaTipoCaselle = []
        conta = 0
        luoghiAutobiografici = 6
        canti = 6
        operette = 4
        poeticaDeiPaesaggi = 4
        jolly = 4
        while len(listaTipoCaselle) < 42:
            listaTipoCaselle.append("")
            if luoghiAutobiografici > 0:
                listaTipoCaselle.append("luoghiAutobiografici")
                luoghiAutobiografici-=1
            if canti > 0:
                listaTipoCaselle.append("canti")
                canti-=1
            if operette > 0:
                listaTipoCaselle.append("operette")
                operette-=1
            if poeticaDeiPaesaggi > 0:
                listaTipoCaselle.append("poeticaDeiPaesaggi")
                poeticaDeiPaesaggi-=1
            if jolly > 0:
                listaTipoCaselle.append("jolly")
                jolly-=1
            listaTipoCaselle.append("")
        #print(len(listaTipoCaselle))
        #print(listaTipoCaselle.count("luoghiAutobiografici"),listaTipoCaselle.count("canti"),listaTipoCaselle.count("operette"),listaTipoCaselle.count("poeticaDeiPaesaggi"),listaTipoCaselle.count("jolly"),listaTipoCaselle.count(""))
        listaDisposizione = [Casella.Casella(1,"")]
        listaTipoCaselle.remove("")
        conta = 1
        while len(listaDisposizione) < 42:
            conta+=1
            x = random.choice(listaTipoCaselle)
            listaDisposizione.append(Casella.Casella(conta,x))
            listaTipoCaselle.remove(x)
        #print(listaDisposizione)
        #print(len(listaDisposizione))
        #print(listaDisposizione.count("luoghiAutobiografici"),listaDisposizione.count("canti"),listaDisposizione.count("operette"),listaDisposizione.count("poeticaDeiPaesaggi"),listaDisposizione.count("jolly"),listaDisposizione.count(""))
        self.listaTipoCaselle = listaDisposizione
        return

if __name__ == "__main__":
    app = wx.App()
    gioco = Gioco()
    app.MainLoop()