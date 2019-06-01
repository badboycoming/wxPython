#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use mini frame. Note, mini frame always used for Tool window, not display in task bar.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.MiniFrame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Mini Frame',
                                             style=wx.DEFAULT_FRAME_STYLE | wx.CLOSE_BOX)
                                             # style=wx.DEFAULT_FRAME_STYLE|wx.FRAME_TOOL_WINDOW)
        panel = wx.Panel(parent=self, id=-1)
        btn = wx.Button(parent=panel, id=-1, label='Close Me')
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnCloseMe, source=btn)
        self.Bind(event=wx.EVT_CLOSE, handler=self.OnCloseWindow)

        # layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=btn, proportion=0, flag=wx.ALL, border=50)
        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()

    def OnCloseMe(self, event):
        self.Close()  # generate wx.EVT_CLOSE

    def OnCloseWindow(self, event):
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



