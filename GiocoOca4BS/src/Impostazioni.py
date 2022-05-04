import wx
class finestraImpostazioni(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Giochi dei Paesaggi di Giacomo - Impostazioni")
        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.panel.SetBackgroundColour((40,40,40))
        self.panel.SetForegroundColour("white")
        testo = wx.StaticText(self.panel, label = "Tema: ")
        self.combo = wx.ComboBox(self.panel, choices = ["Chiaro", "Scuro"],style = wx.CB_READONLY)
        self.combo.SetStringSelection("Scuro")
        hbox.Add(testo, proportion = 0, flag = wx.ALL, border = 5)
        hbox.Add(self.combo, proportion = 1, flag = wx.ALL|wx.ALIGN_CENTRE, border = 5)
        vbox.Add(hbox, proportion = 0, flag = wx.EXPAND|wx.ALL, border = 5)
        
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        testo2 = wx.StaticText(self.panel, label = "Traccia audio:")
        self.list = wx.ListBox(self.panel, choices = ["Aria sulla quarta corda", "Inverno", "Palladio", "Lacrimosa", ""])
        hbox.Add(testo2, proportion = 0, flag = wx.ALL, border = 5)
        hbox.Add(self.list, proportion = 1, flag = wx.ALL|wx.EXPAND, border = 5)
        vbox.Add(hbox, proportion = 0, flag = wx.EXPAND|wx.ALL, border = 5)

        self.panel.SetSizer(vbox)
        self.Refresh()
        return
        
    

if __name__ == "__main__":
    app = wx.App()
    window = finestraImpostazioni()
    window.Show()
    app.MainLoop()
        
    