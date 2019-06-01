#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Purpose: Start the wxPython journey!
#-------------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self):
        # wx.Frame.__init__(self, parent=None, id=-1, title='My Frame', size=(600, 300))
        super(self.__class__, self).__init__(parent=None, id=-1, title='My Frame', size=(600, 300))
        panel = wx.Panel(parent=self, id=-1)
        panel.Bind(event=wx.EVT_MOTION, handler=self.OnMove)
        wx.StaticText(parent=panel, id=-1, label='Pos: ', pos=(15, 12))
        self.posCtrl = wx.TextCtrl(parent=panel, id=-1, value='', pos=(50, 10))

        self.CenterOnScreen()

    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValue('%s, %s' % (pos.x, pos.y))

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




