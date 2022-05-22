import sys
sys.path.append("GiocoDellOca4Bs/")

import random , time

import wx , wx.adv
import pygame , pygame.mixer
from PIL import Image
import Gioco, Domanda, Lobby , Casella, Giocatore, CampoDaGioco, ElencoDomande, datetime, Impostazioni

# 
pygame.init()
app = wx.App()
gioco = Gioco.Gioco()
app.MainLoop()
