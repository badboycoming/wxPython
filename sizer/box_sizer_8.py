#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: box sizer.
#-----------------------------------------------------------------------------

import wx
from blockwindow import BlockWindow

labels = 'one two three four'.split()

class VBoxSizerFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Vertical BoxSizer')
        sizer = self.CreateSizerAndWindows()
        self.SetSizer(sizer)
        self.Fit()

    def CreateSizerAndWindows(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        for label in labels:
            bw = BlockWindow(parent=self, label=label, size=(200, 30))
            sizer.Add(item=bw, flag=wx.EXPAND)
        return sizer

class HBoxSizerFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Horizontal BoxSizer')
        sizer = self.CreateSizerAndWindows()
        self.SetSizer(sizer)
        self.Fit()

    def CreateSizerAndWindows(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        for label in labels:
            bw = BlockWindow(parent=self, label=label, size=(75, 30))
            sizer.Add(item=bw, flag=wx.EXPAND)
        return sizer

class VBoxSizerStretchableFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Stretchable BoxSizer')
        sizer = self.CreateSizerAndWindows()
        self.SetSizer(sizer)
        self.Fit()

    def CreateSizerAndWindows(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        for label in labels:
            bw = BlockWindow(parent=self, label=label, size=(200, 30))
            sizer.Add(item=bw, flag=wx.EXPAND)

        # Add an item the takes all the free space
        bw = BlockWindow(parent=self, label='gets all free space', size=(200, 30))
        sizer.Add(item=bw, proportion=1, flag=wx.EXPAND)
        return sizer

class VBoxSizerMultiProportionalFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Proportional BoxSizer')
        sizer = self.CreateSizerAndWindows()
        self.SetSizer(sizer)
        self.Fit()

    def CreateSizerAndWindows(self):
        sizer=wx.BoxSizer(wx.VERTICAL)
        for label in labels:
            bw = BlockWindow(parent=self, label=label, size=(200, 30))
            sizer.Add(item=bw, flag=wx.EXPAND)

        # Add an item that takes one share of the free space
        bw = BlockWindow(parent=self, label='gets 1/3 of the free space', size=(200, 30))
        sizer.Add(item=bw, proportion=1, flag=wx.EXPAND)

        # add an item that takes two shares of the free space
        bw = BlockWindow(parent=self, label='gets 2/3 of the free space', size=(200, 30))
        sizer.Add(item=bw, proportion=2, flag=wx.EXPAND)

        # add an item that in normal state
        bw = BlockWindow(parent=self, label='normal', size=(200, 30))
        sizer.Add(item=bw, flag=wx.EXPAND)

        return sizer

#-----------------------------------------------------------------------------

class App(wx.App):

    def OnInit(self):
        for frame in [VBoxSizerFrame, HBoxSizerFrame, VBoxSizerStretchableFrame, VBoxSizerMultiProportionalFrame]:
            self.frame = frame()
            self.frame.Show()
            # self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



