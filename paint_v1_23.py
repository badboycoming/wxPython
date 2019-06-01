#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: paint version 1.
#-----------------------------------------------------------------------------

import wx
import copy

class SketchWindow(wx.Window):

    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id)
        self.SetBackgroundColour('White')

        # create a wx.pen object
        self.colour = 'Black'
        self.thickness = 1
        self.pen = wx.Pen(colour=self.colour, width=self.thickness, style=wx.SOLID)

        # initial vars
        self.lines = []
        self.curLine = []
        self.pos = (0, 0)
        self.InitBuffer()

        # link the events
        self.Bind(event=wx.EVT_LEFT_DOWN, handler=self.OnLeftDown)
        self.Bind(event=wx.EVT_MOTION, handler=self.OnMotion)
        self.Bind(event=wx.EVT_LEFT_UP, handler=self.OnLeftUp)
        self.Bind(event=wx.EVT_SIZE, handler=self.OnSize)
        # self.Bind(event=wx.EVT_IDLE, handler=self.OnIdle)
        self.Bind(event=wx.EVT_PAINT, handler=self.OnPaint)

    def InitBuffer(self):
        size = self.GetClientSize()

        # create a buffered device context
        self.buffer = wx.EmptyBitmap(width=size.width, height=size.height)
        # dc = wx.BufferedDC(dc=None, buffer=self.buffer)  # keyword error
        dc = wx.BufferedDC(None, self.buffer)
        dc.SetBackground(brush=wx.Brush(colour=self.GetBackgroundColour()))
        dc.Clear()  # to trigger wx.EVT_PAINT

        self.__DrawLines(dc)
        self.reInitBuffer = False

    def GetLinesData(self):
        # return self.lines[:]
        return copy.deepcopy(self.lines)

    def SetLinesData(self, lines):
        self.lines = copy.deepcopy(lines)
        self.InitBuffer()
        self.Refresh()

    def __DrawLines(self, dc):
        for colour, thickness, line in self.lines:
            pen = wx.Pen(colour=colour, width=thickness, style=wx.SOLID)
            dc.SetPen(pen)
            for coords in line:
                dc.DrawLine(*coords)

    def OnLeftDown(self, event):
        self.curLine = []
        # Get the mouse position
        self.pos = event.GetPositionTuple()
        self.CaptureMouse()

    def OnMotion(self, event):
        if event.Dragging() and event.LeftIsDown():
            dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
            self.__drawMotion(dc, event)

    def __drawMotion(self, dc, event):
        dc.SetPen(self.pen)
        newPos = event.GetPositionTuple()
        coords = self.pos + newPos
        self.curLine.append(coords)
        dc.DrawLine(*coords)
        self.pos=newPos

    def OnLeftUp(self, event):
        if self.HasCapture():
            self.lines.append((self.colour, self.thickness, self.curLine))
            self.curLine = []
            self.ReleaseMouse()

    def OnSize(self, event):
        # self.reInitBuffer = True
        self.InitBuffer()
        self.Refresh(eraseBackground=False)  # to avoid window blink

    # def OnIdle(self, event):
    #     if self.reInitBuffer:
    #         self.InitBuffer()
    #         self.Refresh(False)

    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self, self.buffer)

    def SetColour(self, colour):
        self.colour = colour
        self.pen = wx.Pen(colour=self.colour, width=self.thickness, style=wx.SOLID)

    def SetThickness(self, thickness):
        self.thickness = thickness
        self.pen = wx.Pen(colour=self.colour, width=self.thickness, style=wx.SOLID)

#-----------------------------------------------------------------------------

class Frame(wx.Frame):

    def __init__(self, parent=None, id=-1):
        super(self.__class__, self).__init__(parent=parent, id=id, title='Paint', size=(800, 600))
        self.sketch = SketchWindow(parent=self, id=-1)

        self.CenterOnScreen()

class App(wx.App):

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



