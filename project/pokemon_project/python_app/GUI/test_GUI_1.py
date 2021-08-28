# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 980,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.list_ctrl_view = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size(950,580), wx.LC_REPORT )
		bSizer1.Add( self.list_ctrl_view, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

	def __del__( self ):
		pass


