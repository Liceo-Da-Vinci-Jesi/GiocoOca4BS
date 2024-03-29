import random , time

import wx , wx.adv
import pygame , pygame.mixer
from PIL import Image
import Domanda, Lobby , Casella, Giocatore, CampoDaGioco, ElencoDomande, datetime, Impostazioni

# ---------------------------------
import os
module_dir = os.path.dirname(__file__)
# ---------------------------------

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
        self.iconeDisponibili = [ os.path.join(module_dir,"icone/iconaGinestra-100.png") , os.path.join(module_dir,"icone/iconaCandela-100.png") , os.path.join(module_dir,"icone/iconaZibaldone-100.png") , os.path.join(module_dir,"icone/iconaPassero-100.png") ]
        random.shuffle(self.iconeDisponibili)
        self.listaTipoCaselle = []
        self.creaTipoCaselle()
        self.turnoGiocatore = ""
        self.listaDomande = ElencoDomande.ElencoDomande().listaDomande
        self.listaGiocatori = 0
        self.pulsanteGioca = ""
        self.FinestraLobby = Lobby.Lobby(self.iconeDisponibili)
        self.FinestraLobby.SetTitle("Il gioco dei paesaggi di Giacomo - Lobby")
        self.FinestraLobby.ShowWithEffect(wx.SHOW_EFFECT_ROLL_TO_BOTTOM,timeout=600)
        self.FinestraLobby.PIniziaPartita.Bind(wx.EVT_BUTTON,self.IniziaPartita)
        self.FinestraLobby.Bind(wx.EVT_CLOSE, self.chiudiGioco)
        #tabellone = classe Campo da Gioco
        self.tabellone = CampoDaGioco.CampoDaGioco()
        self.tabellone.Hide()
        self.tabellone.PGiocaTurno.Bind(wx.EVT_BUTTON, self.GiocaTurnoDi)
        self.tabellone.PGiocaTurno.Disable()
        self.attesaDomanda = False
        self.tabellone.SetTitle("Il gioco dei paesaggi di Giacomo")
        self.coordinatePosizioniGiocatori = [coordinateGioc1,coordinateGioc2,coordinateGioc3,coordinateGioc4]
        self.tabellone.Bind(wx.EVT_CLOSE,self.chiudiGioco)
        self.audioDadi = wx.adv.Sound( os.path.join(module_dir,"audio/Casting dices.wav") )
        pygame.mixer.music.load( os.path.join(module_dir,"audio/MarioGalaxy.mp3") )
        pygame.mixer.music.play(-1)
        self.Impostazioni = Impostazioni.finestraImpostazioni()
        self.Impostazioni.r1.Bind(wx.EVT_RADIOBUTTON, self.cambioTema)
        #self.Impostazioni.sliderGenerale.SetValue(int(pygame.mixer.music.get_volume()*100))
        #self.Impostazioni.sliderGenerale.Bind(wx.EVT_SLIDER,self.impostaVolume)
        self.Impostazioni.sliderMusica.SetValue(int(pygame.mixer.music.get_volume() * 100))
        self.Impostazioni.sliderMusica.Bind(wx.EVT_SLIDER, self.impostaVolume)
        self.Impostazioni.rFx1.Bind(wx.EVT_RADIOBUTTON,self.impostaEffettiSonori)
        self.Impostazioni.rFx2.Bind(wx.EVT_RADIOBUTTON,self.impostaEffettiSonori)
        self.Impostazioni.r2.Bind(wx.EVT_RADIOBUTTON, self.cambioTema)
        self.FinestraLobby.PImpostazioni.Bind(wx.EVT_BUTTON, self.apriImpostazioni)
        self.Impostazioni.Bind(wx.EVT_CLOSE, self.chiudiImpostazioni)
        self.Impostazioni.list.Bind(wx.EVT_LISTBOX_DCLICK,self.chiudiImpostazioni)
        self.Impostazioni.pulsIndietro.Bind(wx.EVT_BUTTON,self.chiudiImpostazioni)
        self.ColoreSfondo = (40, 40, 40)
        self.ColoreTesto = (255,255,255)
        self.Impostazioni.list.Bind(wx.EVT_LISTBOX, self.sceltaTracciaAudio)
        self.tracciaAudio = os.path.join(module_dir,"audio/Bg/Lacrimosa.mp3")
        self.tabellone.viewerIconaImpo.Bind(wx.EVT_BUTTON,self.apriImpostazioni)
        self.tabellone.viewerIconaExit.Bind(wx.EVT_BUTTON,self.chiudiGioco)
        self.statoFx = True

        return
    
    def cambioTema(self,evt):
        if self.Impostazioni.r1.GetValue():
            #se il radio Button ci da True o  meglio é premuto
            self.ColoreSfondo = "white"
            self.ColoreTesto = (40,40,40)
        else:
            self.ColoreSfondo = (40,40,40)
            self.ColoreTesto = "white"

        self.Impostazioni.panel.SetBackgroundColour(self.ColoreSfondo)
        for n in self.Impostazioni.listaTesti:
            #testi ovviamente più scuri
            n.SetForegroundColour(self.ColoreTesto)
        self.FinestraLobby.panel.SetBackgroundColour(self.ColoreSfondo)

        self.FinestraLobby.Refresh()
        self.Impostazioni.Refresh()
        self.tabellone.panel.SetBackgroundColour(self.ColoreSfondo)
        self.tabellone.testoTurno.SetForegroundColour(self.ColoreTesto)
        self.tabellone.Refresh()
        self.AggiornaTemaIcone()
        return
    
    def impostaVolume(self,evt):
        pygame.mixer.music.set_volume(self.Impostazioni.sliderMusica.GetValue()/100)
        return
    
    def apriImpostazioni(self,evt):
        self.FinestraLobby.Disable()
        self.tabellone.PGiocaTurno.Disable()
        #non inizi una partita senza prima aver preparato
        #le impostazioni di partita
        self.Impostazioni.Show()
        return
    
    def chiudiImpostazioni(self,evt):
        self.tabellone.PGiocaTurno.Enable()
        self.FinestraLobby.Enable()
        self.Impostazioni.Hide()
        return
    
    def impostaEffettiSonori(self,evt):
        if self.Impostazioni.rFx1.GetValue():
            self.statoFx = True
        else:
            self.statoFx = False
        return
    
    def sceltaTracciaAudio(self,evt):
        if self.Impostazioni.list.GetString(self.Impostazioni.list.GetSelection()) != "":
            self.tracciaAudio = os.path.join(module_dir, "audio/Bg/" + self.Impostazioni.list.GetString(self.Impostazioni.list.GetSelection()) + ".mp3")
            pygame.mixer.music.load(self.tracciaAudio)
            pygame.mixer.music.play(-1)
            self.Impostazioni.sliderMusica.SetValue(int(pygame.mixer.music.get_volume()*100))
            #la path e poi serve per il play()
        return
    
    def chiudiGioco(self,event):
        #self.tabellone.finale(self.listaGiocatori, datetime.datetime.now() - self.OraInizio)
        wx.Exit()
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
        #l'else viene eseguito se non il ciclo for si completa
        else:
            self.OraInizio = datetime.datetime.now()
            self.tabellone.Show()
            self.FinestraLobby.Hide()
            self.listaGiocatori = giocatori
            random.shuffle(self.listaGiocatori)
            self.turnoGiocatore = self.listaGiocatori[0]
            self.aggiornaGrafica()
            
            self.tabellone.testoTurno.SetLabel(self.turnoGiocatore.nome)
            self.tabellone.testoTurno.SetForegroundColour(((255,255,255)))
            self.tabellone.PGiocaTurno.Enable()

            bmp = wx.Bitmap(self.turnoGiocatore.iconPath)
            bmp.SetSize( (100,100) )
            self.tabellone.viewerIconPlayerTurno.SetBitmap(bmp)
            self.aggiornaGraficaTurni()
            for n in self.tabellone.listaTesti:
                n.SetForegroundColour(self.ColoreTesto)
            self.tabellone.panel.SetBackgroundColour(self.ColoreSfondo)
            self.AggiornaTemaIcone()
        return
    
    def AggiornaTemaIcone(self):
        bmpImpo = wx.Bitmap( os.path.join(module_dir,"icone/setting-b.png") )
        bmpExit = wx.Bitmap( os.path.join(module_dir,"icone/on-off-button-b.png") )
        self.tabellone.viewerIconaImpo.SetBackgroundColour(self.ColoreSfondo)
        self.tabellone.viewerIconaExit.SetBackgroundColour(self.ColoreSfondo)
        if self.ColoreSfondo == "white":
            bmpImpo = wx.Bitmap( os.path.join(module_dir,"icone/setting-n.png") )
            bmpExit = wx.Bitmap( os.path.join(module_dir,"icone/on-off-button-n.png") )
        imgImpo = bmpImpo.ConvertToImage().Rescale(30,30)
        imgExit = bmpExit.ConvertToImage().Rescale(30,30)
        self.tabellone.viewerIconaImpo.SetBitmap(wx.Bitmap(imgImpo))
        self.tabellone.viewerIconaExit.SetBitmap(wx.Bitmap(imgExit))
        return
    
    def AggiornaTurno(self):
        #"imposta" il tabellone con i dati del giocatore prossimo a giocare
        self.turnoGiocatore = self.giocatoreSuccessivoA(self.turnoGiocatore)
        self.tabellone.testoTurno.SetLabel(self.turnoGiocatore.nome)
        self.tabellone.PGiocaTurno.Enable()
        bmp = wx.Bitmap(self.turnoGiocatore.iconPath)
        bmp.SetSize((100, 100))
        self.tabellone.viewerIconPlayerTurno.SetBitmap(bmp)
        self.tabellone.viewerDado.SetBitmap(wx.Bitmap())
        self.aggiornaGraficaTurni()
        return

    def aggiornaGraficaTurni(self):
        #sezione di anteprima dove è possibile vedere i turni successivi a quello in corso
        p1 = self.giocatoreSuccessivoA(self.turnoGiocatore)
        bmp1 = wx.Bitmap(p1.iconPath)
        img1 = bmp1.ConvertToImage()
        img1.Rescale(60,60)
        nbmp1 = wx.Bitmap(img1)
        self.tabellone.viewerTurno1.SetBitmap(nbmp1)

        p2 = self.giocatoreSuccessivoA(p1)
        bmp2 = wx.Bitmap(p2.iconPath)
        img2 = bmp2.ConvertToImage().ConvertToDisabled()
        img2.Rescale(40,40)
        nbmp2 = wx.Bitmap(img2)
        self.tabellone.viewerTurno2.SetBitmap(nbmp2)

        p3 = self.giocatoreSuccessivoA(p2)
        bmp3 = wx.Bitmap(p3.iconPath)
        img3 = bmp3.ConvertToImage().ConvertToDisabled()
        img3.Rescale(40,40)
        nbmp3 = wx.Bitmap(img3)
        self.tabellone.viewerTurno3.SetBitmap(nbmp3)
        return
    
    #calcola il giocatore successivo a "giocatore"
    def giocatoreSuccessivoA(self,giocatore):
        giocatori = self.listaGiocatori
        turnoDi = giocatore
        # ix = index
        ix = giocatori.index(turnoDi)
        # ix = 0/1/2/3 --> +2 = 2/3/4/5
        # len =                   2/3/4
        if (ix + 2) > len(giocatori):
            player = giocatori[0]
        else:
            player = giocatori[ix + 1]
        return player

    def aggiornaGrafica(self):
        #ad ogni movimento di ogni singolo giocatore, crea una copia dello sfondo e ci incolla sopra le icone dei giocatori alle rispettive coordinate
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
        #funzione che viene eseguita ogni volta che il pulsante principale gioca viene premuto
        if not self.attesaDomanda:
            dado = self.tiraDado()
            for n in range(dado):
                if self.listaGiocatori[self.listaGiocatori.index(self.turnoGiocatore)].posizione + 1 > 42:
                    #QUALCUNO HA VINTO
                    TempoTrascorso = datetime.datetime.now() - self.OraInizio
                    self.listaGiocatori[self.listaGiocatori.index(self.turnoGiocatore)].muoviGiocatore(1)
                    self.tabellone.finale(self.listaGiocatori,self.ColoreSfondo,self.ColoreTesto, TempoTrascorso)
                    pygame.mixer.stop()
                    if self.statoFx:
                        wx.adv.Sound( os.path.join(module_dir,"audio/vittoria" + str(random.randint(1,2)) + ".wav") ).Play()
                    self.tabellone.pulsanteChiudi.Bind(wx.EVT_BUTTON, self.chiudiGioco)
                    self.tabellone.pulsanteRigioca.Bind(wx.EVT_BUTTON, self.Riavvia)
                    return
                else:
                    self.listaGiocatori[self.listaGiocatori.index(self.turnoGiocatore)].muoviGiocatore(1)
                    self.aggiornaGrafica()
                    time.sleep(0.38)
            time.sleep(0.5)
            tipoDiCasella = self.listaTipoCaselle[self.turnoGiocatore.posizione-1].tipo
            #se il tipo di casella su cui è capitato il giocatore è nulla o c'è il jolly, la finestra domanda non viene aperta
            if tipoDiCasella == "":
                self.AggiornaTurno()
                return
            if tipoDiCasella == "jolly":
                #se è capitato su un jolly il giocatore rilancia il dado
                if self.statoFx:
                    wx.adv.Sound( os.path.join(module_dir,"audio/jolly" + str(random.randint(1,5)) + ".wav") ).Play()
                return

            ############### Apertura finestra domanda
            self.tabellone.PGiocaTurno.Disable()
            self.tabellone.viewerIconaImpo.Disable()
            self.attesaDomanda = True
            domanda = Domanda.scegliDomandaDaFare(tipoDiCasella,self.listaDomande)
            self.finestraDomanda = Domanda.FinestraDomanda(domanda,self.turnoGiocatore,tipoDiCasella)
            self.finestraDomanda.ShowWithEffect(wx.SHOW_EFFECT_ROLL_TO_BOTTOM,timeout=600)
            self.finestraDomanda.SetFocus()
            self.finestraDomanda.Raise()
            self.finestraDomanda.PulsanteA.Bind(wx.EVT_BUTTON, self.visualizzaCorretteErrate)
            self.finestraDomanda.PulsanteB.Bind(wx.EVT_BUTTON, self.visualizzaCorretteErrate)
            self.finestraDomanda.PulsanteC.Bind(wx.EVT_BUTTON, self.visualizzaCorretteErrate)
            return
        return

    def visualizzaCorretteErrate(self,event):
        ID = event.GetId()
        if self.finestraDomanda.esitoRisposta(ID):
            #se la risposta è corretta
            if self.statoFx:
                sound = wx.adv.Sound( os.path.join(module_dir,"audio/audioPositive" + str(random.randint(1,7)) + ".wav") )
                if self.tracciaAudio in ( os.path.join(module_dir,"audio/Bg/Lacrimosa.mp3") , os.path.join(module_dir,"audio/Bg/Aria.mp3") , os.path.join(module_dir,"audio/Bg/Inverno.mp3") , os.path.join(module_dir,"audio/Bg/Palladio.mp3") ):
                    sound = wx.adv.Sound( os.path.join(module_dir, "audio/audioPositive" + str(random.choice((7,1))) + ".wav") )
                sound.Play(flags = wx.adv.SOUND_ASYNC)
            self.EsitoDomanda = True
            self.tabellone.viewerIconaEsito.SetBitmap(wx.Bitmap( os.path.join(module_dir,"icone/iconaEsatto.png") ))
        else:
            #se la risposta NON è corretta
            if self.statoFx:
                sound = wx.adv.Sound( os.path.join(module_dir,"audio/audioNegative" + str(random.randint(1, 5)) + ".wav") )
                if self.tracciaAudio in ( os.path.join(module_dir,"audio/Bg/Lacrimosa.mp3") , os.path.join(module_dir,"audio/Bg/Aria.mp3") , os.path.join(module_dir,"audio/Bg/Inverno.mp3") , os.path.join(module_dir,"audio/Bg/Palladio.mp3") ):
                    sound = wx.adv.Sound( os.path.join(module_dir,"audio/audioNegative" + str(random.choice((5, 1))) + ".wav") )
                sound.Play(flags=wx.adv.SOUND_ASYNC)
            self.EsitoDomanda = False
            self.tabellone.viewerIconaEsito.SetBitmap(wx.Bitmap( os.path.join(module_dir,"icone/iconaErrato.png") ))
            
        self.finestraDomanda.Bind(wx.EVT_TIMER,self.Risposto,self.finestraDomanda.timer)
        self.finestraDomanda.timer.StartOnce(2200)
        lista = [self.finestraDomanda.PulsanteA,self.finestraDomanda.PulsanteB,self.finestraDomanda.PulsanteC]
        #un timer presente nella finestraDomanda si attiva (2.2s) e successivamente si attiva la funzione Risposto, però nel mentre i pulsanti si colorano in base alla loro risposta (verde->corretto;rosso->sbagliato)
        for pulsante in lista:
            pulsante.SetBackgroundColour("red")
            #non permette di correggere la risposta: prende in considerazione la prima risposta data.
            pulsante.Bind(wx.EVT_BUTTON,self.nulla)
            if self.finestraDomanda.IdCorretto == pulsante.GetId():
                pulsante.SetBackgroundColour("green")
        return

    def Risposto(self,event):
        self.tabellone.viewerIconaImpo.Enable()
        self.tabellone.PGiocaTurno.Enable()
        self.attesaDomanda = False
        self.finestraDomanda.Destroy()
        self.tabellone.viewerIconaEsito.SetBitmap(wx.Bitmap())
        self.tabellone.viewerDado.SetBitmap(wx.Bitmap())
        if not self.EsitoDomanda:
            self.listaGiocatori[self.listaGiocatori.index(self.turnoGiocatore)].sbagliate += 1
            self.AggiornaTurno()
        else:
            self.listaGiocatori[self.listaGiocatori.index(self.turnoGiocatore)].corrette += 1
        return

    def tiraDado(self):
        self.tabellone.viewerDado.SetBitmap(wx.Bitmap((100,100),depth = 2))
        if self.statoFx:
            self.audioDadi.Play(flags = wx.adv.SOUND_ASYNC)
        for n in range(7):
            uscito = random.randint(1, 6)
            percorso = os.path.join(module_dir,"dado/dado" + str(uscito) + ".png")
            bmp = wx.Bitmap(percorso)
            bmp.SetSize( (100,100) )
            self.tabellone.viewerDado.SetBitmap(bmp)
            time.sleep(0.08*n)
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
        #GIALLO = OPERETTE C:\Users\s7096089\Desktop\GiocoOca4BS\GiocoDellOca4Bs\tabellone
        campoDaGioco = Image.open( os.path.join(module_dir,'tabellone/fileSfondoCampoDaGioco.png') )
        #campoDaGioco = Image.open('bgMHA.jpg').resize((1075,670))
        sfondo = campoDaGioco.copy()
        wx_image = wx.Image(sfondo.size[0], sfondo.size[1])
        wx_image.SetData(sfondo.convert("RGB").tobytes())
        icona = Image.open( os.path.join(module_dir,"tabellone/quadratoNeroTrasparente-500.png") )
        icona = icona.resize((coordinateCaselle[0][1][0], coordinateCaselle[0][1][1]))
        sfondo.paste(icona, (coordinateCaselle[0][0][0], coordinateCaselle[0][0][1]), icona)
        for n in diz:
            tipo = diz[n]
            if tipo != "":
                if tipo == "luoghiAutobiografici":
                    icona = Image.open( os.path.join(module_dir,"tabellone/quadratoVerdeTrasparente-500.png") )
                elif tipo == "poeticaDeiPaesaggi":
                    icona = Image.open( os.path.join(module_dir,"tabellone/quadratoBluTrasparente-500.png") )
                elif tipo == "canti":
                    icona = Image.open( os.path.join(module_dir,"tabellone/quadratoRossoTrasparente-500.png") )
                elif tipo == "operette":
                    icona = Image.open( os.path.join(module_dir,"tabellone/quadratoGialloTrasparente-500.png") )
                elif tipo == "jolly":
                    icona = Image.open( os.path.join(module_dir,"tabellone/simboloInfinito-500.png") )
            else:
                icona = Image.open( os.path.join(module_dir,"tabellone/quadratoNeroTrasparente-500.png") )
            icona = icona.resize((coordinateCaselle[n][1][0],coordinateCaselle[n][1][1]))
            sfondo.paste(icona,(coordinateCaselle[n][0][0],coordinateCaselle[n][0][1]),icona)
            sfondo.paste(icona,(coordinateCaselle[n][0][0],coordinateCaselle[n][0][1]),icona)
        img = Image.open( os.path.join(module_dir,"tabellone/fileScheletroTabellone.png") )
        sfondo.paste(img,(0,0),img)
        #sfondo.save("tab.png", "PNG")
        
        self.sfondoCampoDaGioco = sfondo
        return

    def nulla(self,evt):
        return

if __name__ == "__main__":
    pygame.init()
    app = wx.App()
    gioco = Gioco()
    app.MainLoop()

    #pyinstaller --onefile -w file.py
    #NSIS
