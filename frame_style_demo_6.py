#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Frame style demo.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self, parent=None, title='Frame Style Demo',
                 # style=wx.DEFAULT_FRAME_STYLE
                 # style=wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
                 # style=wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER |                  wx.CAPTION | wx.CLOSE_BOX
                 # style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX
                 # style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER
                 # style=wx.DEFAULT_FRAME_STYLE ^ (wx.MAXIMIZE_BOX | wx.RESIZE_BORDER)
                 # style=wx.DEFAULT_FRAME_STYLE ^ (wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER)
                 style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER | wx.FRAME_TOOL_WINDOW
                 ):
        super(self.__class__, self).__init__(parent=parent, title=title, style=style)

        self.SetBackgroundColour('White')
        self.CenterOnScreen()

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




