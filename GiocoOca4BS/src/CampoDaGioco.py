import wx, finestraStatistiche

class CampoDaGioco(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Campo Da Gioco - Preview")
        #E' una schermata di prova, il campo da gioco effettivo verrà visualizzato una volta eseguito il file 'Gioco.py'
        panel = wx.Panel(self)
        panel.SetOwnBackgroundColour((40, 40, 40))
        box = wx.BoxSizer(wx.HORIZONTAL)
        bmp = wx.Bitmap("../tabellone/fileCampoDaGiocoRid.png")
        self.viewer = wx.StaticBitmap(panel, bitmap=bmp)
        box.Add(self.viewer, proportion=1, flag=wx.ALL, border=5)

        vboxLaterale = wx.BoxSizer(wx.VERTICAL)
        font = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        # i trattini sono solo per estetica, niente di più
        testoSpazio = wx.StaticText(panel, label="------------------------")
        testoSpazio.SetFont(font)
        testoSpazio.Disable()
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(testoSpazio, proportion=0, flag=wx.ALL | wx.ALIGN_TOP)
        vboxLaterale.Add(hbox, proportion=0, flag=wx.ALL, border=0)

        #sezione relativa alle icone dei giocatori dei turni successivi
        hboxTurni = wx.BoxSizer(wx.HORIZONTAL)
        self.viewerTurno1 = wx.StaticBitmap(panel,bitmap = wx.Bitmap())
        self.viewerTurno2 = wx.StaticBitmap(panel,bitmap = wx.Bitmap())
        self.viewerTurno3 = wx.StaticBitmap(panel,bitmap = wx.Bitmap())
        hboxTurni.Add(self.viewerTurno1,proportion = 0,flag = wx.ALL|wx.ALIGN_CENTER,border = 5)
        hboxTurni.Add(self.viewerTurno2,proportion = 0,flag = wx.ALL|wx.ALIGN_CENTER,border = 5)
        hboxTurni.Add(self.viewerTurno3,proportion = 0,flag = wx.ALL|wx.ALIGN_CENTER,border = 5)
        vboxLaterale.Add(hboxTurni,proportion = 1,flag = wx.EXPAND)


        bmp = wx.Bitmap()
        self.viewerIconPlayerTurno = wx.StaticBitmap(panel, bitmap=bmp)
        self.viewerIconPlayerTurno.SetSize((100,100))
        vboxLaterale.Add(self.viewerIconPlayerTurno, proportion=1, flag=wx.ALL|wx.ALIGN_CENTER, border=5)

        self.testoTurno = wx.StaticText(panel, label="_PLAYER_")
        self.testoTurno.SetFont(font)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.testoTurno, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        vboxLaterale.Add(hbox, proportion=1, flag=wx.ALL | wx.ALIGN_CENTER, border=15)

        # vboxLaterale.Add((-1,60))A
        self.PGiocaTurno = wx.Button(panel, label="GIOCA")
        self.PGiocaTurno.SetFont(font)
        vboxLaterale.Add(self.PGiocaTurno, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)

        # spazio per l'icona del dado
        bmp = wx.Bitmap()
        vboxLaterale.Add((-1,10))
        self.viewerDado = wx.StaticBitmap(panel, bitmap=bmp)
        self.viewerDado.SetSize((100,100))
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.viewerDado,proportion = 0,flag = wx.ALIGN_CENTER)
        vboxLaterale.Add(vbox, proportion=1, flag=wx.LEFT|wx.RIGHT, border=33)

        # spazio per l'icona che da l'esito della risposta
        vboxLaterale.Add((-1,30))
        bmp = wx.Bitmap()
        self.viewerIconaEsito = wx.StaticBitmap(panel,bitmap = bmp)
        self.viewerIconaEsito.SetSize((100,100))
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox2.Add(self.viewerIconaEsito,proportion = 0,flag = wx.ALIGN_CENTER)
        vboxLaterale.Add(vbox2,proportion = 1,flag = wx.LEFT|wx.RIGHT,border = 33)


        hbox = wx.BoxSizer(wx.HORIZONTAL)
        testoSpazio = wx.StaticText(panel, label="------------------------")
        testoSpazio.SetFont(font)
        testoSpazio.Disable()
        hbox.Add(testoSpazio, proportion=0, flag=wx.ALL | wx.ALIGN_BOTTOM)
        vboxLaterale.Add(hbox, proportion=1, flag=wx.ALL, border=0)
        box.Add(vboxLaterale, proportion=0, flag=wx.ALL | wx.EXPAND, border=5)
        #la schermata non può essere ridimensionata poichè altrimenti si andrebbe a perdere le coordinate a cui vanno inserite le icone dei giocatori
        self.SetMinSize((1280, 720))
        self.SetMaxSize((1280, 720))
        panel.SetSizer(box)
        self.SetIcon(wx.Icon("../icone/iconaInfinito.ico"))
        self.Bind(wx.EVT_CLOSE,self.close)

    def calcolaClassifica(self,giocatori):
        #data una lista di giocatori, ne calcola la classifica in base alla posizione
        classifica = []
        classificapos = []
        for player in giocatori:
            classificapos.append(player.posizione)
        classificapos.sort()
        classificapos.reverse()
        for n in classificapos:
            if classificapos.count(n) > 1:
                classificapos.remove(n)
        for n in classificapos:
            for player in giocatori:
                if player.posizione == n:
                    classifica.append(player)
        return classifica
    
    def finale(self,giocatori):
        #finale è la funzione che viene eseguita dall'interno del file Gioco una volta che un giocatore ha superato la casella N°42
        #consiste nel cancellare tutti gli attributi precedenti di questa classe per andare a creare una "nuova" finestra seppur è sempre la stessa
        self.DestroyChildren()
        panel2 = wx.Panel(self)
        panel2.SetBackgroundColour((40,40,40))
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.classifica = self.calcolaClassifica(giocatori)
        vincitore = self.classifica[0].nome
        testo = wx.StaticText(panel2,label = "HAI VINTO!\n" + vincitore,style = wx.ALIGN_CENTER)
        testo.SetForegroundColour("white")
        font40 = wx.Font(40, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        testo.SetFont(font40)
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        vbox.Add(testo,proportion = 1,flag = wx.ALL|wx.ALIGN_CENTER,border = 5)
        conta = 0
        vboxClassifica = wx.BoxSizer(wx.VERTICAL)
        for player in self.classifica:
            conta+=1
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            testo = wx.StaticText(panel2,label = str(conta)+"°: "+ player.nome)
            testo.SetForegroundColour("white")
            testo.SetFont(font20)
            hbox.Add(testo,proportion = 1,flag = wx.ALL,border = 5)
            bitmap = wx.Bitmap(player.iconPath)
            viewer = wx.StaticBitmap(panel2, bitmap=bitmap)
            hbox.Add(viewer,proportion = 1,flag = wx.ALL,border = 5)
            vboxClassifica.Add(hbox,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
        vbox.Add(vboxClassifica,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
        self.pulsanteInfo = wx.Button(panel2,label = "Statistiche")
        self.pulsanteRigioca = wx.Button(panel2,label = "Rigioca")
        self.pulsanteChiudi = wx.Button(panel2,label = "Chiudi")
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.pulsanteInfo,proportion = 1,flag = wx.ALL,border = 5)
        hbox.Add(self.pulsanteRigioca,proportion = 1,flag = wx.ALL,border = 5)
        hbox.Add(self.pulsanteChiudi,proportion = 1,flag = wx.ALL,border = 5)
        vbox.Add(hbox,proportion = 0,flag = wx.ALL|wx.EXPAND,border = 5)
        self.pulsanteInfo.Bind(wx.EVT_BUTTON,self.finestraStatistiche)
        panel2.SetSizer(vbox)
        self.SetMinSize((536, 678))
        self.SetMaxSize((750,730))
        self.SetIcon(wx.Icon("../icone/iconaInfinito.ico"))
        self.SetSize((670,679))
        return
    
    def finestraStatistiche(self,event):
        # è necessario ciò affinchè venga creata al massimo una finestra statistiche (probabile bug)
        try:
            self.a.Close()
        except AttributeError:
            self.a = finestraStatistiche.Statistiche(self.classifica)
        finally:
            self.a.Show()
        return

    def close(self,event):
        self.Destroy()
        quit()
        #print(self.GetSize())
        #self.testoTurno.SetLabel("O")
        #self.Destroy()
        return

if __name__ == "__main__":
    app = wx.App()
    window = CampoDaGioco()
    window.Show()
    app.MainLoop()
