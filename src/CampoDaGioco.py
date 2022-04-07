import wx

class CampoDaGioco(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Campo Da Gioco - Preview")
        self.grigliaPulsanti = []
        box = wx.BoxSizer(wx.HORIZONTAL)
        panel = wx.Panel(self)
        grid = wx.GridSizer(cols = 6,rows = 7,hgap = 5,vgap = 5)
        for n in range(1,43):
            puls = wx.Button(panel,label = str(n),id = n)
            grid.Add(puls,proportion = 1,flag = wx.ALL|wx.EXPAND)
            self.grigliaPulsanti.append(puls)
        box.Add(grid,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)

        vboxLaterale = wx.BoxSizer(wx.VERTICAL)
        font = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        testoSpazio = wx.StaticText(panel, label="------------------------")
        testoSpazio.SetFont(font)
        testoSpazio.Disable()
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(testoSpazio,proportion = 0,flag = wx.ALL|wx.ALIGN_TOP)
        vboxLaterale.Add(hbox, proportion=1, flag=wx.ALL, border=0)

        self.testoTurno = wx.StaticText(panel,label = "_PLAYER_")
        self.testoTurno.SetFont(font)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.testoTurno,proportion = 0,flag = wx.ALL|wx.ALIGN_CENTER_VERTICAL)
        vboxLaterale.Add(hbox,proportion = 1,flag = wx.ALL|wx.ALIGN_CENTER,border = 15)

        #vboxLaterale.Add((-1,60))
        self.PGiocaTurno = wx.Button(panel,label = "GIOCA")
        self.PGiocaTurno.SetFont(font)
        vboxLaterale.Add(self.PGiocaTurno,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)

        # vboxLaterale.Add((-1,60))
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.testoLancioDado = wx.StaticText(panel, label="Lancio del\ndado...",style = wx.ALIGN_CENTER_HORIZONTAL)
        self.testoLancioDado.SetFont(font)
        hbox.Add(self.testoLancioDado, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        vboxLaterale.Add(hbox, proportion=1, flag=wx.ALL | wx.ALIGN_CENTER, border=5)

        #vboxLaterale.Add((-1,60))
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.testoDado = wx.StaticText(panel,label = "0")
        self.testoDado.SetFont(font)
        hbox.Add(self.testoDado,proportion = 0,flag = wx.ALL|wx.ALIGN_CENTER_VERTICAL)
        vboxLaterale.Add(hbox,proportion = 1,flag = wx.ALL|wx.ALIGN_CENTER,border = 5)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        testoSpazio = wx.StaticText(panel, label="------------------------")
        testoSpazio.SetFont(font)
        testoSpazio.Disable()
        hbox.Add(testoSpazio,proportion = 0,flag = wx.ALL|wx.ALIGN_BOTTOM)
        vboxLaterale.Add(hbox, proportion=1, flag=wx.ALL, border=0)

        box.Add(vboxLaterale,proportion = 0,flag = wx.ALL|wx.EXPAND,border = 5)
        self.SetMinSize((1280,720))
        self.SetMaxSize((1280, 720))
        panel.SetSizer(box)
        #self.Bind(wx.EVT_CLOSE,self.close)
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