import random
import wx

# ---------------------------------
import os
module_dir = os.path.dirname(__file__)
# ---------------------------------

class Lobby(wx.Frame):
    
    def __init__(self,listaIconeDisponibili):
        super().__init__(None, title="Giochi dei Paesaggi di Giacomo")
        self.giocatori = []
        self.listaIcone = listaIconeDisponibili
        self.panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridSizer(rows = 2,cols = 4, vgap=0, hgap=0)
        
        self.panel.SetBackgroundColour((40,40,40))
        font13Norm = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        font25Bold = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        font13Bold = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.BOLD)

        self.listaToggleButton = []
        self.listaTc = []
        self.listaViewer = []

        #creazione e gestione dei vari elementi:
        #pulsanti(togglebutton)
        listaColori = [(249,194,68),(241,105,99),(73,154,200),(66,215,132)]
        random.shuffle(listaColori)
        for n in range(1,5):
            ToggleButton=wx.ToggleButton(self.panel, label="Giocatore "+str(n),id = n)
            ToggleButton.Bind(wx.EVT_TOGGLEBUTTON,self.sbloccaStato)
            ToggleButton.SetFont(font13Norm)
            grid.Add(ToggleButton,proportion = 0, flag=wx.ALL | wx.EXPAND, border=5)
            ToggleButton.SetBackgroundColour(listaColori[n-1])
            self.listaToggleButton.append(ToggleButton)

        #textctrl
        for n in range(4):
            textCtrl = wx.TextCtrl(self.panel,style = wx.TE_CENTRE|wx.TEXT_ALIGNMENT_CENTER)
            textCtrl.SetFont(font13Norm)
            textCtrl.Disable()
            grid.Add(textCtrl, proportion=0, flag =wx.ALL|wx.EXPAND, border=5)
            self.listaTc.append(textCtrl)

        #icone
        hbox=wx.BoxSizer(wx.HORIZONTAL)
        for n in self.listaIcone:
            img = wx.Bitmap(n).ConvertToDisabled()
            viewer = wx.StaticBitmap(self.panel,bitmap = wx.Bitmap(img))
            viewer.SetSize((100,100))
            self.listaViewer.append(viewer)
            hbox.Add(viewer,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)


        vbox.Add(grid,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
        vbox.Add(hbox,proportion = 2,flag = wx.ALL|wx.EXPAND,border = 5)
        self.contaGiocatori = 0
        hbox = wx.BoxSizer(wx.VERTICAL)
        self.PImpostazioni= wx.Button(self.panel, label = "IMPOSTAZIONI")
        self.PIniziaPartita= wx.Button(self.panel, label="INIZIA PARTITA")
        self.PIniziaPartita.SetFont(font25Bold)
        self.PImpostazioni.SetFont(font13Bold)
        hbox.Add(self.PIniziaPartita, proportion = 2, flag = wx.EXPAND|wx.ALL, border = 5)
        hbox.Add(self.PImpostazioni, proportion = 1, flag = wx.EXPAND|wx.ALL, border = 5)
        vbox.Add(hbox,proportion = 1,flag =wx.ALL|wx.EXPAND, border=5)
        box.Add(vbox,proportion = 1,flag = wx.ALL|wx.EXPAND,border = 5)
        self.PIniziaPartita.Disable()
        self.panel.SetSizer(box)
        
        self.SetMinSize((685,350))
        self.SetSize((814,380))
        self.SetMaxSize((903,414))
        self.Centre()
        self.SetIcon(wx.Icon( os.path.join(module_dir,"icone/iconaInfinito.ico") ))

    def sbloccaStato(self,event):
        if self.listaToggleButton[event.GetId()-1].GetValue():
            self.contaGiocatori+=1
            self.listaViewer[event.GetId()-1].SetBitmap(wx.Bitmap(self.listaIcone[event.GetId()-1]))
            self.listaTc[event.GetId()-1].Enable()
            self.listaTc[event.GetId()-1].SetFocus()
        else:
            #quando un pulsante viene disattivato fa ritornare l'immagine corrispondente sulla scala dei grigi (ToDisabled)
            self.contaGiocatori-=1
            self.listaTc[event.GetId()-1].Disable()
            self.listaViewer[event.GetId()-1].SetBitmap(wx.Bitmap(self.listaIcone[event.GetId()-1]).ConvertToDisabled())
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
    window = Lobby( [ os.path.join(module_dir,"icone/iconaCandela-100.png") , os.path.join(module_dir,"icone/iconaGinestra-100.png") , os.path.join(module_dir,"icone/iconaPassero-100.png") , os.path.join(module_dir,"icone/iconaZibaldone-100.png") ] )
    window.Show()
    app.MainLoop()
