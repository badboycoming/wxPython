#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use test entry dialog.
#-----------------------------------------------------------------------------

import wx

class App(wx.App):

    def OnInit(self):

        ################################
        # use standard text entry dialog
        ################################

        dlg = wx.TextEntryDialog(parent=None,
                                 message='What kind of text would you like to enter?',
                                 caption='Text Entry',
                                 defaultValue='Default Value',
                                 # style=wx.OK | wx.CANCEL)
                                 style=wx.OK | wx.CANCEL | wx.CENTER)  # wx.CENTER to make the dlg box in the center of the screen
        if dlg.ShowModal() == wx.ID_OK:
            print 'You entered: %s' % dlg.GetValue()
        else:
            print 'Oh, you canceled the entered.'
        dlg.Destroy()

        ##########################
        # use function to get text
        ##########################

        userInputText = wx.GetTextFromUser(message='Enter your name:',
                                           caption='Text Entry',
                                           default_value='',
                                           parent=None)
        if userInputText:
            print 'You entered name: %s' % userInputText
        else:
            print 'Oh, you entered nothing for name.'

        ##############################
        # use function to get password
        ##############################

        userInputPasswd = wx.GetPasswordFromUser(message='Enter your password:',
                                                 caption='Password Entry',
                                                 default_value='',
                                                 parent=None)
        if userInputPasswd:
            print 'You entered password: %s' % userInputPasswd
        else:
            print 'Oh, you entered nothing for password.'

        #################################################################################################
        # use function to get a number from user, less than min will be min, greater than max will be max
        #################################################################################################

        userInputNumber = wx.GetNumberFromUser(message='Enter a number(1~100):',
                                               prompt='~~~',
                                               caption='Number Entry',
                                               value=12,
                                               min=1,
                                               max=100,
                                               parent=None)
        if userInputNumber != -1:  # seems 'wx.GetNumberFromUser' not return -1 when user input beyond [1, 100]
            print 'You entered number: %d' % userInputNumber
        else:
            print 'Oh, you entered number is not in the valid range!'

        return True


if __name__ == '__main__':

    app = App()
    app.MainLoop()




