#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: popup menu.
#-----------------------------------------------------------------------------

import wx

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Popup Menu')
        self.panel = wx.Panel(parent=self)

        stc = wx.StaticText(parent=self.panel, id=-1, label='Right-click on the panel to show a popup menu.')
        sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(item=(-1, -1), proportion=1)
        sizer.Add(item=stc, proportion=0, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, border=20)
        # sizer.Add(item=(-1, -1), proportion=1)
        self.panel.SetSizer(sizer)

        m = wx.Menu()
        exit = m.Append(id=-1, text='E&xit', help='', kind=wx.ITEM_NORMAL)
        self.Bind(event=wx.EVT_MENU, handler=self.OnExit, source=exit)

        mb = wx.MenuBar()
        mb.Append(menu=m, title='&Menu')
        self.SetMenuBar(mb)

        self.popupmenu = wx.Menu()
        self.popupmenu.SetTitle(title='Playoff')
        for text in 'Spurs Nets Rockets Lakers Warriors'.split():
            item = self.popupmenu.Append(id=-1, text=text, help='', kind=wx.ITEM_NORMAL)
            self.Bind(event=wx.EVT_MENU, handler=self.OnPopupItemSelected, source=item)
        self.panel.Bind(event=wx.EVT_CONTEXT_MENU, handler=self.OnShowPopupMenu)

        # layout
        self.CenterOnScreen()

    def OnShowPopupMenu(self, event):
        pos = event.GetPosition()
        pos = self.panel.ScreenToClient(pos)
        self.panel.PopupMenu(menu=self.popupmenu, pos=pos)

    def OnPopupItemSelected(self, event):
        item = self.popupmenu.FindItemById(event.GetId())
        text = item.GetText()
        wx.MessageBox(message='You selected item "%s"' % text)

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



