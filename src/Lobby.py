import wx, Domanda
from PIL import Image

class Lobby(wx.Frame):
    def __init__(self,listaIconeDisponibili):
        super().__init__(None, title="Lobby")
        self.listaIcone = listaIconeDisponibili
        self.giocatori = []
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridSizer(rows = 2,cols = 4, vgap=0, hgap=0)
        
        panel.SetOwnBackgroundColour((40,40,40))
        font13Norm = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        font9Norm = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        font25Bold = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        ToggleButton1=wx.ToggleButton(panel, label="Giocatore 1",id = 1)
        ToggleButton1.Bind(wx.EVT_TOGGLEBUTTON,self.sbloccaStato)
        ToggleButton1.SetFont(font13Norm)
        grid.Add(ToggleButton1,proportion = 0, flag=wx.ALL | wx.EXPAND, border=5)
        
        ToggleButton2=wx.ToggleButton(panel, label="Giocatore 2",id = 2)
        ToggleButton2.Bind(wx.EVT_TOGGLEBUTTON, self.sbloccaStato)
        ToggleButton2.SetFont(font13Norm)
        grid.Add(ToggleButton2,proportion = 0, flag=wx.ALL | wx.EXPAND, border=5)
        
        ToggleButton3=wx.ToggleButton(panel, label="Giocatore 3",id = 3)
        ToggleButton3.Bind(wx.EVT_TOGGLEBUTTON, self.sbloccaStato)
        ToggleButton3.SetFont(font13Norm)
        grid.Add(ToggleButton3,proportion = 0, flag=wx.ALL | wx.EXPAND, border=5)
        
        ToggleButton4=wx.ToggleButton(panel, label="Giocatore 4",id = 4)
        ToggleButton4.Bind(wx.EVT_TOGGLEBUTTON, self.sbloccaStato)
        ToggleButton4.SetFont(font13Norm)
        grid.Add(ToggleButton4,proportion = 0, flag=wx.ALL | wx.EXPAND, border=5)
        
        textCtrl1 = wx.TextCtrl(panel,style = wx.TE_CENTRE|wx.TEXT_ALIGNMENT_CENTER)
        textCtrl1.SetFont(font9Norm)
        grid.Add(textCtrl1, proportion=0, flag =wx.ALL|wx.EXPAND, border=5)
       
        textCtrl2 = wx.TextCtrl(panel,style = wx.TE_CENTRE|wx.TEXT_ALIGNMENT_CENTER)
        textCtrl2.SetFont(font9Norm)
        grid.Add(textCtrl2, proportion=0, flag =wx.ALL|wx.EXPAND, border=5)
        
        textCtrl3 = wx.TextCtrl(panel,style = wx.TE_CENTRE|wx.TEXT_ALIGNMENT_CENTER)
        textCtrl3.SetFont(font9Norm)
        grid.Add(textCtrl3, proportion=0, flag =wx.ALL|wx.EXPAND, border=5)
        
        textCtrl4 = wx.TextCtrl(panel,style = wx.TE_CENTRE|wx.TEXT_ALIGNMENT_CENTER)
        textCtrl4.SetFont(font9Norm)
        grid.Add(textCtrl4, proportion=0, flag =wx.ALL|wx.EXPAND, border=5)

        hbox=wx.BoxSizer(wx.HORIZONTAL)
        bitmap1 = wx.Bitmap(self.listaIcone[0])
        viewer1 = wx.StaticBitmap(panel,bitmap = bitmap1)
        hbox.Add(viewer1,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)

        bitmap2 = wx.Bitmap(self.listaIcone[1])
        viewer2 = wx.StaticBitmap(panel,bitmap = bitmap2)
        hbox.Add(viewer2,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)

        bitmap3 = wx.Bitmap(self.listaIcone[2])
        viewer3 = wx.StaticBitmap(panel,bitmap = bitmap3)
        hbox.Add(viewer3,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)

        bitmap4 = wx.Bitmap(self.listaIcone[3])
        viewer4 = wx.StaticBitmap(panel,bitmap = bitmap4)
        hbox.Add(viewer4,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)

        self.listaToggleButton = (ToggleButton1,ToggleButton2,ToggleButton3,ToggleButton4)
        self.listaTc = (textCtrl1,textCtrl2,textCtrl3,textCtrl4)
        self.listaViewer = (viewer1,viewer2,viewer3,viewer4)

        self.contaGiocatori = 0
        self.PIniziaPartita= wx.Button(panel, label="INIZIA PARTITA")
        self.PIniziaPartita.SetFont(font25Bold)
        vbox.Add(grid,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
        vbox.Add(hbox,proportion = 2,flag = wx.ALL|wx.EXPAND,border = 5)
        vbox.Add(self.PIniziaPartita,proportion = 1,flag =wx.ALL|wx.EXPAND, border=5)
        box.Add(vbox,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
        self.PIniziaPartita.Disable()
        panel.SetSizer(box)
        
        self.SetMinSize((685,350))
        self.SetSize((814,310))
        self.SetMaxSize((903,414))
        self.Centre()
        self.SetIcon(wx.Icon("../icone/iconaInfinito.ico"))
        self.Refresh()

        viewer1.SetBitmap(wx.Bitmap((100,100), depth=2))
        textCtrl1.Disable()
        viewer2.SetBitmap(wx.Bitmap((100,100), depth=2))
        textCtrl2.Disable()
        viewer3.SetBitmap(wx.Bitmap((100,100), depth=2))
        textCtrl3.Disable()
        viewer4.SetBitmap(wx.Bitmap((100,100), depth=2))
        textCtrl4.Disable()
    
    def sbloccaStato(self,event):
        self.Refresh()
        if self.listaToggleButton[event.GetId()-1].GetValue():
            self.contaGiocatori+=1
            self.listaViewer[event.GetId()-1].SetBitmap(wx.Bitmap(self.listaIcone[event.GetId()-1]))
            self.listaTc[event.GetId()-1].Enable()
            self.listaTc[event.GetId()-1].SetFocus()
        else:
            self.contaGiocatori-=1
            self.listaTc[event.GetId()-1].Disable()
            self.listaViewer[event.GetId()-1].SetBitmap(wx.Bitmap((100,100), depth=2))
        self.sbloccaTastoInizioPartita()
        self.Refresh()
        return
    
    def sbloccaTastoInizioPartita(self):
        if self.contaGiocatori >= 2:
            self.PIniziaPartita.Enable()
        else:
            self.PIniziaPartita.Disable()
        return


# ----------------------------------------
if __name__ == "__main__":
    app = wx.App()
    window = Lobby( ["../icone/iconaCandela-100.png" , "../icone/iconaGinestra-100.png" , "../icone/iconaPassero-100.png" , "../icone/iconaZibaldone-100.png"] )
    window.Show()
    app.MainLoop()
