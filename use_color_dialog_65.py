#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use color dialog.
#-----------------------------------------------------------------------------

import  wx

class App(wx.App):

    def OnInit(self):

        ###########
        # use class
        ###########

        dlg = wx.ColourDialog(parent=None)
        # dlg.GetColourData().SetChooseFull(True)  # pop-up window with Customize window, seems have no effect under classic MS-Windows

        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetColourData()  # -> wx.ColourData
            print 'You selected is: %s' % str(data.GetColour().Get())
        else:
            print 'You canceled.'

        ######################################
        # use GetColourFromUser for convinence
        ######################################

        userSelColor = wx.GetColourFromUser()  # -> wx.Colour
        if userSelColor.Ok():
            print 'You now selected is: %s' % str(userSelColor.Get())
        else:
            print 'You canceled.'

        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()





