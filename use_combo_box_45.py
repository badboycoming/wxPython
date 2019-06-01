#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use combo box.
#-----------------------------------------------------------------------------

import wx

class ComboBoxFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Combo Box')
        panel = wx.Panel(parent=self, id=-1)

        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
        stc = wx.StaticText(parent=panel, id=-1, label='Select one:')
        cb1 = wx.ComboBox(parent=panel, id=-1, value='', choices=sampleList, style=wx.CB_DROPDOWN)
        # cb2 = wx.ComboBox(parent=panel, id=-1, value='', choices=sampleList, style=wx.CB_SIMPLE)   # NOTE: CB_SIMPLE is not support Sizer !!!
        cb2 = wx.ComboBox(parent=panel, id=-1, value='', choices=sampleList, style=wx.CB_READONLY)   # NOTE: CB_SIMPLE is not support Sizer !!!

        # layout
        gridSizer = wx.FlexGridSizer(rows=2, cols=2, vgap=5, hgap=5)
        gridSizer.Add(item=stc, proportion=0)
        gridSizer.Add(item=(1, 1))
        gridSizer.Add(item=cb1, proportion=0)
        gridSizer.Add(item=cb2, proportion=0)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=gridSizer, proportion=0, flag=wx.ALL, border=40)
        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()

class ComboBoxApp(wx.App):

    def OnInit(self):
        frame = ComboBoxFrame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = ComboBoxApp()
    app.MainLoop()



