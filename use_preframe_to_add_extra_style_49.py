#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use PreFrame to add extra style. Easy to understand.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self):

        # pre-construct object
        pre = wx.PreFrame()
        pre.SetExtraStyle(wx.FRAME_EX_CONTEXTHELP)

        # create frame
        pre.Create(parent=None, id=-1, title='Help Context', size=(500, 300),
                   style=wx.DEFAULT_FRAME_STYLE ^ (wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))

        # transfer of underlying C++ pointers
        self.PostCreate(pre)

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




