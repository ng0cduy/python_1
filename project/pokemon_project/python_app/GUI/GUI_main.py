# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from library.poke_view import *
from GUI.test_GUI_1 import * #view pkm list
from GUI.test_GUI_2 import * #add_pkm 
from GUI.test_GUI_3 import * #find_pkm
from GUI.test_GUI_4 import * #del_pkm
from GUI.test_GUI_5 import * #update_pkm
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.MDIParentFrame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"POKEMON ENCYCLOPEDIA", pos = wx.DefaultPosition, size = wx.Size( 1000,650 ), style = wx.CAPTION|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.menu_1 = wx.Menu()
		self.mnitem_view_pkm_list = wx.MenuItem( self.menu_1, wx.ID_ANY, u"Pokedex", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_1.Append( self.mnitem_view_pkm_list )

		self.mnitem_add_pkm = wx.MenuItem( self.menu_1, wx.ID_ANY, u"Add pokemon", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_1.Append( self.mnitem_add_pkm )

		self.mnitem_find_pkm = wx.MenuItem( self.menu_1, wx.ID_ANY, u"Find Pokemon", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_1.Append( self.mnitem_find_pkm )

		self.mnitem_del_pkm = wx.MenuItem( self.menu_1, wx.ID_ANY, u"Delete pokemon", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_1.Append( self.mnitem_del_pkm )

		self.mnitem_update_pkm = wx.MenuItem( self.menu_1, wx.ID_ANY, u"Update pokemon stat", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_1.Append( self.mnitem_update_pkm )

		self.m_menubar1.Append( self.menu_1, u"Function" )

		self.m_menu2 = wx.Menu()
		self.welcome = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Welcome", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.welcome )

		self.about = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.about )

		self.m_menubar1.Append( self.m_menu2, u"Help" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.mnitem_view_pkm_list_click, id = self.mnitem_view_pkm_list.GetId() )
		self.Bind( wx.EVT_MENU, self.mnitem_add_pkm_click, id = self.mnitem_add_pkm.GetId() )
		self.Bind( wx.EVT_MENU, self.mnitem_find_pkm_click, id = self.mnitem_find_pkm.GetId() )
		self.Bind( wx.EVT_MENU, self.mnitem_del_pkm_click, id = self.mnitem_del_pkm.GetId() )
		self.Bind( wx.EVT_MENU, self.mnitem_update_pkm_click, id = self.mnitem_update_pkm.GetId() )
		self.Bind( wx.EVT_MENU, self.welcome_click, id = self.welcome.GetId() )
		self.Bind( wx.EVT_MENU, self.about_click, id = self.about.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def mnitem_view_pkm_list_click( self, event ):
		title_name ="List Pokemon"
		children_list = self.GetChildren()
		for children in children_list:
			if children.GetTitle()==title_name:
				children.Activate()
				return
		poke1 = Pokemon("database/pokeinfo.db")
		poke1_exe = poke1.read_poke_info()
		app = wx.App()
		frame = wx.MDIChildFrame(self, pos = (0,0),title="List Pokemon",size=(980,600))
		panel = MyPanel1(frame,-1)
		list_ = panel.list_ctrl_view
		list_.InsertColumn(0, 'ID',wx.LIST_FORMAT_RIGHT, width = 105)
		list_.InsertColumn(1, 'Name', wx.LIST_FORMAT_LEFT, 250)
		list_.InsertColumn(2, 'Type', wx.LIST_FORMAT_LEFT, 105)
		list_.InsertColumn(3, 'HP', wx.LIST_FORMAT_RIGHT, 105)
		list_.InsertColumn(4, 'Attack', wx.LIST_FORMAT_RIGHT, 105)
		list_.InsertColumn(5, 'Defense', wx.LIST_FORMAT_RIGHT, 105)
		list_.InsertColumn(6, 'Speed', wx.LIST_FORMAT_RIGHT, 105)
		for i in poke1_exe:
			index = list_.GetItemCount()
			list_.InsertItem(index,str(i["ID"]))
			list_.SetItem(index = index,column = 1,label = i["Name"])
			list_.SetItem(index,2,i["Type"])
			list_.SetItem(index,3,str(i["HP"]))
			list_.SetItem(index,4,str(i["Attack"]))
			list_.SetItem(index,5,str(i["Defense"]))
			list_.SetItem(index,6,str(i["Speed"]))
		frame.Show(True)
		app.MainLoop()
		poke1.disconnect()

	def mnitem_add_pkm_click( self, event ):
		title_name ="Add Pokemon"
		children_list = self.GetChildren()
		for children in children_list:
			if children.GetTitle()==title_name:
				children.Activate()
				return
		app = wx.App()
		frame = wx.MDIChildFrame(self, title="Add Pokemon",pos=(0,0),size=(420,430))
		panel = panel2_update_pkm(frame,-1)
		frame.Show(True)
		app.MainLoop()

	def mnitem_find_pkm_click( self, event ):
		title_name ="Find Pokemon"
		children_list = self.GetChildren()
		for children in children_list:
			if children.GetTitle()==title_name:
				children.Activate()
				return
		app = wx.App()
		frame = wx.MDIChildFrame(self, title="Find Pokemon",pos = (0,0),size=(980,600))
		panel = panel3_find_pkm(frame,-1)
		frame.Show(True)
		app.MainLoop()

	def mnitem_del_pkm_click( self, event ):
		title_name ="Delete pokemon"
		children_list = self.GetChildren()
		for children in children_list:
			if children.GetTitle()==title_name:
				children.Activate()
				return
		app = wx.App()
		frame = wx.MDIChildFrame(self, title="Delete pokemon",pos = (0,0),size=(420,320))
		panel = panel4_del_pkm(frame,-1)
		frame.Show(True)
		app.MainLoop()

	def mnitem_update_pkm_click( self, event ):
		title_name ="Update pokemon Stat"
		children_list = self.GetChildren()
		for children in children_list:
			if children.GetTitle()==title_name:
				children.Activate()
				return
		app = wx.App()
		frame = wx.MDIChildFrame(self, title="Update pokemon stat",pos = (0,0),size=(620,520))
		panel = panel5_update_pkm_info(frame,-1)
		frame.Show(True)
		app.MainLoop()

	def welcome_click( self, event ):
		event.Skip()

	def about_click( self, event ):
		event.Skip()