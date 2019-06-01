#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: paint version 5, add FileDialog.
#-----------------------------------------------------------------------------

import wx
from paint_v1_23 import SketchWindow
import cPickle
import os
# import pdb; pdb.set_trace()

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1):
        self.title = 'Paint'
        super(self.__class__, self).__init__(parent=parent, id=id, title=self.title, size=(800, 600))
        self.filename = ''
        self.wildcard = 'Sketch files (*.sketch)|*.sketch|All files(*.*)|*.*'
        self.sketch = SketchWindow(parent=self, id=-1)
        # self.sketch.SetBackgroundColour('Gray')
        self.sketch.Bind(event=wx.EVT_MOTION, handler=self.OnSketchMotion)
        self.__initStatusBar()
        self.__createMenuBar()

        self.CenterOnScreen()

    def __initStatusBar(self):
        self.sb = self.CreateStatusBar()
        self.sb.SetFieldsCount(3)
        self.sb.SetStatusWidths([-1, -2, -3])

    def OnSketchMotion(self, event):
        self.sb.SetStatusText('Pos: %s' % str(event.GetPositionTuple()), 0)
        self.sb.SetStatusText('Current Pts: %s' % len(self.sketch.curLine), 1)
        self.sb.SetStatusText('Line Cnts: %s' % len(self.sketch.lines), 2)
        event.Skip()

    def menuData(self):
        return (
            ('&File',
                (
                    ('&New', 'New sketch file', self.OnNew),
                    ('&Open', 'Open sketch file', self.OnOpen),
                    ('&Save', 'Save sketch file', self.OnSave),
                    ('&Save As...', 'Save as sketch file', self.OnSaveAs),
                    ('', '', ''),
                    ('&Color',
                        (
                            ('&Black', '', self.OnColour, wx.ITEM_RADIO),
                            ('&Red', '', self.OnColour, wx.ITEM_RADIO),
                            ('&Green', '', self.OnColour, wx.ITEM_RADIO),
                            ('&Blue', '', self.OnColour, wx.ITEM_RADIO),
                        ),
                    ),
                    ('', '', ''),
                    ('&Quit', 'Quit', self.OnCloseWindow),
                )
            ),

            ('&Help',
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
                menu.AppendMenu(id=-1, text=label, submenu=subMenu)
            else:
                self.createMenuItem(menu, *eachItem)
        return menu

    def createMenuItem(self, menu, text, help, handler, kind=wx.ITEM_NORMAL):
        if text == '':
            menu.AppendSeparator()
            return
        menuItem = menu.Append(id=-1, text=text, help=help, kind=kind)
        self.Bind(event=wx.EVT_MENU, handler=handler, source=menuItem)


    def OnNew(self, event):
    #     if self.sketch:
    #         self.sketch.Destroy()
    #     self.sketch = SketchWindow(parent=self, id=-1)
    #     self.sketch.SetBackgroundColour('White')
    #     self.sketch.InitBuffer()
    #     self.sketch.Refresh()
    #     self.sketch.Bind(event=wx.EVT_MOTION, handler=self.OnSketchMotion)
    #     self.SetTitle(self.title + ' - ' + 'Untitled*')
        pass


    def OnOpen(self, event):
        dlg = wx.FileDialog(parent=self,
                            message='Open sketch file...',
                            defaultDir=os.getcwd(),
                            wildcard=self.wildcard,
                            style=wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            if self.filename == dlg.GetPath():
                return
            self.filename = dlg.GetPath()
            self.ReadFile()
            self.SetTitle(self.title + ' - ' + self.filename)
        dlg.Destroy()

    def ReadFile(self):
        if self.filename:
            try:
                f = open(self.filename, 'rb')
                data = cPickle.load(f)
                f.close()
                self.sketch.SetLinesData(data)
            except cPickle.UnpickleableError:
                wx.MessageBox(message='%s is not a sketch file.' % self.filename,
                              caption='oops!',
                              style=wx.OK|wx.ICON_EXCLAMATION)

    def OnSave(self, event):
        if not self.filename:
            self.OnSaveAs(event)
        else:
            self.SaveFile()

    def OnSaveAs(self, event):
        dlg = wx.FileDialog(parent=self,
                            message='Save sketch as...',
                            defaultDir=os.getcwd(),
                            wildcard=self.wildcard,
                            style=wx.SAVE|wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            if not os.path.splitext(filename)[1]:
                filename += '.sketch'
            self.filename = filename
            self.SaveFile()
            self.SetTitle(self.title + ' - ' + self.filename)
        dlg.Destroy()

    def SaveFile(self):
        if self.filename:
            data = self.sketch.GetLinesData()
            f = open(self.filename, 'wb')
            cPickle.dump(obj=data, file=f, protocol=2)
            f.close()

    def OnColour(self, event):
        menuBar = self.GetMenuBar()
        itemId = event.GetId()
        item = menuBar.FindItemById(itemId)
        colour = item.GetLabel()
        self.sketch.SetColour(colour)

    def OnUpdate(self, event): pass
    def OnAbout(self, event): pass

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


