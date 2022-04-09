import wx, Domanda
class Lobby(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Lobby")

        self.giocatori = []
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        #testo = wx.StaticText(panel,label = "SCEGLIERE IL NUMERO E I RISPETTIVI NOMI DEI GIOCATORI")
        #vbox.Add(testo,proportion=0,flag = wx.ALL|wx.ALIGN_CENTER,border = 15)
        bag = wx.GridBagSizer(vgap=4, hgap=5)
        
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
        
        textCtrl1 = wx.TextCtrl(panel,style = wx.TE_CENTRE)
        bag.Add(textCtrl1, pos=(2,0), flag =wx.ALL|wx.EXPAND, border=5)
       
        textCtrl2 = wx.TextCtrl(panel,style = wx.TE_CENTRE|wx.TE_MULTILINE|wx.TEXT_ALIGNMENT_CENTER)
        bag.Add(textCtrl2, pos=(2,1), flag =wx.ALL|wx.EXPAND, border=5)
        
        textCtrl3 = wx.TextCtrl(panel,style = wx.TE_CENTRE|wx.TE_MULTILINE|wx.TEXT_ALIGNMENT_CENTER)
        bag.Add(textCtrl3, pos=(2,2), flag =wx.ALL|wx.EXPAND, border=5)
        
        textCtrl4 = wx.TextCtrl(panel,style = wx.TE_CENTRE|wx.TE_MULTILINE|wx.TEXT_ALIGNMENT_CENTER)
        bag.Add(textCtrl4, pos=(2,3), flag =wx.ALL|wx.EXPAND, border=5)

        panel1 = wx.Panel(panel)
        panel1.SetOwnBackgroundColour((0,255, 0))
        bag.Add(panel1,pos = (1,0),flag = wx.ALL|wx.EXPAND,border = 5)

        panel2 = wx.Panel(panel)
        panel2.SetOwnBackgroundColour((255, 255, 0))
        bag.Add(panel2, pos=(1, 1), flag=wx.ALL | wx.EXPAND, border=5)

        panel3 = wx.Panel(panel)
        panel3.SetOwnBackgroundColour((0, 255, 255))
        bag.Add(panel3, pos=(1, 2), flag=wx.ALL | wx.EXPAND, border=5)

        panel4 = wx.Panel(panel)
        panel4.SetOwnBackgroundColour((255, 0, 255))
        bag.Add(panel4, pos=(1, 3), flag=wx.ALL | wx.EXPAND, border=5)

        self.listaToggleButton = (ToggleButton1,ToggleButton2,ToggleButton3,ToggleButton4)
        self.listaTc = (textCtrl1,textCtrl2,textCtrl3,textCtrl4)
        self.listaPanel = (panel1,panel2,panel3,panel4)

        self.contaGiocatori = 0
        self.PIniziaPartita= wx.Button(panel, label="INIZIA LA PARTITA")
        bag.Add(self.PIniziaPartita, pos=(4,0), span=(0,4),flag =wx.ALL|wx.EXPAND, border=5)
        self.PIniziaPartita.Disable()

        bag.AddGrowableCol(0)
        bag.AddGrowableCol(1)
        bag.AddGrowableCol(2)
        bag.AddGrowableCol(3)
        
        bag.AddGrowableRow(0)
        #bag.AddGrowableRow(2)
        bag.AddGrowableRow(1)
        bag.AddGrowableRow(4)
        vbox.Add(bag,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
        panel.SetSizer(vbox)
        self.SetMinSize((1000,500))
        self.SetMaxSize((1000,500))
        self.Centre()
        self.Bind(wx.EVT_CLOSE,self.nonChiudere)

        panel1.Hide()
        textCtrl1.Disable()
        panel2.Hide()
        textCtrl2.Disable()
        panel3.Hide()
        textCtrl3.Disable()
        panel4.Hide()
        textCtrl4.Disable()
    def nonChiudere(self,event):
        self.Destroy()
        return
    def sbloccaStato(self,event):
        if self.listaToggleButton[event.GetId()-1].GetValue():
            self.contaGiocatori+=1
            self.listaTc[event.GetId()-1].Enable()
            self.listaPanel[event.GetId()-1].Show()
        else:
            self.contaGiocatori-=1
            self.listaTc[event.GetId()-1].Disable()
            self.listaPanel[event.GetId()-1].Hide()
        self.sbloccaTastoInizioPartita()
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
    window = Lobby()
    window.Show()

    app.MainLoop()
    print(window.giocatori)
