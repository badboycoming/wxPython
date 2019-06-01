#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use font dialog, to control the text display.
#
#          * Have bugs: when adjust the font, the frame, panel, cannot refresh to get better layout immediately
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1, title='Set Font Example'):
        super(self.__class__, self).__init__(parent=parent, id=id, title=title)
        self.panel = wx.Panel(parent=self, id=-1)

        self.st = wx.StaticText(parent=self.panel, id=-1, label='Have a nice day :)')
        btn = wx.Button(parent=self.panel, label='Set Font')
        self.Bind(event=wx.EVT_BUTTON, handler=self.OnSetFont, source=btn)

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)

        # NOTE: how to make the item at the center of the Horizontal Layout Box
        subSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        subSizer1.Add(item=(1, 1), proportion=1)
        subSizer1.Add(item=self.st)
        subSizer1.Add(item=(1, 1), proportion=1)
        self.mainSizer.Add(item=subSizer1, proportion=0, flag=wx.ALL|wx.EXPAND, border=10)

        self.mainSizer.Add(item=wx.StaticLine(parent=self.panel), proportion=0, flag=wx.EXPAND|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=10)

        # NOTE: how to make the item at the center of the Horizontal Layout Box
        subSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        subSizer2.Add(item=(1, 1), proportion=1)
        subSizer2.Add(item=btn)
        subSizer2.Add(item=(1, 1), proportion=1)
        self.mainSizer.Add(item=subSizer2, proportion=0, flag=wx.ALL^wx.TOP|wx.EXPAND, border=10)

        self.panel.SetSizer(self.mainSizer)
        # self.mainSizer.Fit(self)
        # self.mainSizer.SetSizeHints(self)  # to prevent the frame from getting smaller than this Fit size
        self.CenterOnScreen()

    def OnSetFont(self, event):

        dlg = wx.FontDialog(parent=self, data=wx.FontData())
        dlg.CenterOnParent()
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetFontData()
            font = data.GetChosenFont()
            self.st.SetFont(font=font)

            ### All following cannot refresh the Frame, Panel, Layout... :(
            # self.panel.Refresh()
            # self.panel.Update()
            # self.Refresh()
            # self.Update()
            # self.panel.AutoLayout()
            # self.mainSizer.RecalcSizes()

            # self.Maximize()
        dlg.Destroy()

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()





