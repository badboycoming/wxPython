#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: paint version 4, add Menu.
#-----------------------------------------------------------------------------

import wx
from paint_v1_23 import SketchWindow

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Paint', size=(800, 600))
        self.sketch = SketchWindow(parent=self, id=-1)
        self.sketch.Bind(event=wx.EVT_MOTION, handler=self.OnSketchMotion)
        self.__initStatusBar()
        self.__createMenuBar()

        self.CenterOnScreen()

    #------------------------------------------------------------------------- for status bar

    def __initStatusBar(self):
        self.sb = self.CreateStatusBar()
        self.sb.SetFieldsCount(3)
        self.sb.SetStatusWidths([-1, -2, -3])

    def OnSketchMotion(self, event):
        self.sb.SetStatusText('Pos: %s' % str(event.GetPositionTuple()), 0)
        self.sb.SetStatusText('Current Pts: %s' % len(self.sketch.curLine), 1)
        self.sb.SetStatusText('Line Cnts: %s' % len(self.sketch.lines), 2)
        event.Skip()

    #------------------------------------------------------------------------- for menu, with submenu

    def menuData(self):
        return (
            (
                '&File',
                (
                    ('&New', 'New sketch file', self.OnNew),
                    ('&Open', 'Open sketch file', self.OnOpen),
                    ('&Save', 'Save sketch file', self.OnSave),
                    ('', '', ''),
                    ('&Color',
                        (
                            ('&Black', '', self.OnColour, wx.ITEM_RADIO),
                            ('&Red', '', self.OnColour, wx.ITEM_RADIO),
                            ('&Green', '', self.OnColour, wx.ITEM_RADIO),
                            ('&Blue', '', self.OnColour, wx.ITEM_RADIO),
                        )
                     ),
                    ('', '', ''),
                    ('&Quit', 'Quit the program', self.OnCloseWindow),
                )
            ),

            (
                '&Help',
                (
                    ('&Check Update...', 'Check for avaliable updates', self.OnUpdate),
                    ('', '', ''),
                    ('&About', 'About the program', self.OnAbout),
                )
            ),
        )

    def __createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(menu=self.createMenu(menuItems), title=menuLabel)
        self.SetMenuBar(menuBar)

    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachItem in menuData:
            if len(eachItem) == 2:
                label = eachItem[0]
                subMenu = self.createMenu(eachItem[1])
                menu.AppendMenu(id=-1, text=label, submenu=subMenu)  # NOTE, subMenu use AppendMenu
            else:
                self.createMenuItem(menu, *eachItem)
        return menu

    def createMenuItem(self, menu, text, help, handler, kind=wx.ITEM_NORMAL):
        if text == '':
            menu.AppendSeparator()
            return
        menuItem = menu.Append(id=-1, text=text, help=help, kind=kind)
        self.Bind(event=wx.EVT_MENU, handler=handler, source=menuItem)

    def OnNew(self, event): pass
    def OnOpen(self, event): pass
    def OnSave(self, event): pass
    def OnUpdate(self, event): pass
    def OnAbout(self, event): pass

    def OnColour(self, event):
        menubar = self.GetMenuBar()
        itemId = event.GetId()
        item = menubar.FindItemById(itemId)
        colour = item.GetLabel()
        self.sketch.SetColour(colour)

    def OnCloseWindow(self, event):
        self.Destroy()

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




