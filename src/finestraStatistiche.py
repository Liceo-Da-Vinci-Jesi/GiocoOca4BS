import wx

class Statistiche(wx.Frame):
    def __init__(self,classifica):
        super().__init__(None, title="Campo Da Gioco - Preview")
        panel = wx.Panel(self)
        self.SetTitle("Statistiche")
        box = wx.BoxSizer(wx.VERTICAL)
        font20 = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        panel.SetBackgroundColour((40,40,40))
        add = False
        for n in classifica:
            if add:
                box.Add((-1,40))
            vbox = wx.BoxSizer(wx.VERTICAL)
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            nome = wx.StaticText(panel,label = n.nome+": ")
            nome.SetFont(font20)
            nome.SetForegroundColour("white")
            posiz = wx.StaticText(panel,label = "Posizionamento: "+str(classifica.index(n)+1) + "°")
            posiz.SetFont(font20)
            posiz.SetForegroundColour("white")
            posizione = wx.StaticText(panel,label = "Posizione Finale: "+str(n.posizione))
            posizione.SetFont(font20)
            posizione.SetForegroundColour("white")
            hbox.Add(nome,proportion = 1,flag = wx.ALL,border = 5)
            hbox.Add(posiz,proportion = 1,flag = wx.ALL,border = 5)
            hbox.Add(posizione,proportion = 1,flag = wx.ALL,border =5)
            vbox.Add(hbox,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 15)
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            rap = wx.StaticText(panel,label = "Corrette/Errate: "+str(n.corrette)+"/"+str(n.sbagliate))
            rap.SetFont(font20)
            rap.SetForegroundColour("white")
            hbox.Add(rap,proportion = 1,flag = wx.ALL,border = 5)
            bitmap = wx.Bitmap(n.iconPath)
            bitmap.SetSize((50,50))
            viewer = wx.StaticBitmap(panel, bitmap=bitmap)
            hbox.Add(viewer,proportion = 1,flag = wx.ALL,border = 5)
            vbox.Add(hbox,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
            box.Add(vbox,proportion = 1,flag = wx.ALL,border = 10)
            if not add:
                add = True
        panel.SetSizer(box)
        box.Fit(self)
        self.SetMinSize(self.GetSize())
        self.SetMaxSize(self.GetSize())


if __name__ == "__main__":
    app = wx.App()
    window = Statistiche()
    window.Show()
    app.MainLoop()