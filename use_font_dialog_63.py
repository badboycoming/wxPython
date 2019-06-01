#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use font dialog.
#-----------------------------------------------------------------------------

import wx

class App(wx.App):

    def OnInit(self):

        ###########
        # use class
        ###########

        dlg = wx.FontDialog(parent=None, data=wx.FontData())
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetFontData()
            font = data.GetChosenFont()
            colour = data.GetColour()
            print 'You selected: "%s", %d points' % (font.GetFaceName(), font.GetPointSize())

        dlg.Destroy()

        ####################################
        # use GetFontFromUser for convinence
        ####################################

        userSetFont = wx.GetFontFromUser()
        if userSetFont.Ok():
            print 'You chosed font name is: %s' % userSetFont.GetFaceName()
        else:
            print 'You canceled.'

        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()








