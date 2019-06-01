#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: menu item.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Menu item with Status bar', size=(500, 250))
        panel = wx.Panel(parent=self)

        # create StatusBar
        self.CreateStatusBar()

        # create MenuBar
        mb = wx.MenuBar()

        # create menu, append menu item to menu
        m1 = wx.Menu()
        simple = m1.Append(id=-1, text='&Simple', help='This is used to open simple window', kind=wx.ITEM_NORMAL)
        m1.AppendSeparator()
        exit = m1.Append(id=-1, text='E&xit', help='Exit GUI', kind=wx.ITEM_NORMAL)

        # bind event to menu item
        self.Bind(event=wx.EVT_MENU, handler=self.OnSimple, source=simple)
        self.Bind(event=wx.EVT_MENU, handler=self.OnExit, source=exit)

        # Add menu to MenuBar
        mb.Append(menu=m1, title='&Menu')

        # set frame menu
        self.SetMenuBar(mb)

        # layout
        self.CenterOnScreen()

    def OnSimple(self, event):
        wx.MessageBox(message='You selected the simple menu item.')

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





