import wx

class Statistiche(wx.Frame):
    def __init__(self,classifica):
        super().__init__(None, title="Il gioco dei paesaggi di Giacomo - Statistiche")
        # per ogni giocatore (in ordine di classifica) ne va a "schematizzare" le statistiche principali
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        panel.SetBackgroundColour((40,40,40))
        for n in classifica:
            vbox = wx.BoxSizer(wx.VERTICAL)
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            testo = wx.StaticText(panel,label = n.nome+": \nPosizionamento: "+str(classifica.index(n)+1) + "°\nPosizione Finale: "+str(n.posizione)+ "\nCorrette/Errate: "+str(n.corrette)+"/"+str(n.sbagliate))
            vbox.Add(testo,proportion = 1,flag = wx.ALL,border = 5)
            testo.SetFont(font20)
            testo.SetForegroundColour("white")
            hbox.Add(vbox,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 15)
            bitmap = wx.Bitmap(n.iconPath)
            bitmap.SetSize((75,75))
            viewer = wx.StaticBitmap(panel, bitmap=bitmap)
            viewer.SetSize((75,75))
            hbox.Add(viewer,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 10)
            box.Add(hbox,proportion = 1,flag = wx.ALL,border = 10)
        panel.SetSizer(box)
        box.Fit(self)
        self.SetMinSize(self.GetSize())
        self.SetMaxSize(self.GetSize())
        self.SetIcon(wx.Icon("../icone/iconaInfinito.ico"))
        self.Bind(wx.EVT_CLOSE,self.nonChiudere)

    def nonChiudere(self,event):
        self.Hide()
        return


if __name__ == "__main__":
    app = wx.App()
    window = Statistiche()
    window.Show()
    app.MainLoop()
