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
## Class panel2_update_pkm
###########################################################################

class panel2_update_pkm ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,420 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Add Pokemon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 14, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )

		bSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gbSizer3.Add( self.m_staticText3, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtCtrl_ID = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		gbSizer3.Add( self.txtCtrl_ID, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gbSizer3.Add( self.m_staticText4, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtCtrl_Name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		gbSizer3.Add( self.txtCtrl_Name, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gbSizer3.Add( self.m_staticText5, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtCtrl_Type = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		gbSizer3.Add( self.txtCtrl_Type, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"HP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gbSizer3.Add( self.m_staticText6, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtCtrl_HP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		gbSizer3.Add( self.txtCtrl_HP, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Attack", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gbSizer3.Add( self.m_staticText7, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtCtrl_Attack = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		gbSizer3.Add( self.txtCtrl_Attack, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Defense", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gbSizer3.Add( self.m_staticText8, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txtCtrl_Defense = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		gbSizer3.Add( self.txtCtrl_Defense, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Speed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		gbSizer3.Add( self.m_staticText9, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btn_update = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.btn_update, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.txtCtrl_Speed = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		gbSizer3.Add( self.txtCtrl_Speed, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer2.Add( gbSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		# Connect Events
		self.btn_update.Bind( wx.EVT_BUTTON, self.btn_update_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_update_click( self, event ):
		pkm_link = Pokemon("database/pokeinfo.db")
		type_tuple = ("Normal", "Fire", "Water", "Grass", "Flying", "Fighting","Poison","Electric","Ground","Rock","Psychic","Ice","Bug","Ghost","Steel","Dragon","Dark","Fairy","")
		ID = self.txtCtrl_ID.GetValue()
		name = self.txtCtrl_Name.GetValue()
		Type = self.txtCtrl_Type.GetValue()
		HP = self.txtCtrl_HP.GetValue()
		Atk =self.txtCtrl_Attack.GetValue()
		Def = self.txtCtrl_Defense.GetValue()
		Speed = self.txtCtrl_Speed.GetValue()
		id_list =[]
		name_list =[]
		for item in pkm_link.read_poke_info():
			id_list.append(item["ID"])
			name_list.append(str(item["Name"]).lower())
		# condition: valid ID -> valid name ->valid other stats
		if (int(ID) <=0 or int(ID) >id_list[-1]+1):
			wx.MessageBox('Invalid ID, please try again','Notification',wx.OK|wx.ICON_INFORMATION)
		elif (ID=="" or name ==""):
			wx.MessageBox('ID and name cannot be blank!','Notification',wx.OK|wx.ICON_INFORMATION)
		elif (ID in id_list or name.lower() in name_list):
			wx.MessageBox('Information in the list already, Please try another ID and name','Notification',wx.OK|wx.ICON_INFORMATION)
		elif (str(Type).capitalize().strip() not in type_tuple):
			wx.MessageBox('Type not valid','Notification',wx.OK|wx.ICON_INFORMATION)
		elif ((str(HP).isnumeric()==False and HP!="") or (str(Def).isnumeric()==False and Def!="" ) or (str(Atk).isnumeric()==False and Atk!="") or (str(Speed).isnumeric()==False and Speed!="")):
			wx.MessageBox('HP,Attack,Defense,Speed must be a number. Try again!','Notification',wx.OK|wx.ICON_INFORMATION)
		else:
			result = pkm_link.add_pkm(ID,name,Type,HP,Atk,Def,Speed)
			if (result!=0):
				self.txtCtrl_ID.SetValue(ID)
				self.txtCtrl_Name.SetValue("")
				self.txtCtrl_Type.SetValue("")
				self.txtCtrl_HP.SetValue("")
				self.txtCtrl_Attack.SetValue("")
				self.txtCtrl_Defense.SetValue("")
				self.txtCtrl_Speed.SetValue("")
				wx.MessageBox('Add pokemon successful','Notification', wx.OK|wx.ICON_INFORMATION)
			else:
				wx.MessageBox('Fail to add pokemon','Notification',wx.OK|wx.ICON_INFORMATION)
		pkm_link.disconnect()
