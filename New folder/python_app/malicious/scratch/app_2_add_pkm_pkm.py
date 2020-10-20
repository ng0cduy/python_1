from library.sql_lib import *
from GUI.test_GUI_2 import *
from library.poke_view import *
app = wx.App()
frame = wx.Frame(None, title="Add Pokemon",size=(420,430))
panel = panel2_update_pkm(frame,-1)
frame.Show(True)
app.MainLoop()