#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use startup tips.
#-----------------------------------------------------------------------------

import wx

class App(wx.App):

    def OnInit(self):

        povider = wx.CreateFileTipProvider('tips.txt', 0)
        wx.ShowTip(parent=None, tipProvider=povider, showAtStartup=True)

        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



