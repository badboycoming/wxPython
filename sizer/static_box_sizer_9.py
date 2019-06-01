#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: static box sizer.
#-----------------------------------------------------------------------------

import wx
from blockwindow import BlockWindow

labels = 'one two three four five six seven eight nine'.split()

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Static Box Sizer')
        self.panel = wx.Panel(self)

        # make three static box sizer
        box1 = self.MakeStaticBoxSizer(boxLabel='Box 1', itemLabels=labels[0:3])
        box2 = self.MakeStaticBoxSizer(boxLabel='Box 2', itemLabels=labels[3:6])
        box3 = self.MakeStaticBoxSizer(boxLabel='Box 3', itemLabels=labels[6:9])

        # we can also use a sizer to manage the placement of other sizers
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(item=box1, proportion=0, flag=wx.ALL, border=10)
        sizer.Add(item=box2, proportion=0, flag=wx.ALL, border=10)
        sizer.Add(item=box3, proportion=0, flag=wx.ALL, border=10)
        self.panel.SetSizer(sizer)
        sizer.Fit(self)

    def MakeStaticBoxSizer(self, boxLabel, itemLabels):
        box = wx.StaticBox(parent=self.panel, id=-1, label=boxLabel)
        sizer = wx.StaticBoxSizer(box, wx.VERTICAL)

        for label in itemLabels:
            bw = BlockWindow(parent=self.panel, label=label)
            sizer.Add(item=bw, proportion=0, flag=wx.ALL, border=2)

        return sizer

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



