#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: use menu.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Simple Menu', size=(400, 200))
        panel = wx.Panel(parent=self)

        # create menu bar
        mb = wx.MenuBar()

        # create menu
        m1 = wx.Menu()
        m2 = wx.Menu()
        m3 = wx.Menu()

        # add menu to menu bar
        mb.Append(menu=m1, title='&Left Menu')
        mb.Append(menu=m2, title='&Middle Menu')
        mb.Append(menu=m3, title='&Right Menu')

        # set frame menu
        self.SetMenuBar(mb)

        ######################################################################
        # idx = mb.FindMenu(title='&Left Menu')
        # print 'idx =', idx
        ######################################################################

        # layout
        self.CenterOnScreen()

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        self.SetTopWindow(frame)
        frame.Show()

        ######################################################################
        # mb = frame.GetMenuBar()
        # idx = mb.FindMenu(title='&Right Menu')
        # print 'Right menu idx =', idx
        ######################################################################

        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




