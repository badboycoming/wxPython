#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use basic frame. Note, in common, not directely use Frame, but use it derive.
#-----------------------------------------------------------------------------

import wx

class App(wx.App):

    def OnInit(self):
        frame = wx.Frame(parent=None, id=-1, title='Basic Frame', size=(500, 300))
        frame.Show()
        self.SetTopWindow(frame=frame)
        frame.CenterOnScreen()
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




