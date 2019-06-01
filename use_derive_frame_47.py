#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use derive frame.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Frame')
        panel = wx.Panel(parent=self, id=-1)
        btn = wx.Button(parent=panel, id=-1, label='Close Me')
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnCloseMe, source=btn)
        self.Bind(event=wx.EVT_CLOSE, handler=self.OnClose)

        # layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=btn, proportion=0, flag=wx.ALL, border=50)

        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()

    def OnCloseMe(self, event):
        self.Close()  # generate EVT_CLOSE

    def OnClose(self, event):
        self.Destroy()

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




