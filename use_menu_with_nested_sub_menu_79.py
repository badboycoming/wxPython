#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: menu with nested submenu.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Menu with SubMenu')
        panel = wx.Panel(parent=self)

        m = wx.Menu()
        sm = wx.Menu()
        sm.Append(id=-1, text='Sub menu item 1', help='', kind=wx.ITEM_NORMAL)
        sm.Append(id=-1, text='Sub menu item 2', help='', kind=wx.ITEM_NORMAL)
        m.AppendMenu(id=-1, text='SM', submenu=sm, help='')
        m.AppendSeparator()
        exit = m.Append(id=-1, text='E&xit', help='', kind=wx.ITEM_NORMAL)
        self.Bind(event=wx.EVT_MENU, handler=self.OnExit, source=exit)

        mb = wx.MenuBar()
        mb.Append(menu=m, title='&Menu')
        self.SetMenuBar(mb)

        self.CenterOnScreen()

    def OnExit(self, event):
        self.Close()

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        self.SetTopWindow(frame)
        frame.Show()
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



