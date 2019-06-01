#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Dialog scratch.
#-----------------------------------------------------------------------------

import wx

class App(wx.App):

    def __init__(self, redirect=True, filename=None):
        super(self.__class__, self).__init__(redirect=redirect, filename=filename)

    def OnInit(self):

        #### message dialog
        msg_dlg = wx.MessageDialog(parent=None,
                                   message='Is this the coolest thing ever ?',
                                   caption='Message Dialog',
                                   # style=wx.YES_NO | wx.ICON_ASTERISK)
                                   # style=wx.YES_NO | wx.ICON_QUESTION)  # no icon effect under MS-Windows
                                   # style=wx.YES_NO | wx.ICON_ERROR)
                                   # style=wx.YES_NO | wx.ICON_EXCLAMATION)
                                   # style=wx.YES_NO | wx.ICON_HAND)
                                   # style=wx.YES_NO | wx.ICON_INFORMATION)
                                   style=wx.YES_NO | wx.ICON_WARNING)
        result = msg_dlg.ShowModal()
        if result == wx.ID_YES:
            print 'You select "Yes" for the Message Dialog.'
        else:
            print 'You select "No" for the Message Dialog.'
        msg_dlg.Destroy()

        #### text entry dialog
        txt_dlg = wx.TextEntryDialog(parent=None,
                                     message='Who is the hero ?',
                                     caption='Text Entry Dialog',
                                     defaultValue='Peter Pan')
        result = txt_dlg.ShowModal()
        if result == wx.ID_OK:
            print 'Text Entry Dialog get value: %s' % txt_dlg.GetValue()
        txt_dlg.Destroy()

        #### single choice dialog
        sc_dlg = wx.SingleChoiceDialog(parent=None,
                                       message='What version of Python are you using ?',
                                       caption='Single Choice',
                                       choices=['1.5', '2.0', '2.1.3', '2.6.4', '2.7.1', '2.7.14', '3.6'])
        result = sc_dlg.ShowModal()
        if result == wx.ID_OK:
            print 'Single Choice Dialog get value index is: %s, value is: %s' % \
                  (sc_dlg.GetSelection(), sc_dlg.GetStringSelection())
        sc_dlg.Destroy()

        return True


if __name__ == '__main__':

    app = App(redirect=False)
    app.MainLoop()




