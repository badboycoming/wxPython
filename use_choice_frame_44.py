#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use choice pull down selection.
#-----------------------------------------------------------------------------

import wx

class ChoiceFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Choice')
        panel = wx.Panel(parent=self, id=-1)

        stc = wx.StaticText(parent=panel, id=-1, label='Select one:')

        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'goodgoodstudy']
        c = wx.Choice(parent=panel, id=-1, choices=sampleList)

        # layout
        subSizer = wx.BoxSizer(wx.HORIZONTAL)
        subSizer.Add(item=stc, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=5)
        subSizer.Add(item=c, proportion=0, flag=wx.ALL^wx.LEFT, border=5)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=subSizer, proportion=0, flag=wx.ALL, border=30)
        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()

class ChoiceApp(wx.App):

    def OnInit(self):
        frame = ChoiceFrame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = ChoiceApp()
    app.MainLoop()



