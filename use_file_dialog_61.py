#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use file dialog.
#-----------------------------------------------------------------------------

import wx
import os

class App(wx.App):

    def OnInit(self):

        dlg = wx.FileDialog(parent=None,
                            message='Choose a file',
                            defaultDir=os.getcwd(),
                            wildcard='Python source (*.py)|*.py|Python compiled (*.pyc)|*.pyc|All files (*.*)|*.*',
                            style=wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            print 'Get file: %s' % dlg.GetPath()
        dlg.Destroy()

        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



