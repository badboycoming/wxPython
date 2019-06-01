#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: menu with fancy item, such as bitmap and color.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Fancy Menu')
        panel = wx.Panel(parent=self)

        m = wx.Menu()
        bmpClock = wx.Bitmap(name='./clock.png', type=wx.BITMAP_TYPE_PNG)
        # clock = m.Append(id=-1, text='&Clock', help='', kind=wx.ITEM_NORMAL)
        # clock.SetBitmap(bmp=bmpClock)
        clock = wx.MenuItem(parentMenu=m, id=-1, text='&Clock', help='', kind=wx.ITEM_NORMAL)
        clock.SetBitmap(bmp=bmpClock)
        m.AppendItem(item=clock)

        m.AppendSeparator()

        if 'wxMSW' in wx.PlatformInfo:

            bmpR = wx.Bitmap(name='./starR.png', type=wx.BITMAP_TYPE_PNG)
            bmpB = wx.Bitmap(name='./starB.png', type=wx.BITMAP_TYPE_PNG)

            font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
            font.SetWeight(wx.BOLD)

            item = wx.MenuItem(parentMenu=m, id=-1, text='&Super Star', help='', kind=wx.ITEM_NORMAL)
            item.SetFont(font)
            item.SetTextColour('Red')
            item.SetBitmap(bmp=bmpR)
            m.AppendItem(item)

            item = wx.MenuItem(parentMenu=m, id=-1, text='&Blue Star', help='', kind=wx.ITEM_NORMAL)
            item.SetFont(font)
            item.SetTextColour('Blue')
            item.SetBitmap(bmp=bmpB)
            m.AppendItem(item)

        bmpExit = wx.Bitmap(name='./exit.png', type=wx.BITMAP_TYPE_PNG)
        # exit = m.Append(id=-1, text='E&xit', help='', kind=wx.ITEM_NORMAL)
        # exit.SetBitmap(bmp=bmpExit)
        exit = wx.MenuItem(parentMenu=m, id=-1, text='E&xit', help='', kind=wx.ITEM_NORMAL)
        exit.SetBitmap(bmp=bmpExit)
        m.AppendItem(item=exit)

        self.Bind(event=wx.EVT_MENU, handler=self.OnExit, source=exit)

        mb = wx.MenuBar()
        mb.Append(menu=m, title='&Menu')
        self.SetMenuBar(menubar=mb)

        # layout
        self.CenterOnScreen()

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





