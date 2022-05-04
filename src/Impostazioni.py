import wx, re

from pathlib import Path
class finestraImpostazioni(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Giochi dei Paesaggi di Giacomo - Impostazioni")
        self.panel = wx.Panel(self)

        font13Norm = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        font25Bold = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        font13Bold = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.BOLD)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.panel.SetBackgroundColour((40,40,40))
        self.panel.SetForegroundColour("white")
        testo = wx.StaticText(self.panel, label = "Tema: ")
        testo.SetFont(font25Bold)
        self.r1 = wx.RadioButton(self.panel, label = "Chiaro",style = wx.RB_GROUP)
        self.r1.SetFont(font13Bold)
        self.r2 = wx.RadioButton(self.panel, label = "Scuro")
        self.r2.SetFont(font13Bold)
        self.r2.SetValue(True)
        hbox.Add(testo, proportion = 0, flag = wx.ALL, border = 5)
        hbox.Add(self.r1, proportion = 1, flag = wx.ALL|wx.ALIGN_CENTRE, border = 5)
        hbox.Add(self.r2, proportion = 1, flag = wx.ALL|wx.ALIGN_CENTRE, border = 5)
        vbox.Add(hbox, proportion = 1, flag = wx.EXPAND|wx.ALL, border = 5)
        vbox.Add(wx.StaticLine(self.panel,size = (800,2)))
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        testo2 = wx.StaticText(self.panel, label = "Traccia audio:")
        testo2.SetFont(font25Bold)
        self.listaTesti = [testo, testo2, self.r1, self.r2]
        file = []
        o = str("\\")
        path = Path("../audio/Bg")
        for n in path.iterdir():
            if str(n).endswith(".mp3"):
                testo = str(n)
                testo = testo.replace(o,"o")
                testo = testo.replace("..oaudiooBgo","")
                testo = testo.replace(".mp3","")
                file.append(testo)
        self.list = wx.ListBox(self.panel, choices = file, style = wx.LB_ALWAYS_SB)
        self.list.SetFont(font13Norm)
        hbox.Add(testo2, proportion = 0, flag = wx.ALL, border = 5)
        hbox.Add(self.list, proportion = 1, flag = wx.ALL|wx.EXPAND, border = 5)


        vbox.Add(hbox, proportion = 2, flag = wx.EXPAND|wx.ALL, border = 5)
        self.pulsIndietro = wx.Button(self.panel,label = "Indietro")
        vbox.Add(self.pulsIndietro,proportion = 0,flag = wx.ALL|wx.ALIGN_RIGHT,border = 5)


        self.panel.SetSizer(vbox)
        vbox.Fit(self)
        self.SetMinSize((490,self.GetSize()[1]))
        self.SetSize((500,self.GetSize()[1]))
        self.SetMaxSize((590,self.GetSize()[1]+100))
        self.Refresh()
        self.SetIcon(wx.Icon("../icone/iconaInfinito.ico"))
        return



if __name__ == "__main__":
    app = wx.App()
    window = finestraImpostazioni()
    window.Show()
    app.MainLoop()
        
    