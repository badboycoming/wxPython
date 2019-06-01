#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use single choice dialog.
#-----------------------------------------------------------------------------

import wx

class App(wx.App):

    def OnInit(self):

        ###################################
        # use standard single choice dialog
        ###################################

        choices = ['Alpha', 'Beta', 'Gama', 'Delta']
        dlg = wx.SingleChoiceDialog(parent=None, message='Pick A Choice', caption='Standard Choices', choices=choices)
        dlg.SetSelection(sel=1)  # set the default selection item
        if dlg.ShowModal() == wx.ID_OK:
            print '1st, You selected item index: %s' % dlg.GetSelection()  # get the selected item index, which begin with 0
            print '1st, You selected item string: %s' % dlg.GetStringSelection()
        dlg.Destroy()

        ##########################################
        # use function to get single choice string
        ##########################################

        userChoice = wx.GetSingleChoice(message='Pick A Choice', caption='Fun Choices String', choices=choices, parent=None)
        if userChoice == '':
            print '2nd, You canceled string selection.'
        else:
            print '2nd, You selected item string: %s' % userChoice

        #########################################
        # use function to get single choice index
        #########################################

        userChoiceIdx = wx.GetSingleChoiceIndex(message='Pick A Choice', caption='Fun Choices Index', choices=choices, parent=None)
        if userChoiceIdx == -1:
            print '3rd, You canceled index selection.'
        else:
            print '3rd, You selected item index: %s' % userChoiceIdx

        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



