import Domanda, wx,random , time , Lobby , Casella, Giocatore, CampoDaGioco, ElencoDomande
import wx.adv
from PIL import Image

coordinateGioc1 = { 0:(47,531), 1:(46,595), 2:(126,595), 3:(205,595) ,4:(284,595) , 5:(364,595) , 6:(443,595) , 7:(524,595) , 8:(603,595) , 9:(682,595) , 10:(763,595) , 11:(842,595) , 12:(921,595),
                    13:(921,529) , 14:(921,459) , 15:(921,389) , 16:(921,318) , 17:(921,247) , 18:(921,177) , 19:(921,106) , 20:(921,35), 21:(843,35) , 22:(770,35) , 23:(689,35) , 24:(608,35) ,
                    25:(528,35) , 26:(448,35), 27:(367,35) , 28:(288,35) , 29:(209,35), 30:(129,35) , 31:(129,103) , 32:(129,173) , 33:(129,245) , 34:(129,315), 35:(129,385) , 36:(209,385) , 37:(288,385),
                    38: (368, 385), 39: (448, 385), 40: (530, 385), 41: (607, 385), 42: (686, 385), 43: (686, 319)}

coordinateGioc2 = { 0:(82,531), 1:(81,595), 2:(161,595), 3:(240,595) ,4:(319,595) , 5:(399,595) , 6:(478,595) , 7:(559,595) , 8:(638,595) , 9:(717,595) , 10:(798,595) , 11:(877,595) , 12:(956,595),
                    13:(956,529) , 14:(956,459) , 15:(956,389) , 16:(956,318) , 17:(956,247) , 18:(956,177) , 19:(956,106) , 20:(956,35), 21:(880,35) , 22:(805,35) , 23:(724,35) , 24:(643,35) ,
                    25:(563,35), 26:(483,35) , 27:(402,35) , 28:(323,35) , 29:(244,35), 30:(164,35) , 31:(164,103) , 32:(164,173) , 33:(164,245) , 34:(164,315), 35:(164,385) , 36:(244,385) , 37:(323,385),
                    38: (403, 385), 39: (483, 385), 40: (565, 385), 41: (642, 385), 42: (721, 385), 43: (721, 319)}

coordinateGioc3 = { 0:(47,559), 1:(46,623), 2:(126,623), 3:(205,623) ,4:(284,623) , 5:(364,623) , 6:(443,623) , 7:(524,623) , 8:(603,623) , 9:(682,623) , 10:(763,623) , 11:(842,623) , 12:(921,623),
                    13:(921,557) , 14:(921,487) , 15:(921,417) , 16:(921,346) , 17:(921,275) , 18:(921,205) , 19:(921,134) , 20:(921,63), 21:(846,63) , 22:(770,63) , 23:(689,63) , 24:(608,63) ,
                    25:(528,63) , 26:(448,63), 27:(367,63) , 28:(288,63) , 29:(209,63), 30:(129,63) , 31:(129,131) , 32:(129,201) , 33:(129,273) , 34:(129,343), 35:(129,413) , 36:(209,413) , 37:(288,413),
                    38: (368, 413), 39: (448, 413), 40: (530, 413), 41: (607, 413), 42: (686, 413), 43: (686, 347)}


coordinateGioc4 = { 0:(82,559), 1:(81,623), 2:(161,623), 3:(240,623) ,4:(319,623) , 5:(399,623) , 6:(478,623) , 7:(559,623) , 8:(638,623) , 9:(717,623) , 10:(798,623) , 11:(877,623) , 12:(956,623),
                    13:(956,557) , 14:(956,487) , 15:(956,417) , 16:(956,346) , 17:(956,275) , 18:(956,205) , 19:(956,134) , 20:(956,63), 21:(880,63) , 22:(805,63) , 23:(724,63) , 24:(643,63),
                    25:(563,63) , 26:(483,63), 27:(402,63) , 28:(323,63) , 29:(244,63), 30:(164,63) , 31:(164,131) , 32:(164,201) , 33:(164,273) , 34:(164,343), 35:(164,413) , 36:(244,413) , 37:(323,413),
                    38: (403, 413), 39: (483, 413), 40: (565, 413), 41: (642, 413), 42: (721, 413), 43: (721, 347)}

class Gioco:
    def __init__(self):
        self.iconeDisponibili = [Image.open("iconaXverde-24.png"),Image.open("iconaXrosa-24.png"),Image.open("iconaXblu-24.png"),Image.open("iconaXgialla-24.png")]
        random.shuffle(self.iconeDisponibili)
        self.listaTipoCaselle = []
        self.creaTipoCaselle()
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
        self.coordinatePosizioniGiocatori = [coordinateGioc1,coordinateGioc2,coordinateGioc3,coordinateGioc4]
        return
    def chiudiGioco(self,event):
        quit()
        return

    def IniziaPartita(self,evt):
        giocatori = []
        conta=0
        nomi = []
        for n in self.FinestraLobby.listaToggleButton:
            if n.GetValue():
                giocatori.append(Giocatore.Giocatore((self.FinestraLobby.listaTc[n.GetId()-1]).GetValue(),self.iconeDisponibili[conta]))
                nomi.append(giocatori[conta].nome)
                conta+=1
        for n in nomi:
            if nomi.count(n) > 1:
                break
        else:
            self.tabellone.Show()
            self.FinestraLobby.Destroy()
            self.listaGiocatori = giocatori
            random.shuffle(self.listaGiocatori)
            self.turnoGiocatore = self.listaGiocatori[0]
            #crea la parte parte grafica X
            sfondo = Image.open('fileCampoDaGiocoRid.png')
            pil_image = sfondo.copy()
            for n in self.listaGiocatori:
                pil_image.paste(n.icona, self.coordinatePosizioniGiocatori[self.listaGiocatori.index(n)][n.posizione])
                wx_image = wx.Image(pil_image.size[0], pil_image.size[1])
                wx_image.SetData(pil_image.convert("RGB").tobytes())
                bitmap = wx.Bitmap(wx_image)
                self.tabellone.viewer.SetBitmap(bitmap)
            self.tabellone.testoTurno.SetLabel(self.turnoGiocatore.nome)
            self.tabellone.PGiocaTurno.Enable()
            self.tabellone.testoLancioDado.SetOwnForegroundColour((240, 240, 240))
            self.tabellone.testoDado.SetOwnForegroundColour((240,240,240))

            ico = wx.Image(self.turnoGiocatore.icona.size[0],self.turnoGiocatore.icona.size[1])
            ico.SetData(self.turnoGiocatore.icona.convert("RGB").tobytes())
            bmp = wx.Bitmap(ico)
            self.tabellone.viewerIconPlayerTurno.SetBitmap(bmp)
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
        ico = wx.Image(self.turnoGiocatore.icona.size[0], self.turnoGiocatore.icona.size[1])
        ico.SetData(self.turnoGiocatore.icona.convert("RGB").tobytes())
        bmp = wx.Bitmap(ico)
        self.tabellone.viewerIconPlayerTurno.SetBitmap(bmp)
        return

    def aggiornaGrafica(self):
        sfondo = Image.open('fileCampoDaGiocoRid.png')
        pil_image = sfondo.copy()
        for giocatore in self.listaGiocatori:
            pil_image.paste(giocatore.icona, self.coordinatePosizioniGiocatori[self.listaGiocatori.index(giocatore)][giocatore.posizione])
            wx_image = wx.Image(pil_image.size[0], pil_image.size[1])
            wx_image.SetData(pil_image.convert("RGB").tobytes())
            bitmap = wx.Bitmap(wx_image)
            self.tabellone.viewer.SetBitmap(bitmap)
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
                    self.aggiornaGrafica()
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

    def creaTipoCaselle(self):
        listaTipoCaselle = []
        luoghiAutobiografici = 6
        canti = 6
        operette = 4
        poeticaDeiPaesaggi = 4
        jolly = 4
        while len(listaTipoCaselle) < 42:
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
        diz = {}
        for n in range(1,len(self.listaTipoCaselle)+1):
            diz[n] = self.listaTipoCaselle[n-1].tipo
        print(diz)
        return

if __name__ == "__main__":
    app = wx.App()
    gioco = Gioco()
    app.MainLoop()