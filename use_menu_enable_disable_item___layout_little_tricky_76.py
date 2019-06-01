#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: menu item, enable or disable.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Enable/Disable Menu Item', size=(400, 250))
        panel = wx.Panel(parent=self)

        self.btn = wx.Button(parent=panel, id=-1, label='Disable Item') #, pos=(50, 50))
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnToggleItem, source=self.btn)

        # layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(item=(-1, -1), proportion=1)
        sizer.Add(item=self.btn, proportion=0, flag=wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(item=(-1, -1), proportion=1)
        panel.SetSizer(sizer)
        self.CenterOnScreen()

        self._CreateMenu()

        # m = wx.Menu()
        #
        # self.idsimple = wx.NewId()
        # m.Append(id=self.idsimple, text='&Simple', help='', kind=wx.ITEM_NORMAL)
        # self.Bind(event=wx.EVT_MENU, handler=self.OnSimple, id=self.idsimple)
        #
        # m.AppendSeparator()
        #
        # idexit = wx.NewId()
        # m.Append(id=idexit, text='E&xit', help='', kind=wx.ITEM_NORMAL)
        # self.Bind(event=wx.EVT_MENU, handler=self.OnExit, id=idexit)
        #
        # mb = wx.MenuBar()
        # mb.Append(menu=m, title='&Menu')
        # self.SetMenuBar(mb)

        # ##################################################################### layout cannot in here !! Why...??  Not bad in Linux, only bad in Windows
        # # layout
        # sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(item=(-1, -1), proportion=1)
        # sizer.Add(item=self.btn, proportion=0, flag=wx.ALIGN_CENTER_HORIZONTAL)
        # sizer.Add(item=(-1, -1), proportion=1)
        # panel.SetSizer(sizer)
        # self.CenterOnScreen()
        # #####################################################################

    def _CreateMenu(self):

        m = wx.Menu()

        self.idsimple = wx.NewId()
        m.Append(id=self.idsimple, text='&Simple', help='', kind=wx.ITEM_NORMAL)
        self.Bind(event=wx.EVT_MENU, handler=self.OnSimple, id=self.idsimple)

        m.AppendSeparator()

        idexit = wx.NewId()
        m.Append(id=idexit, text='E&xit', help='', kind=wx.ITEM_NORMAL)
        self.Bind(event=wx.EVT_MENU, handler=self.OnExit, id=idexit)

        mb = wx.MenuBar()
        mb.Append(menu=m, title='&Menu')
        self.SetMenuBar(mb)

    def OnSimple(self, event):
        wx.MessageBox(message='You selected the simple menu item.')

    def OnExit(self, event):
        self.Close()

    def OnToggleItem(self, event):
        mb = self.GetMenuBar()
        enabled = mb.IsEnabled(id=self.idsimple)
        mb.Enable(id=self.idsimple, enable=(not enabled))
        self.btn.SetLabel(('Enable' if enabled else 'Disable') + ' Item')

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        self.SetTopWindow(frame)
        frame.Show()
        return True


if __name__ == '__main__':

    app = App()
    app.MainLoop()




