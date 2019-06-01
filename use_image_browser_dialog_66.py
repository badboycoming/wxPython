#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use image browser dialog.
#-----------------------------------------------------------------------------

import wx
import wx.lib.imagebrowser as imagebrowser

class App(wx.App):

    def OnInit(self):

        dlg = imagebrowser.ImageDialog(parent=None)
        if dlg.ShowModal() == wx.ID_OK:
            print 'You selected file is: %s' % dlg.GetFile()
        else:
            print 'You canceled.'
        dlg.Destroy()

        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()


