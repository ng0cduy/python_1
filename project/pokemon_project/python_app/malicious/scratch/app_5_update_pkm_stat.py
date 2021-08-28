from GUI.test_GUI_5 import *
from library.sql_lib import *
from library.poke_view import *
app = wx.App()
frame = wx.Frame(None, title="Update pokemon stat",pos = (-1,-1),size=(620,520))
panel = panel5_update_pkm_info(frame,-1)
frame.Show(True)
app.MainLoop()