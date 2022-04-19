import wx, finestraStatistiche

class CampoDaGioco(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Campo Da Gioco - Preview")
        self.posizione1 = -1
        self.posizione2 = -1
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)
        bmp = wx.Bitmap("fileCampoDaGiocoRid.png")
        self.viewer = wx.StaticBitmap(panel, bitmap=bmp)
        box.Add(self.viewer, proportion=1, flag=wx.ALL, border=5)

        vboxLaterale = wx.BoxSizer(wx.VERTICAL)
        font = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        testoSpazio = wx.StaticText(panel, label="------------------------")
        testoSpazio.SetFont(font)
        testoSpazio.Disable()
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(testoSpazio, proportion=0, flag=wx.ALL | wx.ALIGN_TOP)
        vboxLaterale.Add(hbox, proportion=1, flag=wx.ALL, border=0)

        bmp = wx.Bitmap("iconaXverde-100.png")
        self.viewerIconPlayerTurno = wx.StaticBitmap(panel, bitmap=bmp)
        vboxLaterale.Add(self.viewerIconPlayerTurno, proportion=1, flag=wx.ALL|wx.ALIGN_CENTER, border=5)

        self.testoTurno = wx.StaticText(panel, label="_PLAYER_")
        self.testoTurno.SetFont(font)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.testoTurno, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        vboxLaterale.Add(hbox, proportion=1, flag=wx.ALL | wx.ALIGN_CENTER, border=15)

        # vboxLaterale.Add((-1,60))
        self.PGiocaTurno = wx.Button(panel, label="GIOCA")
        self.PGiocaTurno.SetFont(font)
        vboxLaterale.Add(self.PGiocaTurno, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)

        # vboxLaterale.Add((-1,60))
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.testoLancioDado = wx.StaticText(panel, label="Lancio del\ndado...", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.testoLancioDado.SetFont(font)
        hbox.Add(self.testoLancioDado, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        vboxLaterale.Add(hbox, proportion=1, flag=wx.ALL | wx.ALIGN_CENTER, border=5)

        # vboxLaterale.Add((-1,60))
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.testoDado = wx.StaticText(panel, label="0")
        self.testoDado.SetFont(font)
        hbox.Add(self.testoDado, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        vboxLaterale.Add(hbox, proportion=1, flag=wx.ALL | wx.ALIGN_CENTER, border=5)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        testoSpazio = wx.StaticText(panel, label="------------------------")
        testoSpazio.SetFont(font)
        testoSpazio.Disable()
        hbox.Add(testoSpazio, proportion=0, flag=wx.ALL | wx.ALIGN_BOTTOM)
        vboxLaterale.Add(hbox, proportion=1, flag=wx.ALL, border=0)
        box.Add(vboxLaterale, proportion=0, flag=wx.ALL | wx.EXPAND, border=5)
        self.SetMinSize((1280, 720))
        self.SetMaxSize((1280, 720))
        panel.SetSizer(box)

    def calcolaClassifica(self,giocatori):
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
        #print(classifica)
        return classifica
    
    def finale(self,giocatori):
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
            wx_image = wx.Image(player.icona75.size[0], player.icona75.size[1])
            wx_image.SetData(player.icona75.convert("RGB").tobytes())
            bitmap = wx.Bitmap(wx_image)
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
        self.SetMinSize((536, 508))
        self.SetMaxSize((837,793))
        self.SetSize((670,635))
        return
    
    def finestraStatistiche(self,event):
        a = finestraStatistiche.Statistiche(self.classifica)
        a.Show()
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