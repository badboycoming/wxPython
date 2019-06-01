#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: connect menu with keyboard.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Menu with Accelerator')
        panel = wx.Panel(parent=self)

        m = wx.Menu()
        simple = m.Append(id=-1, text='&Simple', help='', kind=wx.ITEM_NORMAL)
        accel = m.Append(id=-1, text='&Accelerator\tCtrl+A', help='', kind=wx.ITEM_NORMAL)   # add accelerator method 1
        m.AppendSeparator()
        exit = m.Append(id=-1, text='E&xit', help='', kind=wx.ITEM_NORMAL)

        self.Bind(event=wx.EVT_MENU, handler=self.OnSimple, source=simple)
        self.Bind(event=wx.EVT_MENU, handler=self.OnAccelerator, source=accel)
        self.Bind(event=wx.EVT_MENU, handler=self.OnExit, source=exit)

        mb = wx.MenuBar()
        mb.Append(menu=m, title='&Menu')
        self.SetMenuBar(mb)

        # add accelerator method 2
        acceltbl = wx.AcceleratorTable([
            # wx.AcceleratorEntry(flags=wx.ACCEL_CTRL, keyCode=ord('Q'), cmdID=exit.GetId())
            (wx.ACCEL_CTRL, ord('Q'), exit.GetId())
        ])
        self.SetAcceleratorTable(acceltbl)

        # layout
        self.CenterOnScreen()

    def OnSimple(self, event):
        wx.MessageBox(message='You selected the Simple menu item.')

    def OnAccelerator(self, event):
        wx.MessageBox(message='You selected the Accelerated menu item!')

    def OnExit(self, event):
        self.Close()

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        self.SetTopWindow(frame)
        frame.Show()
        return True


if __name__ == '__main__':

    app = App()
    app.MainLoop()


