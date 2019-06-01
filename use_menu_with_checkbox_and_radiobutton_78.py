#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: menu with checkbox and radiobutton.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Menu with Check and Radio')
        panel = wx.Panel(self)

        m1 = wx.Menu()
        exit = m1.Append(id=-1, text='E&xit', help='', kind=wx.ITEM_NORMAL)
        self.Bind(event=wx.EVT_MENU, handler=self.OnExit, source=exit)

        m2 = wx.Menu()
        # m2.AppendCheckItem(id=-1, text='Check Item 1', help='')
        # m2.AppendCheckItem(id=-1, text='Check Item 2', help='')
        # m2.AppendCheckItem(id=-1, text='Check Item 3', help='')
        # m2.AppendSeparator()
        # m2.AppendRadioItem(id=-1, text='Radio Item 1', help='')
        # m2.AppendRadioItem(id=-1, text='Radio Item 2', help='')
        # m2.AppendRadioItem(id=-1, text='Radio Item 3', help='')
        m2.Append(id=-1, text='Check Item 1', help='', kind=wx.ITEM_CHECK)
        m2.Append(id=-1, text='Check Item 2', help='', kind=wx.ITEM_CHECK)
        m2.Append(id=-1, text='Check Item 3', help='', kind=wx.ITEM_CHECK)
        m2.Append(id=wx.ID_SEPARATOR, text='', help='', kind=wx.ITEM_SEPARATOR)
        m2.Append(id=-1, text='Radio Item 1', help='', kind=wx.ITEM_RADIO)
        m2.Append(id=-1, text='Radio Item 2', help='', kind=wx.ITEM_RADIO)
        m2.Append(id=-1, text='Radio Item 3', help='', kind=wx.ITEM_RADIO)

        mb = wx.MenuBar()
        mb.Append(menu=m1, title='Menu')
        mb.Append(menu=m2, title='Toggle Items')
        self.SetMenuBar(mb)

        # layout
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




