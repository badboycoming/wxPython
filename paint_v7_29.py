#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: paint version 7, final.
#-----------------------------------------------------------------------------

import wx
import wx.html
from wx.lib import buttons

import cPickle
import os

from paint_v1_23 import SketchWindow

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1):
        self.title = 'Paint'
        super(self.__class__, self).__init__(parent=parent, id=id, title=self.title, size=(800, 600))
        self.filename = ''
        self.wildcard = 'Sketch files (*.sketch)|*.sketch|All files(*.*)|*.*'
        self.sketch = SketchWindow(parent=self, id=-1)
        # wx.EVT_MOTION(self.sketch, self.OnSketchMotion)
        self.sketch.Bind(event=wx.EVT_MOTION, handler=self.OnSketchMotion)
        self.__initStatusBar()
        self.__createMenuBar()
        self.__createToolBar()
        self.__createPanel()

        self.CenterOnScreen()

    #------------------------------------------------------------------------- for StatusBar

    def __initStatusBar(self):
        self.sb = self.CreateStatusBar()
        self.sb.SetFieldsCount(3)
        self.sb.SetStatusWidths([-1, -2, -3])

    def OnSketchMotion(self, event):
        self.sb.SetStatusText('Pos: %s' % str(event.GetPositionTuple()), 0)
        self.sb.SetStatusText('Current Pts: %s' % len(self.sketch.curLine), 1)
        self.sb.SetStatusText('Line Cnts: %s' % len(self.sketch.lines), 2)
        event.Skip()

    #------------------------------------------------------------------------- for MenuBar

    def menuData(self):
        return (
            ('&File',
                (
                    ('&New', 'New Sketch File', self.OnNew),
                    ('&Open', 'Open Sketch File', self.OnOpen),
                    ('&Save', 'Save Sketch Fike', self.OnSave),
                    ('&Save As...', 'Save Sketch Fike As', self.OnSaveAs),
                    ('', '', ''),
                    ('&Color',
                        (
                            ('&Black', '', self.OnColor, wx.ITEM_RADIO),
                            ('&Red', '', self.OnColor, wx.ITEM_RADIO),
                            ('&Green', '', self.OnColor, wx.ITEM_RADIO),
                            ('&Bl&ue', '', self.OnColor, wx.ITEM_RADIO),
                            # ('&Other...', '', self.OnOtherColor, wx.ITEM_RADIO),
                            ('&Other...', '', self.OnOtherColor),
                        )
                    ),
                    ('', '', ''),
                    ('&Quit', 'Quit the program', self.OnCloseWindow),
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

    def OnNew(self, event):
        pass

    def OnOpen(self, event):
        dlg = wx.FileDialog(parent=self,
                            message='Open sketch file...',
                            defaultDir=os.getcwd(),
                            style=wx.OPEN,
                            wildcard=self.wildcard)
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
                wx.MessageBox('%s is not a valid sketch file!' % self.filename,
                              'Oops!', style=wx.OK|wx.ICON_EXCLAMATION)

    def OnSave(self, event):
        if not self.filename:
            self.OnSaveAs(event)
        else:
            self.SaveFile()

    def OnSaveAs(self, event):
        dlg = wx.FileDialog(parent=self,
                            message='Save sketch as...',
                            defaultDir=os.getcwd(),
                            style=wx.SAVE|wx.OVERWRITE_PROMPT,
                            wildcard=self.wildcard)
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

    def OnColor(self, event):
        menubar = self.GetMenuBar()
        itemId = event.GetId()
        item = menubar.FindItemById(itemId)
        if not item:
            toolbar = self.GetToolBar()
            item = toolbar.FindById(itemId)
            color = item.GetShortHelp()
        else:
            color = item.GetLabel()
        self.sketch.SetColour(color)

    def OnOtherColor(self, event):
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)
        if dlg.ShowModal() == wx.ID_OK:
            self.sketch.SetColour(dlg.GetColourData().GetColour())
        dlg.Destroy()

    def OnUpdate(self, event):
        pass

    def OnAbout(self, event):
        dlg = SketchAbout(self)
        dlg.ShowModal()
        dlg.Destroy()

    def OnCloseWindow(self, event):
        self.Destroy()

    def __createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuTitle = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(menu=self.createMenu(menuItems), title=menuTitle)
        self.SetMenuBar(menuBar)

    def createMenu(self, menuItems):
        menu = wx.Menu()
        for eachItem in menuItems:
            if len(eachItem) == 2:
                text = eachItem[0]
                subMenu = self.createMenu(eachItem[1])
                menu.AppendMenu(id=-1, text=text, submenu=subMenu)
            else:
                self.createMenuItem(menu, *eachItem)
        return menu

    def createMenuItem(self, menu, text, help, handler, kind=wx.ITEM_NORMAL):
        if text == '':
            menu.AppendSeparator()
            return
        menuItem = menu.Append(id=-1, text=text, help=help, kind=kind)
        self.Bind(event=wx.EVT_MENU, handler=handler, source=menuItem)

    #------------------------------------------------------------------------- for ToolBar

    def toolbarData(self):
        return (
            ('New', './sketch_icon/new.bmp', 'Create new sketch', self.OnNew),
            ('', '', '', ''),
            ('Open', './sketch_icon/open.bmp', 'Open existing sketch', self.OnOpen),
            ('Save', './sketch_icon/save.bmp', 'Save existing sketch', self.OnSave),
        )

    def toolbarColorData(self):
        return ('Black', 'Red', 'Green', 'Blue')

    def __createToolBar(self):
        toolbar = self.CreateToolBar()
        for each in self.toolbarData():
            self.createSimpleTool(toolbar, *each)
        toolbar.AddSeparator()
        for each in self.toolbarColorData():
            self.createColorTool(toolbar, each)
        toolbar.Realize()

    def createSimpleTool(self, toolbar, label, filename, help, handler):
        if label == '':
            toolbar.AddSeparator()
            return
        bmp = wx.Image(filename, wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        toolItem = toolbar.AddSimpleTool(-1, bmp, label, help)
        self.Bind(wx.EVT_MENU, handler, toolItem)  # NOTE, tool button binding to 'wx.EVT_MENU'

    def createColorTool(self, toolbar, color):
        bmp = self.MakeBitmap(color)
        toolItem = toolbar.AddRadioTool(-1, bmp, shortHelp=color)
        self.Bind(wx.EVT_MENU, self.OnColor, toolItem)  # # NOTE, tool button binding to 'wx.EVT_MENU'

    def MakeBitmap(self, color):
        bmp = wx.EmptyBitmap(16, 15)
        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        dc.SetBackground(wx.Brush(color))
        dc.Clear()
        dc.SelectObject(wx.NullBitmap)
        return bmp

    #------------------------------------------------------------------------- for control panel

    def __createPanel(self):
        controlPanel = ControlPanel(parent=self, id=-1, sketch=self.sketch)
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(item=controlPanel, proportion=0, flag=wx.EXPAND)
        box.Add(item=self.sketch, proportion=1, flag=wx.EXPAND)
        self.SetSizer(box)

#----------------------------------------------------------------------------- Auxilinary Class

class ControlPanel(wx.Panel):

    BMP_SIZE = 16
    BMP_BORDER = 3
    NUM_COLS = 4
    SPACING = 4

    colorList = ('Black', 'Yellow', 'Red', 'Green',
                 'Blue', 'Purple', 'Brown', 'Aquamarine',
                 'Forest Green', 'Light Blue', 'Goldnrod', 'Cyan',
                 'Orange', 'Navy', 'Dark Grey', 'Light Grey')

    maxThickness = 16

    def __init__(self, parent, id, sketch):
        super(self.__class__, self).__init__(parent=parent, id=id, style=wx.RAISED_BORDER)
        self.sketch = sketch
        buttonSize = (self.BMP_SIZE + 2 * self.BMP_BORDER,
                      self.BMP_SIZE + 2 * self.BMP_BORDER)
        colorGrid = self.__createColorGrid(parent, buttonSize)
        thicknessGrid = self.__createThicknessGrid(buttonSize)
        self.__layout(colorGrid, thicknessGrid)

    def __createColorGrid(self, parent, buttonSize):
        self.colorMap = {}
        self.colorButtons = {}
        colorGrid = wx.GridSizer(cols=self.NUM_COLS, hgap=2, vgap=2)
        for eachColor in self.colorList:
            bmp = parent.MakeBitmap(eachColor)
            b = buttons.GenBitmapToggleButton(self, -1, bmp, size=buttonSize)
            b.SetBezelWidth(1)
            b.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON, self.OnSetColour, b)
            colorGrid.Add(b, 0)
            self.colorMap[b.GetId()] = eachColor
            self.colorButtons[eachColor] = b
        self.colorButtons[self.colorList[0]].SetToggle(True)
        return colorGrid

    def __createThicknessGrid(self, buttonSize):
        self.thicknessIdMap = {}
        self.thicknessButtons = {}
        thicknessGrid = wx.GridSizer(cols=self.NUM_COLS, hgap=2, vgap=2)
        for x in range(1, self.maxThickness + 1):
            b = buttons.GenToggleButton(self, -1, str(x), size=buttonSize)
            b.SetBezelWidth(1)
            b.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON, self.OnSetThickness, b)
            thicknessGrid.Add(b, 0)
            self.thicknessIdMap[b.GetId()] = x
            self.thicknessButtons[x] = b
        self.thicknessButtons[1].SetToggle(True)
        return thicknessGrid

    def OnSetColour(self, event):
        color = self.colorMap[event.GetId()]
        if color != self.sketch.colour:
            self.colorButtons[self.sketch.colour].SetToggle(False)
        self.sketch.SetColour(color)

    def OnSetThickness(self, event):
        thickness = self.thicknessIdMap[event.GetId()]
        if thickness != self.sketch.thickness:
            self.thicknessButtons[self.sketch.thickness].SetToggle(False)
        self.sketch.SetThickness(thickness)

    def __layout(self, colorGrid, thicknessGrid):
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(colorGrid, 0, wx.ALL, self.SPACING)
        box.Add(thicknessGrid, 0, wx.ALL, self.SPACING)
        self.SetSizer(box)
        box.Fit(self)

class SketchAbout(wx.Dialog):
    text = '''
<html>
    <body bgcolor="#ACAA60">
        <center>
            <table bgcolor="#455481" width="100%" cellspacing="0" cellpadding="0" border="1">
                <tr>
                    <td align="center"><h1>Sketch!</h1></td>
                </tr>
            </table>
        </center>

<p><b>Sketch</b> is a demonstration program for <b>wxPython In Action</b>
Chapter 7. It is based on the SuperDoodle demo include with wxPython,
avaliable at http://www.wxpython.org/
</p>

<p><b>SuperDoodle</b> and <b>wxPython</b> are brought to you by
<b>Robin Dunn</b> and <b>Total Control Software</b>, Copyright 
&copy; 1997-2006.
</p>

    </body>
</html>
'''
    def __init__(self, parent):
        super(self.__class__, self).__init__(parent=parent, id=-1, title='About Paint', size=(400, 400))
        html = wx.html.HtmlWindow(self)
        html.SetPage(self.text)
        button = wx.Button(parent=self, id=wx.ID_OK, label='OK')

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(item=html, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        sizer.Add(item=button, proportion=0, flag=wx.ALIGN_CENTER|wx.ALL, border=5)

        self.SetSizer(sizer)
        self.Layout()

#----------------------------------------------------------------------------- App Class

class App(wx.App):

    def OnInit(self):
        # startup splash
        bmp = wx.Image('./sketch_icon/splash.png').ConvertToBitmap()
        wx.SplashScreen(bmp, wx.SPLASH_CENTER_ON_SCREEN|wx.SPLASH_TIMEOUT, 1000, None, -1)
        wx.Yield()

        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()




