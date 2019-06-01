#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to add subwindow and button to a frame.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Frame with Button', size=(300, 200))

        # create a panel based on current frame
        panel = wx.Panel(parent=self)

        # create a button based on the panel
        #button = wx.Button(parent=panel, label='Close', pos=wx.DefaultPosition, size=wx.DefaultSize)
        button = wx.Button(parent=panel, label='Close', pos=(115, 50), size=(60, 50))

        # binding
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnCloseButton, source=button)  # bind the button click event
        self.Bind(event=wx.EVT_CLOSE, handler=self.OnCloseWindow)  # bind the window close event

        self.CenterOnScreen()

    def OnCloseButton(self, event):
        print '>>> Invoke OnCloseButton'
        self.Close()  # Note, the wx.Frame.Close() will generate the wx.EVT_CLOSE, then the function OnCloseWindow will be invoked

    def OnCloseWindow(self, event):
        print '<<< Invoke OnCloseWindow'
        self.Destroy()

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

    def OnExit(self):
        print 'Clean...Over'


if __name__ == '__main__':

    app = App()
    app.MainLoop()





