#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use simple text button.
#-----------------------------------------------------------------------------

import wx

class ButtonFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Button')
        self.panel = wx.Panel(parent=self, id=-1)
        self.btn = wx.Button(parent=self.panel, id=-1, label='Hello')
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnClick, source=self.btn)
        # self.btn.SetDefault()

        # layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=self.btn, proportion=0, flag=wx.ALIGN_CENTER|wx.ALL, border=30)

        self.panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        # self.Center(wx.BOTH)
        self.CenterOnScreen()

    def OnClick(self, event):
        self.btn.SetLabel('Clicked')

class ButtonApp(wx.App):

    def OnInit(self):
        self.frame = ButtonFrame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = ButtonApp()
    app.MainLoop()



