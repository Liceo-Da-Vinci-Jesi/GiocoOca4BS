import wx, Domanda
from PIL import Image
class Lobby(wx.Frame):
    def __init__(self,listaIcone):
        super().__init__(None, title="Lobby")

        self.giocatori = []
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        bag = wx.GridBagSizer(vgap=5, hgap=5)
        
        panel.SetOwnBackgroundColour((40,40,40))
        
        ToggleButton1=wx.ToggleButton(panel, label="Giocatore 1",id = 1)
        ToggleButton1.Bind(wx.EVT_TOGGLEBUTTON,self.sbloccaStato)
        bag.Add(ToggleButton1, pos=(0,0), flag=wx.ALL | wx.EXPAND, border=5)
        
        ToggleButton2=wx.ToggleButton(panel, label="Giocatore 2",id = 2)
        ToggleButton2.Bind(wx.EVT_TOGGLEBUTTON, self.sbloccaStato)
        bag.Add(ToggleButton2, pos=(0,1), flag=wx.ALL | wx.EXPAND, border=5)
        
        ToggleButton3=wx.ToggleButton(panel, label="Giocatore 3",id = 3)
        ToggleButton3.Bind(wx.EVT_TOGGLEBUTTON, self.sbloccaStato)
        bag.Add(ToggleButton3, pos=(0,2), flag=wx.ALL | wx.EXPAND, border=5)
        
        ToggleButton4=wx.ToggleButton(panel, label="Giocatore 4",id = 4)
        ToggleButton4.Bind(wx.EVT_TOGGLEBUTTON, self.sbloccaStato)
        bag.Add(ToggleButton4, pos=(0,3), flag=wx.ALL | wx.EXPAND, border=5)
        
        textCtrl1 = wx.TextCtrl(panel,style = wx.TE_CENTRE|wx.TEXT_ALIGNMENT_CENTER)
        bag.Add(textCtrl1, pos=(1,0), flag =wx.ALL|wx.EXPAND, border=5)
       
        textCtrl2 = wx.TextCtrl(panel,style = wx.TE_CENTRE|wx.TEXT_ALIGNMENT_CENTER)
        bag.Add(textCtrl2, pos=(1,1), flag =wx.ALL|wx.EXPAND, border=5)
        
        textCtrl3 = wx.TextCtrl(panel,style = wx.TE_CENTRE|wx.TEXT_ALIGNMENT_CENTER)
        bag.Add(textCtrl3, pos=(1,2), flag =wx.ALL|wx.EXPAND, border=5)
        
        textCtrl4 = wx.TextCtrl(panel,style = wx.TE_CENTRE|wx.TEXT_ALIGNMENT_CENTER)
        bag.Add(textCtrl4, pos=(1,3), flag =wx.ALL|wx.EXPAND, border=5)

        bitmap1 = wx.Bitmap(listaIcone[0])
        viewer1 = wx.StaticBitmap(panel,bitmap = bitmap1)
        bag.Add(viewer1,pos = (2,0),flag = wx.ALL|wx.EXPAND,border = 5)

        bitmap2 = wx.Bitmap(listaIcone[1])
        viewer2 = wx.StaticBitmap(panel,bitmap = bitmap2)
        bag.Add(viewer2,pos = (2,1),flag = wx.ALL|wx.EXPAND,border = 5)

        bitmap3 = wx.Bitmap(listaIcone[2])
        viewer3 = wx.StaticBitmap(panel,bitmap = bitmap3)
        bag.Add(viewer3,pos = (2,2),flag = wx.ALL|wx.EXPAND,border = 5)

        bitmap4 = wx.Bitmap(listaIcone[3])
        viewer4 = wx.StaticBitmap(panel,bitmap = bitmap4)
        bag.Add(viewer4,pos = (2,3),flag = wx.ALL|wx.EXPAND,border = 5)

        self.listaToggleButton = (ToggleButton1,ToggleButton2,ToggleButton3,ToggleButton4)
        self.listaTc = (textCtrl1,textCtrl2,textCtrl3,textCtrl4)
        self.listaViewer = (viewer1,viewer2,viewer3,viewer4)

        self.contaGiocatori = 0
        self.PIniziaPartita= wx.Button(panel, label="INIZIA LA PARTITA")
        bag.Add(self.PIniziaPartita, pos=(3,0), span=(0,4),flag =wx.ALL|wx.EXPAND, border=5)
        self.PIniziaPartita.Disable()

        bag.AddGrowableCol(0)
        bag.AddGrowableCol(1)
        bag.AddGrowableCol(2)
        bag.AddGrowableCol(3)
        
        #bag.AddGrowableRow(0)
        bag.AddGrowableRow(2)
        bag.AddGrowableRow(3)
        vbox.Add(bag,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
        panel.SetSizer(vbox)
        self.SetMinSize((600,300))
        self.SetSize((800,400))
        self.SetMaxSize((1000,500))
        self.Centre()
        self.Refresh()
        self.Bind(wx.EVT_CLOSE,self.nonChiudere)

        viewer1.Hide()
        textCtrl1.Disable()
        viewer2.Hide()
        textCtrl2.Disable()
        viewer3.Hide()
        textCtrl3.Disable()
        viewer4.Hide()
        textCtrl4.Disable()
        #self.Bind(wx.EVT_SIZE,self.aggiustaScalaIcone)
    
    def aggiustaScalaIcone(self,evt):
        self.Refresh()
        for n in self.listaPanel:
            if type(n) == type(wx.StaticBitmap()):
                print("AA")
                n.SetScaleMode(1)
        return
    
    # PROF: Perché una funzione chiamata "nonChiudere" fa Destroy??? :)
    def nonChiudere(self,event):
        self.Destroy()
        return
    
    def sbloccaStato(self,event):
        self.Refresh()
        if self.listaToggleButton[event.GetId()-1].GetValue():
            self.contaGiocatori+=1
            self.listaViewer[event.GetId()-1].Show()
            self.listaTc[event.GetId()-1].Enable()
            self.listaTc[event.GetId()-1].SetFocus()
        else:
            self.contaGiocatori-=1
            self.listaTc[event.GetId()-1].Disable()
            self.listaViewer[event.GetId()-1].Hide()
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
    window = Lobby( ["iconaXverde-100.png" , "iconaXrosa-100.png" , "iconaXblu-100.png" , "iconaXgialla-100.png"] )
    window.Show()
    app.MainLoop()