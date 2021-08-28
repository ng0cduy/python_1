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

###########################################################################
## Class panel3_find_pkm
###########################################################################

class panel3_find_pkm ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = (-1,-1), size = wx.Size( 980,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Find Pokemon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 30, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )

		bSizer3.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"Find with Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		gbSizer4.Add( self.m_staticText101, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtCtrl_find = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 800,-1 ), 0 )
		gbSizer4.Add( self.txtCtrl_find, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btn_find = wx.Button( self, wx.ID_ANY, u"Find_pkm", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.btn_find, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.lstCtrl_pkm = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 950,380 ), wx.LC_REPORT )
		gbSizer4.Add( self.lstCtrl_pkm, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer3.Add( gbSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		# Connect Events
		self.btn_find.Bind( wx.EVT_BUTTON, self.btn_find_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_find_click( self, event ):
		list_ = self.lstCtrl_pkm
		list_.ClearAll()
		pkm_link = Pokemon("database/pokeinfo.db")
		name = self.txtCtrl_find.GetValue()
		find_pkm_list = pkm_link.find_pkm(name)
		if (find_pkm_list !=[]):
			list_.InsertColumn(0, 'ID',wx.LIST_FORMAT_RIGHT, width = 105)
			list_.InsertColumn(1, 'Name', wx.LIST_FORMAT_LEFT, 250)
			list_.InsertColumn(2, 'Type', wx.LIST_FORMAT_LEFT, 105)
			list_.InsertColumn(3, 'HP', wx.LIST_FORMAT_RIGHT, 105)
			list_.InsertColumn(4, 'Attack', wx.LIST_FORMAT_RIGHT, 105)
			list_.InsertColumn(5, 'Defense', wx.LIST_FORMAT_RIGHT, 105)
			list_.InsertColumn(6, 'Speed', wx.LIST_FORMAT_RIGHT, 105)
			for i in find_pkm_list:
				index = list_.GetItemCount()
				list_.InsertItem(index,str(i[0]))
				list_.SetItem(index = index,column = 1,label = i[1])
				list_.SetItem(index,2,i[2])
				list_.SetItem(index,3,str(i[3]))
				list_.SetItem(index,4,str(i[4]))
				list_.SetItem(index,5,str(i[5]))
				list_.SetItem(index,6,str(i[6]))
		else:
			wx.MessageBox('Cannot find any pokemon','Notification',wx.OK|wx.ICON_INFORMATION)
		pkm_link.disconnect()
