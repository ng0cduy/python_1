# finding Pokemon by name
from GUI.test_GUI_3 import *
from library.sql_lib import *
from library.poke_view import *
app = wx.App()
frame = wx.Frame(None, title="Find Pokemon",pos = (-1,-1),size=(1000,600))
panel = panel3_find_pkm(frame,-1)
frame.Show(True)
app.MainLoop()