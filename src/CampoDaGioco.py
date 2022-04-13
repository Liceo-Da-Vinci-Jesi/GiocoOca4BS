import wx

class CampoDaGioco(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Campo Da Gioco - Preview")
        self.posizione1 = -1
        self.posizione2 = -1
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)
        bmp = wx.Bitmap("FileCampoDaGiocoRid.png")
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

        bmp = wx.Bitmap("iconaXverde-24.png")
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

    def close(self,event):
        self.Destroy()
        #print(self.GetSize())
        #self.testoTurno.SetLabel("O")
        #self.Destroy()
        return

if __name__ == "__main__":
    app = wx.App()
    window = CampoDaGioco()
    window.Show()
    app.MainLoop()