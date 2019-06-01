#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use single line text entry.
#-----------------------------------------------------------------------------

import wx

class TextEntryFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Text Entry',
                                             style=wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER^wx.MAXIMIZE_BOX, size=(250, 150))
        self.panel = wx.Panel(parent=self, id=-1)

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        usrnameLabel = wx.StaticText(parent=self.panel, id=-1, label='Username:')
        usrnameText = wx.TextCtrl(parent=self.panel, id=-1, value='', size=(120, -1))
        passwdLabel = wx.StaticText(parent=self.panel, id=-1, label='Password:')
        passwdText = wx.TextCtrl(parent=self.panel, id=-1, value='', size=(120, -1), style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        self.Bind(event=wx.EVT_TEXT_ENTER, handler=self.OnFinishPasswdEnter, source=passwdText)

        subSizer = wx.FlexGridSizer(rows=2, cols=2, hgap=5, vgap=5)
        # subSizer.AddGrowableCol(1)
        subSizer.Add(item=usrnameLabel, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT)
        subSizer.Add(item=usrnameText, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL)
        subSizer.Add(item=passwdLabel, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT)
        subSizer.Add(item=passwdText, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL)

        mainSizer.Add(item=subSizer, proportion=0, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=30)

        self.panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()

    def OnFinishPasswdEnter(self, event):
        self.panel.SetBackgroundColour('yellow')
        self.panel.Refresh()

class TextEntryApp(wx.App):

    def OnInit(self):
        self.frame = TextEntryFrame()
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == '__main__':

    app = TextEntryApp()
    app.MainLoop()





