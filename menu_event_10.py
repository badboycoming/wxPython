#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Menu event.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Menu Event', size=(700, 400))

        mFile = wx.Menu()
        mFile.Append(id=wx.NewId(), text='&Open')
        mFile.AppendSeparator()
        exitItem = mFile.Append(id=wx.NewId(), text='E&xit')

        mb = wx.MenuBar()
        mb.Append(menu=mFile, title='&File')
        self.SetMenuBar(menubar=mb)

        # bind
        self.Bind(event=wx.EVT_MENU, handler=self.OnClose, source=exitItem)

        self.SetBackgroundColour('White')
        self.CenterOnScreen()

    def OnClose(self, event):
        self.Close()

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


if __name__ == '__main__':

    app = App()
    app.MainLoop()





