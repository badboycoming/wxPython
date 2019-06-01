#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use dir dialog.
#-----------------------------------------------------------------------------

import wx
import os

class App(wx.App):

    def OnInit(self):

        ###########
        # use class
        ###########

        dlg = wx.DirDialog(parent=None,
                           message='Choose a directory...',
                           defaultPath=os.getcwd(),
                           style=wx.DD_DEFAULT_STYLE)
                           # style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)  # wx.DD_NEW_DIR_BUTTON seems no effect under MS-Windows

        if dlg.ShowModal() == wx.ID_OK:
            print 'You choosed dir is: %s' % dlg.GetPath()
        dlg.Destroy()


        ################################
        # use DirSelector for convinence
        ################################

        userSelDir = wx.DirSelector(message='Choose another directory...',
                                    defaultPath=os.getcwd(),
                                    style=wx.DD_DEFAULT_STYLE,
                                    parent=None)
        if userSelDir == '':
            print 'You canceled.'
        else:
            print 'You choosed dir is: %s' % userSelDir


        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



