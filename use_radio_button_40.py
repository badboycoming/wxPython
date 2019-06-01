#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: To demo how to use radio button.
#-----------------------------------------------------------------------------

import wx

class RadioButtonFrame(wx.Frame):
    
    def __init__(self):
        super(self.__class__, self).__init__(parent=None, id=-1, title='Radio Button')
        panel = wx.Panel(parent=self, id=-1)
        
        # create radioButton
        rb1 = wx.RadioButton(parent=panel, id=-1, label='Li Lei', style=wx.RB_GROUP)
        rb2 = wx.RadioButton(parent=panel, id=-1, label='Hanmm')
        rb3 = wx.RadioButton(parent=panel, id=-1, label='Jim')
        
        # create text controls
        txt1 = wx.TextCtrl(parent=panel, id=-1, value='')
        txt2 = wx.TextCtrl(parent=panel, id=-1, value='')
        txt3 = wx.TextCtrl(parent=panel, id=-1, value='')
        
        # create a sizer
        subSizer = wx.FlexGridSizer(rows=3, cols=2, hgap=6, vgap=6)
        # subSizer.AddMany([rb1, txt1, rb2, txt2, rb3, txt3])  # not use this style, the control grain size too big
        subSizer.Add(item=rb1, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL)
        subSizer.Add(item=txt1, proportion=0)
        subSizer.Add(item=rb2, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL)
        subSizer.Add(item=txt2, proportion=0)
        subSizer.Add(item=rb3, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL)
        subSizer.Add(item=txt3, proportion=0)

        # layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(item=subSizer, proportion=0, flag=wx.ALIGN_CENTRE|wx.ALL, border=50)
        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)
        self.CenterOnScreen()

        #####################################################
        # connect the radioButton and text with a simple dict
        #####################################################

        self.txts = {'Li Lei': txt1, 'Hanmm': txt2, 'Jim': txt3}
        
        # set the txt initial state
        for eachTxt in [txt2, txt3]:
            eachTxt.Enable(False)  # txt1 enable in default
            
        # bind the radioButton event
        for eachRb in [rb1, rb2, rb3]:
            self.Bind(event=wx.EVT_RADIOBUTTON, handler=self.OnRadio, source=eachRb)
            
        self.selectedTxt = txt1

    def OnRadio(self, event):
        if self.selectedTxt is not None:
            self.selectedTxt.Enable(False)  # disable the old txt window
        radioSelected = event.GetEventObject()
        txt = self.txts[radioSelected.GetLabel()]
        txt.Enable(True)  # enable the new txt window
        self.selectedTxt = txt
            
class RadioButtonApp(wx.App):
    
    def OnInit(self):
        self.frame = RadioButtonFrame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
    
if __name__ == '__main__':
    
    app = RadioButtonApp()
    app.MainLoop()
    
    
    
        