#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: menu item.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Add Menu Item in Runtime', size=(400, 250))
        panel = wx.Panel(parent=self)

        self.txt = wx.TextCtrl(parent=panel, id=-1, value='&New Item')
        btn = wx.Button(parent=panel, id=-1, label='Add Menu Item')
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnAddItem, source=btn)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(item=(1, 1), proportion=1)
        sizer.Add(item=self.txt, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(item=btn, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL|wx.LEFT, border=5)
        sizer.Add(item=(1, 1), proportion=1)
        panel.SetSizer(sizer)

        self.menu = wx.Menu()
        simple = self.menu.Append(id=-1, text='&Simple', help='', kind=wx.ITEM_NORMAL)
        self.menu.AppendSeparator()
        exit = self.menu.Append(id=-1, text='E&xit', help='', kind=wx.ITEM_NORMAL)
        self.Bind(event=wx.EVT_MENU, handler=self.OnSimple, source=simple)
        self.Bind(event=wx.EVT_MENU, handler=self.OnExit, source=exit)

        mb = wx.MenuBar()
        mb.Append(menu=self.menu, title='&Menu')
        self.SetMenuBar(menubar=mb)

        # layout
        self.CenterOnScreen()

    def OnSimple(self, event):
        wx.MessageBox(message='You selected the simple menu item.')

    def OnExit(self, event):
        self.Close()

    def OnAddItem(self, event):
        item = self.menu.Insert(pos=1, id=-1, text=self.txt.GetValue(), help='', kind=wx.ITEM_NORMAL)
        self.Bind(event=wx.EVT_MENU, handler=self.OnNewItemSelected, source=item)

    def OnNewItemSelected(self, event):
        wx.MessageBox(message='You selected a ' + self.txt.GetValue().replace('&', ''))

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        self.SetTopWindow(frame)
        frame.Show()
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




