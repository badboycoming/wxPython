#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Mouse event.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Menu Event', size=(550, 220))

        self.panel = wx.Panel(parent=self)
        self.btn = wx.Button(parent=self.panel, label=':)', pos=(200, 60), size=(150, 50))

        # bind the button event to Frame
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnButtonClick, source=self.btn)

        # bind the mouse Enter event to Button
        #-------------------------------------------------------------------------------------------------------------
        # NOTE: due to the wx.EVT_ENTER_WINDOW is not command event, so should bind it to self.btn, shouldn't bind it
        # to frame.
        # self.Bind(event=wx.EVT_ENTER_WINDOW, handler=self.OnEnterWindow, source=self.btn)
        #-------------------------------------------------------------------------------------------------------------
        self.btn.Bind(event=wx.EVT_ENTER_WINDOW, handler=self.OnEnterWindow)

        # bind the mouse Leave event to Button
        #-------------------------------------------------------------------------------------------------------------
        # NOTE: due to the wx.EVT_LEAVE_WINDOW is not command event, so should bind it to self.btn, shouldn't bind it
        # to frame.
        # self.Bind(event=wx.EVT_LEAVE_WINDOW, handler=self.OnLeaveWindow, source=self.btn)
        #-------------------------------------------------------------------------------------------------------------
        self.btn.Bind(event=wx.EVT_LEAVE_WINDOW, handler=self.OnLeaveWindow)

        self.CenterOnScreen()

    def OnButtonClick(self, event):
        self.panel.SetBackgroundColour('Pink')
        self.panel.Refresh()

    def OnEnterWindow(self, event):
        self.btn.SetLabel('!! Over Me !!')
        # event.Skip()  # No need propagation, due to no need dispose anymore

    def OnLeaveWindow(self, event):
        self.btn.SetLabel('Not Over :)')
        # event.Skip()  # No need propagation, due to no need dispose anymore

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




