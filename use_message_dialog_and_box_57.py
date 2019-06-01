#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use message dialog and box.
#-----------------------------------------------------------------------------

import wx

class App(wx.App):

    def OnInit(self):

        ################################
        # use a class to create a dialog
        ################################

        dlg = wx.MessageDialog(parent=None, message='Is this explanation OK?', caption='Message Dialog',
                               # style=wx.YES_NO | wx.ICON_QUESTION)  # NOTE: wx.ICON_QUESTION have no effect under MS_Windows
                               style=wx.YES_NO | wx.ICON_INFORMATION)
        rtv = dlg.ShowModal()
        if rtv == wx.ID_YES:
            print 'Yes'
        else:
            print 'No'
        dlg.Destroy()

        ###################################
        # use a function to create a dialog
        ###################################

        rtv2 = wx.MessageBox(message='Is this way easier?', caption='Message Box',
                             style=wx.YES_NO | wx.ICON_WARNING)
                             # style=wx.YES_NO | wx.ICON_ERROR)

                             # style=wx.YES_NO | wx.ICON_EXCLAMATION)  # same as ICON_WARNING under MS_Windows
                             # style=wx.YES_NO | wx.ICON_STOP)         # same as ICON_ERROR under MS_Windows

                             # style=wx.YES_NO | wx.ICON_ASTERISK)     # no effect under MS_Windows

        #---->>> NOTE, `wx.MessageBox` not return wx.ID_YES, wx.ID_NO, etc. It return: wx.YES, wx.NO, wx.OK, wx.CANCEL
        # if rtv2 == wx.ID_YES:
        if rtv2 == wx.YES:
            print 'Yes'
        elif rtv2 == wx.NO:
            print 'No'

        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



