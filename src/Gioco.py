import wx
import wx.adv
from PIL import Image
import random , time
import Domanda, Lobby , Casella, Giocatore, CampoDaGioco, ElencoDomande



coordinateCaselle = {0:((34,524),(80,65)),1:((35,589),(79,63)),2:((114,589),(79,63)), 3:((193,589),(80,63)), 4:((273,589),(79,63)), 5:((352,589),(80,63)), 6: ((433,589),(79,63)), 7:((512,589),(80,63)), 8:((592,589),(79,63)),
                     9:((671,589),(80,63)), 10: ((751,589),(81,63)), 11: ((832,589),(78,63)), 12:((910,589),(80,63)), 13:((910,519),(80,70)), 14:((910,449),(80,70)), 15:((910,377),(80,72)), 16:((910,308),(80,69)),
                     17:((910,237),(80,70)), 18:((910,166),(80,71)), 19:((910,95),(80,71)), 20:((910,26),(80,69)), 21:((837,26),(73,69)), 22:((756,26),(81,69)), 23:((676,26),(80,69)), 24:((595,26),(81,69)),
                     25:((517,26),(78,69)),26:((435,26),(82,68)),27:((355,26),(81,68)),28:((277,26),(79,68)),29:((196,26),(82,68)),30:((119,25),(80,70)),31:((117,95),(82,69)),32:((118,164),(80,72)),33:((118,236),(80,71)),
                     34:((118,307),(81,70)),35:((118,376),(80,71)),36:((199,376),(77,71)),37:((277,377),(78,70)),38:((356,377),(79,70)),39:((436,377),(85,70)),40:((522,377),(73,70)),41:((595,377),(79,70)),42:((675,377),(78,70))}

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
        self.iconeDisponibili = ["../icone/iconaGinestra-100.png" , "../icone/iconaCandela-100.png" , "../icone/iconaZibaldone-100.png" , "../icone/iconaPassero-100.png" ]
        random.shuffle(self.iconeDisponibili)
        self.listaTipoCaselle = []
        self.creaTipoCaselle()
        self.turnoGiocatore = ""
        self.listaDomande = ElencoDomande.ElencoDomande().listaDomande
        self.listaGiocatori = 0
        self.pulsanteGioca = ""
        self.FinestraLobby = Lobby.Lobby(self.iconeDisponibili)
        self.FinestraLobby.SetTitle("Lobby - Gioco Dell'Oca 4Bs")
        self.FinestraLobby.ShowWithEffect(wx.SHOW_EFFECT_ROLL_TO_BOTTOM,timeout=600)
        self.FinestraLobby.PIniziaPartita.Bind(wx.EVT_BUTTON,self.IniziaPartita)
        #tabellone = classe Campo da Gioco
        self.tabellone = CampoDaGioco.CampoDaGioco()
        self.tabellone.Hide()
        self.tabellone.PGiocaTurno.Bind(wx.EVT_BUTTON, self.GiocaTurnoDi)
        self.tabellone.PGiocaTurno.Disable()
        self.attesaDomanda = False
        self.tabellone.Bind(wx.EVT_CLOSE,self.chiudiGioco)
        self.tabellone.SetTitle("Leopardi - Gioco Dell'Oca 4Bs")
        self.coordinatePosizioniGiocatori = [coordinateGioc1,coordinateGioc2,coordinateGioc3,coordinateGioc4]
        #self.tabellone.Bind(wx.EVT_CLOSE,self.chiudiGioco)

        # conterrà l'immagine del campo da gioco, generata dalla funzione "creaGraficaCaselle"
        #self.sfondoCampoDaGioco

        return

    def chiudiGioco(self,event):
        #self.tabellone.finale(self.listaGiocatori)
        quit()
        return

    def Riavvia(self,event):
        self.tabellone.Destroy()
        self.__init__()
        return

    def IniziaPartita(self,evt):
        giocatori = []
        conta=0
        nomi = []
        for n in self.FinestraLobby.listaToggleButton:
            if n.GetValue():
                giocatori.append(Giocatore.Giocatore((self.FinestraLobby.listaTc[n.GetId()-1]).GetValue(),self.iconeDisponibili[n.GetId()-1]))
                nomi.append(giocatori[conta].nome)
                conta+=1
        for n in nomi:
            if nomi.count(n) > 1 or n.replace(" ","") == "":
                break
        else:
            self.tabellone.Show()
            self.FinestraLobby.Destroy()
            self.listaGiocatori = giocatori
            random.shuffle(self.listaGiocatori)
            self.turnoGiocatore = self.listaGiocatori[0]
            self.aggiornaGrafica()
            
            self.tabellone.testoTurno.SetLabel(self.turnoGiocatore.nome)
            self.tabellone.PGiocaTurno.Enable()
            self.tabellone.testoLancioDado.SetOwnForegroundColour((240, 240, 240))
            self.tabellone.testoDado.SetOwnForegroundColour((240,240,240))

            bmp = wx.Bitmap(self.turnoGiocatore.iconPath)
            bmp.SetSize( (100,100) )
            self.tabellone.viewerIconPlayerTurno.SetBitmap(bmp)
            #self.tabellone.viewerIconPlayerTurno.SetSize((150,100))
            #self.tabellone.viewerIconaEsito.SetBitmap(wx.Bitmap((100,100),depth = 2))
        return

    def AggiornaTurno(self):
        self.tabellone.testoLancioDado.SetLabel("")
        giocatori = self.listaGiocatori
        turnoDi = self.turnoGiocatore
        #ix = index
        ix = giocatori.index(turnoDi)
        # ix = 0/1/2/3 --> +2 = 2/3/4/5
        # len =                   2/3/4
        if (ix + 2) > len(giocatori):
            self.turnoGiocatore = giocatori[0]
        else:
            self.turnoGiocatore = giocatori[ix+1]
        self.tabellone.testoTurno.SetLabel(self.turnoGiocatore.nome)
        self.tabellone.PGiocaTurno.Enable()

        bmp = wx.Bitmap(self.turnoGiocatore.iconPath)
        bmp.SetSize((100, 100))
        self.tabellone.viewerIconPlayerTurno.SetBitmap(bmp)
        #self.tabellone.viewerIconPlayerTurno.SetSize((75,75))
        return

    def aggiornaGrafica(self):
        sfondo = self.sfondoCampoDaGioco.copy()

        for n in self.listaGiocatori:
            iconaGiocatore = Image.open(n.iconPath).resize( (24,24) )
            coordinatePosizioneGiocatore = self.coordinatePosizioniGiocatori[self.listaGiocatori.index(n)][n.posizione]    
            sfondo.paste(iconaGiocatore, coordinatePosizioneGiocatore, iconaGiocatore)
        wx_image = wx.Image(sfondo.size[0], sfondo.size[1])
        wx_image.SetData(sfondo.convert("RGB").tobytes())
        bitmap = wx.Bitmap(wx_image)

        self.tabellone.viewer.SetBitmap(bitmap)
        return

    def GiocaTurnoDi(self,event):
        if not self.attesaDomanda:
            dado = self.tiraDado()
            self.tabellone.testoDado.SetLabel(str(dado))
            for n in range(dado):
                if self.listaGiocatori[self.listaGiocatori.index(self.turnoGiocatore)].posizione + 1 > 42:
                    self.listaGiocatori[self.listaGiocatori.index(self.turnoGiocatore)].muoviGiocatore(1)
                    self.tabellone.finale(self.listaGiocatori)
                    self.tabellone.pulsanteChiudi.Bind(wx.EVT_BUTTON, self.chiudiGioco)
                    self.tabellone.pulsanteRigioca.Bind(wx.EVT_BUTTON, self.Riavvia)
                    return
                else:
                    self.listaGiocatori[self.listaGiocatori.index(self.turnoGiocatore)].muoviGiocatore(1)
                    self.aggiornaGrafica()
                    time.sleep(0.5)
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
            self.finestraDomanda = Domanda.FinestraDomanda(domanda,self.turnoGiocatore,self.listaTipoCaselle[self.turnoGiocatore.posizione-1].tipo)
            self.finestraDomanda.ShowWithEffect(wx.SHOW_EFFECT_ROLL_TO_BOTTOM,timeout=600)
            self.finestraDomanda.PulsanteA.Bind(wx.EVT_BUTTON, self.visualizzaCorretteErrate)
            self.finestraDomanda.PulsanteB.Bind(wx.EVT_BUTTON, self.visualizzaCorretteErrate)
            self.finestraDomanda.PulsanteC.Bind(wx.EVT_BUTTON, self.visualizzaCorretteErrate)
            return
        return

    def nulla(self,evt):
        return

    def visualizzaCorretteErrate(self,event):
        ID = event.GetId()
        self.EsitoCorretto = False
        self.tabellone.viewerIconaEsito.SetBitmap(wx.Bitmap("../icone/iconaErrato.png"))
        if self.finestraDomanda.esitoRisposta(ID):
            self.EsitoCorretto = True
            self.tabellone.viewerIconaEsito.SetBitmap(wx.Bitmap("../icone/iconaEsatto.png"))
        self.finestraDomanda.Bind(wx.EVT_TIMER,self.Risposto,self.finestraDomanda.timer)
        self.finestraDomanda.timer.StartOnce(2200)
        lista = [self.finestraDomanda.PulsanteA,self.finestraDomanda.PulsanteB,self.finestraDomanda.PulsanteC]
        for pulsante in lista:
            #Colorazione delle risposte giuste e sbagliate (verdi e rosse)
            pulsante.SetBackgroundColour("red")
            #non permette di correggere la risposta: prende in considerazione la prima risposta data.
            pulsante.Bind(wx.EVT_BUTTON,self.nulla)
            if self.finestraDomanda.IdCorretto == pulsante.GetId():
                pulsante.SetBackgroundColour("green")
        return

    def Risposto(self,event):
        self.tabellone.PGiocaTurno.Enable()
        self.attesaDomanda = False
        self.finestraDomanda.Destroy()
        self.tabellone.viewerIconaEsito.SetBitmap(wx.Bitmap((100,100),depth = 2))
        if not self.EsitoCorretto:
            self.listaGiocatori[self.listaGiocatori.index(self.turnoGiocatore)].sbagliate += 1
            self.tabellone.testoDado.Hide()
            self.AggiornaTurno()
        else:
            self.listaGiocatori[self.listaGiocatori.index(self.turnoGiocatore)].corrette += 1
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
        self.tabellone.testoLancioDado.SetLabel("È Uscito:")
        return uscito

    def creaTipoCaselle(self):
        #funzione iniziale per creare e distribuire le varie tipologie di caselle
        #numero caselle = 42 + una iniziale (0)
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
        listaDisposizione = [Casella.Casella(1,"")]
        listaTipoCaselle.remove("")
        conta = 1
        while len(listaDisposizione) < 42:
            conta+=1
            x = random.choice(listaTipoCaselle)
            listaDisposizione.append(Casella.Casella(conta,x))
            listaTipoCaselle.remove(x)
        self.listaTipoCaselle = listaDisposizione
        diz = {}
        for n in range(1,len(self.listaTipoCaselle)+1):
            diz[n] = self.listaTipoCaselle[n-1].tipo
        #print(diz)
        self.creaGraficaCaselle(diz)
        return

    def creaGraficaCaselle(self,diz):
        #BLU = POETICHEDEIPAESAGGI 
        #VERDE = LUOGHIAUTOBIOGRAFICI 
        #ROSSO = CANTI 
        #GIALLO = OPERETTE 
        campoDaGioco = Image.open('../tabellone/fileCampoDaGiocoRid.png')
        #campoDaGioco = Image.open('bgMHA.jpg').resize((1075,670))
        sfondo = campoDaGioco.copy()
        wx_image = wx.Image(sfondo.size[0], sfondo.size[1])
        wx_image.SetData(sfondo.convert("RGB").tobytes())
        icona = Image.open("../tabellone/quadratoNeroTrasparente-500.png")
        icona = icona.resize((coordinateCaselle[0][1][0], coordinateCaselle[0][1][1]))
        sfondo.paste(icona, (coordinateCaselle[0][0][0], coordinateCaselle[0][0][1]), icona)
        for n in diz:
            tipo = diz[n]
            if tipo != "":
                if tipo == "luoghiAutobiografici":
                    icona = Image.open("../tabellone/quadratoVerdeTrasparente-500.png")
                elif tipo == "poeticaDeiPaesaggi":
                    icona = Image.open("../tabellone/quadratoBluTrasparente-500.png")
                elif tipo == "canti":
                    icona = Image.open("../tabellone/quadratoRossoTrasparente-500.png")
                elif tipo == "operette":
                    icona = Image.open("../tabellone/quadratoGialloTrasparente-500.png")
                elif tipo == "jolly":
                    icona = Image.open("../tabellone/simboloInfinito-500.png")
            else:
                icona = Image.open("../tabellone/quadratoNeroTrasparente-500.png")
            icona = icona.resize((coordinateCaselle[n][1][0],coordinateCaselle[n][1][1]))
            sfondo.paste(icona,(coordinateCaselle[n][0][0],coordinateCaselle[n][0][1]),icona)
        
        self.sfondoCampoDaGioco = sfondo
                    
        return

if __name__ == "__main__":
    app = wx.App()
    gioco = Gioco()
    app.MainLoop()

    #pyinstaller --onefile -w file.py
    #NSIS
