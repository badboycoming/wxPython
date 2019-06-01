#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: a simple menu window, with wxPython.
# Date: Wed 01/25/2017
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)

        menuFile = wx.Menu()
        menuFile.Append(1, "&About...")
        menuFile.AppendSeparator()
        menuFile.Append(2, "E&xit")
        
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&File")
        self.SetMenuBar(menuBar)

        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")

        self.Bind(wx.EVT_MENU, self.OnAbout, id=1)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=2)

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello world sample", 
                "About Hello World", wx.OK | wx.ICON_INFORMATION, self)

class App(wx.App):

    def OnInit(self):
        frame = Frame("Hello World", (50, 60), (450, 340))
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()


