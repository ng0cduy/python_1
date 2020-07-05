# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from thu_vien.xu_ly_chung import *
from thu_vien.c_Cong_ty import *
from thu_vien.c_NhanVien import *
from thu_vien.c_Nhom_Tivi import *
from thu_vien.c_TIVI import *
from giao_dien.gd_Bai_7_1 import *
from giao_dien.gd_Bai_7_2 import *
from giao_dien.gd_Bai_7_3 import *
from giao_dien.gd_Bai_7_4 import *
###########################################################################
## Class frame_main
###########################################################################

class frame_main ( wx.MDIParentFrame ):

    def __init__( self, parent ):
        wx.MDIParentFrame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar2 = wx.MenuBar( 0 )
        self.m_menu3 = wx.Menu()
        self.menuItem_login = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Đăng nhập", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.Append( self.menuItem_login )

        self.menuItem_logout = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Đăng xuất", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.Append( self.menuItem_logout )

        self.m_menubar2.Append( self.m_menu3, u"Thông Tin" )

        self.m_menu4 = wx.Menu()
        self.menuItem_tt_congty = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Thông tin công ty", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu4.Append( self.menuItem_tt_congty )

        self.menuItem_nhom_tv = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Nhóm Tivi", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu4.Append( self.menuItem_nhom_tv )

        self.menuItem_them_nv = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Thêm Nhân Viên", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu4.Append( self.menuItem_them_nv )

        self.menuItem_themTV = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Thêm Tivi", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu4.Append( self.menuItem_themTV )

        self.m_menubar2.Append( self.m_menu4, u"Chức năng" )

        self.SetMenuBar( self.m_menubar2 )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.menuItem_login_click, id = self.menuItem_login.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItem_logout_click, id = self.menuItem_logout.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItem_tt_congty_click, id = self.menuItem_tt_congty.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItem_nhom_tv_click, id = self.menuItem_nhom_tv.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItem9_them_nv_click, id = self.menuItem_them_nv.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItem_themTV_click, id = self.menuItem_themTV.GetId() )

    def __del__( self ):
    	pass


	# Virtual event handlers, overide them in your derived class
    def menuItem_login_click( self, event ):
    	event.Skip()

    def menuItem_logout_click( self, event ):
        event.Skip()

    def menuItem_tt_congty_click( self, event ):
        title_name = "Thông tin công ty"
        ds_children = self.GetChildren()
        for children in ds_children:
            if children.GetTitle()==title_name:
                children.Activate()
                return
        # khởi tạo đối tượng công ty
        xl_cong_ty = CongTy(duong_dan_cong_ty)
        ds_cong_ty = xl_cong_ty.doc_thong_tin_cong_ty()[0]
        app = wx.App()
        # wx.Frame => wx.MDICHildFrame , None =>self
        frame = wx.MDIChildFrame(self,title = "Thông tin công ty",size = (540,360))
        panel = panel_Bai_7_1(frame)
        panel.txt_ten.SetValue(ds_cong_ty['Ten'])
        panel.txt_ma_so.SetValue(ds_cong_ty['Ma_so'])
        panel.txt_dien_thoai.SetValue(ds_cong_ty['Dien_thoai'])
        panel.txt_dia_chi.SetValue(ds_cong_ty['Dia_chi'])
        panel.txt_email.SetValue(ds_cong_ty['Email'])
        frame.Show(True)
        app.MainLoop()
        xl_cong_ty.disconnect()
        
    def menuItem_nhom_tv_click( self, event ):
        title_name = "Nhóm Tivi"
        ds_children = self.GetChildren()
        for children in ds_children:
            if children.GetTitle()==title_name:
                children.Activate()
                return
        xl_nhom_tivi = NhomTivi(duong_dan_tivi)
        ds_nhom_tivi= xl_nhom_tivi.doc_danh_sach_nhom_tv()
        ds_ten_nhom_tivi = []
        for nhom_tivi in ds_nhom_tivi:
            ds_ten_nhom_tivi.append(nhom_tivi['Ten'])
        # Khởi tạo đối tượng nhóm TIVI
        app = wx.App()
        frame = wx.MDIChildFrame(self,title = "Nhóm Tivi",size = (500,430))
        panel = panel_Bai_7_2(frame)
        panel.lstbox_dsnhom.Append(ds_ten_nhom_tivi)
        frame.Show(True)
        app.MainLoop()
        xl_nhom_tivi.disconnect()

    def menuItem9_them_nv_click( self, event ):
        title_name = "Thêm nhân viên"
        ds_children = self.GetChildren()
        for children in ds_children:
            if children.GetTitle()==title_name:
                children.Activate()
                return
        app=wx.App()
        # wx.Frame => wx.MDICHildFrame , None =>self
        frame = wx.MDIChildFrame(self,title="Thêm nhân viên",size=(520,370))
        panel = panel_Bai_7_3(frame)
        frame.Show(True)
        app.MainLoop()

    def menuItem_themTV_click( self, event ):
        title_name = "Thêm Tivi"
        ds_children = self.GetChildren()
        for children in ds_children:
            if children.GetTitle()==title_name:
                children.Activate()
                return
        xl_nhom_tivi = NhomTivi(duong_dan_tivi)
        ds_nhom_tivi = xl_nhom_tivi.doc_danh_sach_nhom_tv()
        ds_ten_nhom_tivi = []
        for nhom_tivi in ds_nhom_tivi:
            ds_ten_nhom_tivi.append(nhom_tivi['Ten'])
        app = wx.App()
        frame = wx.MDIChildFrame(self,title="Thêm Tivi",size=(520,280))
        panel = panel_Bai_7_4(frame)
        panel.choice_nhom_tv.Append(ds_ten_nhom_tivi)
        frame.Show(True)
        app.MainLoop()
        xl_nhom_tivi.disconnect()
