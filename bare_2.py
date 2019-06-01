#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Purpose: A minimum wxPython frame.
#-------------------------------------------------------------------------------

#########
# Step 1: Import the necessary wxPython package.
#         NOTE, should import wx first, then other wx related package, non-wx package can be in any import order.
#########
import wx

#########
# Step 2: Subclass the wxPython frame class
#########
class SubFrame(wx.Frame):
    def __init__(self, parent, title):
        # wx.Frame.__init__(self, parent=parent, title=title, size=(800, 600))
        super(self.__class__, self).__init__(parent=parent, title=title, size=(800, 600))
        self.CenterOnScreen()

#########
# Step 3: Subclass the wxPython application class
#########
class SubApp(wx.App):

    #######
    # NOTE: The __init__ method in the Application is unnecessary
    #######
    def __init__(self):
        wx.App.__init__(self)

    #########
    # Step 4: Define an application initialize method, should named 'OnInit', and should return True
    #########
    def OnInit(self):
        self.frame = SubFrame(parent=None, title='Bare')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':

    #########
    # Step 5: Create an application class instance
    #########
    app = SubApp()

    #########
    # Step 6: Enter the application main event loop
    #########
    app.MainLoop()




