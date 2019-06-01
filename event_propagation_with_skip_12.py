#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo skip make the event propagation.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Propagation Event with Skip', size=(550, 220))

        self.panel = wx.Panel(parent=self)
        self.btn = wx.Button(parent=self.panel, label=':)', pos=(200, 60), size=(150, 50))

        # bind the button click event to frame
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnButtonClick, source=self.btn)

        # bind the left button down event to button
        # NOTE: due to the wx.EVT_LEFT_DOWN is not command event, so should bind it to self.btn
        self.btn.Bind(event=wx.EVT_LEFT_DOWN, handler=self.OnMouseDown)

        # flag for fun
        self.backgroundFlag = False
        self.clickFlag = False

        self.CenterOnScreen()

    def OnButtonClick(self, event):
        print 'OnButtonClick <<<'
        if not self.backgroundFlag:
            self.panel.SetBackgroundColour('Yellow')
            self.backgroundFlag = True
        else:
            self.panel.SetBackgroundColour('Green')
            self.backgroundFlag = False
        self.panel.Refresh()

    def OnMouseDown(self, event):
        print 'OnMouseDown >>>'
        if not self.clickFlag:
            self.btn.SetLabel('Again !')
            self.clickFlag = True
        else:
            self.btn.SetLabel('Click Me')
            self.clickFlag = False

        event.Skip()  # need propagation, due to the mouse down will generate a button click

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()





