import gioco
import wx

def run():
    app = wx.App()
    a = gioco.Gioco()
    return app.MainLoop()