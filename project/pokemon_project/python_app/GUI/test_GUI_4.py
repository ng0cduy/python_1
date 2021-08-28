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
## Class panel4_del_pkm
###########################################################################

class panel4_del_pkm ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Delete Pokemon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )

		bSizer4.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gbSizer3.Add( self.m_staticText12, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txt_ctrl_ID_del = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		gbSizer3.Add( self.txt_ctrl_ID_del, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btn_del = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.btn_del, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( gbSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		# Connect Events
		self.btn_del.Bind( wx.EVT_BUTTON, self.btn_del_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_del_click( self, event ):
		pkm_link = Pokemon("database/pokeinfo.db")
		ID = str(self.txt_ctrl_ID_del.GetValue())
		id_list =[]
		for item in pkm_link.read_poke_info():
			id_list.append(str(item["ID"]))
		if (ID ==""):
			wx.MessageBox('Fail to delete pokemon, add ID please','Notification',wx.OK|wx.ICON_INFORMATION)
		elif (ID not in id_list):
			wx.MessageBox("No ID available in the list to delete",'Notification',wx.OK|wx.ICON_INFORMATION)
		elif (ID in id_list):
			pkm_link.del_pkm(ID)
			wx.MessageBox("Delete Pokemon successful",'Notification',wx.OK|wx.ICON_INFORMATION)
		pkm_link.disconnect()
