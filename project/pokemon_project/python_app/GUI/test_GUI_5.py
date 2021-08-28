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
## Class panel5_update_pkm_info
###########################################################################

class panel5_update_pkm_info ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 600,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Update pokemon Stat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Comic Sans MS" ) )

		bSizer5.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		gbSizer4.Add( self.m_staticText14, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txt_ctrl_ID = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		gbSizer4.Add( self.txt_ctrl_ID, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gbSizer4.Add( self.m_staticText15, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txt_ctrl_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		gbSizer4.Add( self.txt_ctrl_name, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.sta_txt_ctrl_type = wx.StaticText( self, wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sta_txt_ctrl_type.Wrap( -1 )

		gbSizer4.Add( self.sta_txt_ctrl_type, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txt_ctrl_type = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		gbSizer4.Add( self.txt_ctrl_type, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"HP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		gbSizer4.Add( self.m_staticText17, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txt_ctrl_HP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		gbSizer4.Add( self.txt_ctrl_HP, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Attack", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		gbSizer4.Add( self.m_staticText18, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txt_ctrl_atk = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		gbSizer4.Add( self.txt_ctrl_atk, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Defense", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		gbSizer4.Add( self.m_staticText19, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txt_ctrl_def = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		gbSizer4.Add( self.txt_ctrl_def, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Speed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		gbSizer4.Add( self.m_staticText20, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.txt_ctrl_speed = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		gbSizer4.Add( self.txt_ctrl_speed, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btn_update = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.btn_update, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer5.Add( gbSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		# Connect Events
		self.btn_update.Bind( wx.EVT_BUTTON, self.btn_update_click )

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def btn_update_click( self, event ):
		pkm_link = Pokemon("database/pokeinfo.db")
		type_tuple = ("Normal", "Fire", "Water", "Grass", "Flying", "Fighting","Poison","Electric","Ground","Rock","Psychic","Ice","Bug","Ghost","Steel","Dragon","Dark","Fairy","")
		id_list =[]
		name_list=[]
		for item in pkm_link.read_poke_info():
			id_list.append(str(item["ID"]))
			name_list.append(str(item["Name"]).lower())
		ID		= 	(self.txt_ctrl_ID.GetValue())
		name 	= 	(self.txt_ctrl_name.GetValue())
		type_ 	= 	(self.txt_ctrl_type.GetValue())
		hp 		=   (self.txt_ctrl_HP.GetValue())
		attack_ = 	(self.txt_ctrl_atk.GetValue())
		def_    = 	(self.txt_ctrl_def.GetValue())
		speed_  = 	(self.txt_ctrl_speed.GetValue())
		#if input none, keep old data
		if (str(name).strip().lower()=="none"):
			name=pkm_link.read_poke_info()[int(ID)-1]["Name"]
		if (str(type_).strip().lower()=="none"):
			type_=pkm_link.read_poke_info()[int(ID)-1]["Type"]
		if (str(hp).strip().lower()=="none"):
			hp=pkm_link.read_poke_info()[int(ID)-1]["HP"]
		if (str(attack_).strip().lower()=="none"):
			attack_=pkm_link.read_poke_info()[int(ID)-1]["Attack"]
		if (str(def_).strip().lower()=="none"):
			def_=pkm_link.read_poke_info()[int(ID)-1]["Defense"]
		if (str(speed_).strip().lower()=="none"):
			hp=pkm_link.read_poke_info()[int(ID)-1]["Speed"]
		#constrain: ID -> ->Name -> Type -> Stat
		if (ID ==""):
			wx.MessageBox('Fail to update pokemon stat, add ID please','Notification',wx.ICON_WARNING|wx.ICON_INFORMATION)
		elif(ID not in id_list):
			wx.MessageBox('ID not available to update','Notification',wx.ICON_WARNING|wx.ICON_INFORMATION)
		elif (str(name).strip()==""):
			wx.MessageBox('Name can not be blank, input name or input "none" to keep old name',style=wx.OK|wx.ICON_INFORMATION)
		elif (str(name).lower() in name_list and name_list.index(str(name).lower())!=int(ID)-1):
			wx.MessageBox('Name already exists',style=wx.ICON_WARNING|wx.ICON_INFORMATION)
		elif (str(type_).capitalize().strip() not in type_tuple):
			wx.MessageBox('Type not valid','Notification',wx.ICON_WARNING|wx.ICON_INFORMATION)
		elif ((str(hp).isnumeric()==False and hp!="") or (str(def_).isnumeric()==False and def_!="" ) or (str(attack_).isnumeric()==False and attack_!="") or (str(speed_).isnumeric()==False and speed_!="")):
			wx.MessageBox('HP,Attack,Defense,Speed must be a number. Try again!','Notification',wx.OK|wx.ICON_INFORMATION)
		else:
			result = pkm_link.update_pkm(ID,name,type_,hp,attack_,def_,speed_)
			if result !=0:
				wx.MessageBox('Update pokemon successfully','Notification',wx.OK|wx.ICON_INFORMATION)
				self.txt_ctrl_ID.SetValue("")
				self.txt_ctrl_name.SetValue("")
				self.txt_ctrl_type.SetValue("")
				self.txt_ctrl_HP.SetValue("")
				self.txt_ctrl_atk.SetValue("")
				self.txt_ctrl_def.SetValue("")
				self.txt_ctrl_speed.SetValue("")
			else:
				wx.MessageBox('Fail to update pokemon stat','Notification',wx.ICON_WARNING|wx.ICON_INFORMATION)
		pkm_link.disconnect()

