#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Purpose: A minimum wxPython frame.
#-------------------------------------------------------------------------------

import wx

class Frame(wx.Frame):
    def __init__(self, parent, title):
        super(self.__class__, self).__init__(parent=parent, title=title, size=(800, 600))

        self.CenterOnScreen()

class App(wx.App):
    def OnInit(self):
        self.frame = Frame(parent=None, title='Spare')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()





