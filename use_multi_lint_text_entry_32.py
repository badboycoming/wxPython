#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use multi line text entry.
#-----------------------------------------------------------------------------

import wx

class TextEntryFrame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Text Entry')
        panel = wx.Panel(parent=self, id=-1)

        multiLabel = wx.StaticText(parent=panel, id=-1, label='Multi-Line')
        multiText = wx.TextCtrl(parent=panel, id=-1,
                                value="This is the default value of the multiline text entry.\n\n"
                                "So, here I will put a poem:\n"
                                "Hold fast to dreams, for if dreams die,"
                                "Life is a broken-wing bird, that cannot fly."
                                "Hold fast to dreams, for if dreams go,"
                                "Life is a barren-field, fronzon with snow.",
                                size=(200, 100),
                                style=wx.TE_MULTILINE)
        multiText.SetInsertionPoint(0)

        richLabel = wx.StaticText(parent=panel, id=-1, label='Rich Text')
        richText = wx.TextCtrl(parent=panel, id=-1,
                               value="If supported by the native control, "
                               "this is reversed, and this is a different font.\n\n"
                               "Good good study,\n"
                               "Day day up.",
                               size=(200, 100),
                               style=wx.TE_MULTILINE|wx.TE_RICH)
                               # style=wx.TE_MULTILINE|wx.TE_RICH2)
        richText.SetInsertionPoint(0)
        richText.SetStyle(start=44, end=52, style=wx.TextAttr(colText='white', colBack='black'))
        points = richText.GetFont().GetPointSize()
        f = wx.Font(pointSize=points+3, family=wx.ROMAN, style=wx.ITALIC, weight=wx.BOLD, underline=True)
        richText.SetStyle(start=68, end=82, style=wx.TextAttr(colText='blue', colBack=wx.NullColour, font=f))

        gridSizer = wx.FlexGridSizer(rows=2, cols=2, hgap=6, vgap=6)
        gridSizer.AddMany([multiLabel, multiText, richLabel, richText])

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=gridSizer, proportion=1, flag=wx.ALIGN_CENTER|wx.ALL, border=50)

        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        # self.Center(wx.BOTH)
        self.CenterOnScreen()

class TextEntryApp(wx.App):

    def OnInit(self):
        self.frame = TextEntryFrame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = TextEntryApp()
    app.MainLoop()






