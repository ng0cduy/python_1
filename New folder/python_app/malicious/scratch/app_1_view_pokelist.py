from GUI.test_GUI_1 import *
from library.sql_lib import *
from library.poke_view import *
# poke1 = Pokemon("database/pokeinfo.db")
# poke1_exe = poke1.read_poke_info()


# app = wx.App()
# frame = wx.Frame(None, pos=(-1,-1),title="List Pokemon",size=(1000,600))
# panel = MyPanel1(frame,-1)
# list_ = panel.list_ctrl_view
# list_.InsertColumn(0, 'ID',wx.LIST_FORMAT_RIGHT, width = 105)
# list_.InsertColumn(1, 'Name', wx.LIST_FORMAT_LEFT, 250)
# list_.InsertColumn(2, 'Type', wx.LIST_FORMAT_LEFT, 105)
# list_.InsertColumn(3, 'HP', wx.LIST_FORMAT_RIGHT, 105)
# list_.InsertColumn(4, 'Attack', wx.LIST_FORMAT_RIGHT, 105)
# list_.InsertColumn(5, 'Defense', wx.LIST_FORMAT_RIGHT, 105)
# list_.InsertColumn(6, 'Speed', wx.LIST_FORMAT_RIGHT, 105)
# for i in poke1_exe:
#     index = list_.GetItemCount()
#     list_.InsertItem(index,str(i["ID"]))
#     list_.SetItem(index = index,column = 1,label = i["Name"])
#     list_.SetItem(index,2,i["Type"])
#     list_.SetItem(index,3,str(i["HP"]))
#     list_.SetItem(index,4,str(i["Attack"]))
#     list_.SetItem(index,5,str(i["Defense"]))
#     list_.SetItem(index,6,str(i["Speed"]))
frame.Show(True)
app.MainLoop()
poke1.disconnect()