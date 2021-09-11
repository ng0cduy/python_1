#delete_pokemon
from GUI.test_GUI_4 import *
from library.sql_lib import *
from library.poke_view import *
app = wx.App()
frame = wx.Frame(None, title="Delete pokemon",pos = (-1,-1),size=(420,320))
panel = panel4_del_pkm(frame,-1)
frame.Show(True)
app.MainLoop()