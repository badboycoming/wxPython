#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: custom event.
#-----------------------------------------------------------------------------

import wx

##############################################################################
# Step 1: Define the event

class TwoButtonEvent(wx.PyCommandEvent):
    def __init__(self, evtType, id):
        super(self.__class__, self).__init__(eventType=evtType, id=id)
        self.cnt = 0

    def GetClickCount(self):
        return self.cnt

    def SetClickCount(self, count):
        self.cnt = count

##############################################################################
# Step 2: Generate an event Type

EVT_TWO_BUTTON_TYPE = wx.NewEventType()

##############################################################################
# Step 3: Create a binder object

EVT_TWO_BUTTON = wx.PyEventBinder(evtType=EVT_TWO_BUTTON_TYPE, expectedIDs=1)

##############################################################################
# Step 4: Add new event creation code, and use ProcessEvent() to induce the event to system

class TwoButtonPanel(wx.Panel):

    def __init__(self, parent=None, id=-1, leftText='Left', rightText='Right'):
        super(self.__class__, self).__init__(parent=parent, id=id)

        self.leftBtn = wx.Button(parent=self, label=leftText, pos=(50, 50))
        self.rightBtn = wx.Button(parent=self, label=rightText, pos=(200, 50))

        self.leftClick = False
        self.rightClick = False
        self.clickCount = 0
        self.leftBtn.Bind(event=wx.EVT_LEFT_DOWN, handler=self.OnLeftClick)
        self.rightBtn.Bind(event=wx.EVT_LEFT_DOWN, handler=self.OnRightClick)

    def OnLeftClick(self, event):
        self.leftClick = True
        self.OnClick()
        event.Skip()

    def OnRightClick(self, event):
        self.rightClick = True
        self.OnClick()
        event.Skip()

    def OnClick(self):
        self.clickCount += 1
        if self.leftClick and self.rightClick:
            self.leftClick = False
            self.rightClick = False

            ##################################################################
            # instance the custome event
            evt = TwoButtonEvent(evtType=EVT_TWO_BUTTON_TYPE, id=self.GetId())
            # add data to event
            evt.SetClickCount(self.clickCount)
            # process the event
            self.GetEventHandler().ProcessEvent(evt)

#-----------------------------------------------------------------------------

class Frame(wx.Frame):
    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Click Count: 0', size=(400, 200))
        self.panel = TwoButtonPanel(parent=self)
        self.Bind(event=EVT_TWO_BUTTON, handler=self.OnTwoClick, source=self.panel)

        self.CenterOnScreen()

    def OnTwoClick(self, event):
        self.SetTitle('Click Count: %s' % event.GetClickCount())

class App(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()





