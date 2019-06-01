#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Draw a radar graph.
#-----------------------------------------------------------------------------

import wx
import math
import random

class RadarGraph(wx.Window):

    def __init__(self, parent, title, labels):
        super(self.__class__, self).__init__(parent=parent)
        self.title = title
        self.labels = labels

        self.data = [0.0] * len(self.labels)
        self.titleFont = wx.Font(pointSize=14, family=wx.SWISS, style=wx.NORMAL, weight=wx.BOLD)
        self.labelFont = wx.Font(pointSize=10, family=wx.SWISS, style=wx.NORMAL, weight=wx.NORMAL)

        self.InitBuffer()
        self.Bind(event=wx.EVT_SIZE, handler=self.OnSize)
        self.Bind(event=wx.EVT_PAINT, handler=self.OnPaint)

    def InitBuffer(self):
        # create the buffer bitmap to be the same size as the window, then draw our graph to it.
        # since we use wx.BufferedDC whatever is drawn to the buffer is also drawn to the window.
        w, h = self.GetClientSize()
        self.buffer = wx.EmptyBitmap(width=w, height=h)
        # dc = wx.BufferedDC(dc=wx.ClientDC(self), buffer=self.buffer)
        dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
        self.DrawGraph(dc=dc)

    def OnSize(self, event):
        # when the window size changes, we need a new buffer
        self.InitBuffer()

    def OnPaint(self, event):
        # this automatically blits self.buffer to a wx.PaintDC when the dc destroyed (at the time of this function run over),
        # nothing else needs to do, no need user's paint command, due to wx.PaintDC also can draw on Screen as the wx.ClientDC
        dc = wx.BufferedPaintDC(window=self, buffer=self.buffer)  # refresh window from the buffer

    def GetData(self):
        return self.data

    def SetData(self, newData):
        assert len(newData) == len(self.data)
        self.data = newData[:]
        # dc = wx.BufferedDC(dc=wx.ClientDC(self), buffer=self.buffer)
        dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
        self.DrawGraph(dc=dc)

    def PolarToCartesian(self, radius, angle, cx, cy):
         x = radius * math.cos(math.radians(angle))
         y = radius * math.sin(math.radians(angle))
         return (cx+x, cy-y)

    def DrawGraph(self, dc):
        spacer = 10
        scaledmax = 150.0

        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dw, dh = dc.GetSize()

        # find out where to draw the title and do it
        dc.SetFont(self.titleFont)
        tw, th = dc.GetTextExtent(self.title)
        dc.DrawText(text=self.title, x=(dw-tw)/2, y=spacer)

        # find the center of the space below the title
        th = th + 2 * spacer
        cx = dw / 2
        cy = (dh - th) / 2 + th

        # calculate a scale factor to used for drawing the graph based on the minimum avaliable width or height
        mindim = min(cx, (dh-th)/2)
        scale = mindim / scaledmax

        # draw the graph axis and 'bulls eye' with rings at scaled 25, 50, 72, 100 positions
        dc.SetPen(wx.Pen('black', 1))
        dc.SetBrush(wx.TRANSPARENT_BRUSH)
        dc.DrawCircle(x=cx, y=cy, radius=25*scale)
        dc.DrawCircle(x=cx, y=cy, radius=50*scale)
        dc.DrawCircle(x=cx, y=cy, radius=75*scale)
        dc.DrawCircle(x=cx, y=cy, radius=100*scale)

        dc.SetPen(wx.Pen('black', 2))
        dc.DrawLine(x1=cx-110*scale, y1=cy, x2=cx+110*scale, y2=cy)
        dc.DrawLine(x1=cx, y1=cy-110*scale, x2=cx, y2=cy+110*scale)

        # find the coordinates for each data point, draw the labels, and find the max data point
        dc.SetFont(self.labelFont)
        maxval = 0
        angle = 0
        polypoints = []
        for i, label in enumerate(self.labels):
            val = self.data[i]
            point = self.PolarToCartesian(val*scale, angle, cx, cy)  # translate data values to polygon points
            polypoints.append(point)
            x, y = self.PolarToCartesian(125*scale, angle, cx, cy)
            dc.DrawText(label, x, y)  # draw the label
            if val > maxval:
                maxval = val
            angle = angle + 360 / len(self.labels)

        # set the brush color based on the max value (green is good,  red is bad)
        c = 'forest green'
        if maxval > 70:
            c = 'yellow'
        if maxval > 95:
            c = 'red'

        # draw the plot data as a filled polygon
        dc.SetBrush(wx.Brush(c))
        dc.SetPen(wx.Pen('navy', 3))
        dc.DrawPolygon(polypoints)

#-----------------------------------------------------------------------------

class Frame(wx.Frame):

    def __init__(self):
        super(self.__class__, self).__init__(parent=None, title='Double Buffered Drawing', size=(480, 480))
        self.plot = RadarGraph(parent=self, title='Sample Radar Plot', labels=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

        # set some random initial data values
        data = []
        for d in self.plot.GetData():
            data.append(random.randint(0, 75))
        self.plot.SetData(data)

        # create a timer to update the data values
        self.Bind(event=wx.EVT_TIMER, handler=self.OnTimeOut)
        self.timer = wx.Timer(self)
        self.timer.Start(100)

    def OnTimeOut(self, event):
        # simulate the positive or negative growth of each data value
        data = []
        for d in self.plot.GetData():
            val = d + random.uniform(-5, 5)
            if val < 0:
                val = 0
            if val > 110:
                val = 110
            data.append(val)
        self.plot.SetData(data)

class App(wx.App):

    def OnInit(self):
        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()








