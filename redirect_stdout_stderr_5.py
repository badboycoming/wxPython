#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Redirect stdout, stderr.
#-----------------------------------------------------------------------------

import wx
import sys

class Frame(wx.Frame):

    def __init__(self, parent, id, title):
        print 'Frame __init__'
        super(self.__class__, self).__init__(parent=parent, id=id, title=title, size=(800, 600))

        self.CenterOnScreen()

class App(wx.App):

    def __init__(self, redirect=True, filename=None):
        print 'App __init__'
        super(self.__class__, self).__init__(redirect=redirect, filename=filename)

    def OnInit(self):
        self.frame = Frame(parent=None, id=-1, title='Redirect Stdout & Stderr')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print >> sys.stderr, 'A pretend error message :p'
        return True

    # NOTE: the OnExit() method of your wx.App subclass is called after the last window
    #       closed, but before wxPython's internal cleanup. You can use this method to
    #       clean up any non-wxPython resources you've create, for example, a database connection.
    def OnExit(self):
        print 'Now GUI have closed, add realease rescourses and clear trash methods here!'

if __name__ == '__main__':

    #app = App(redirect=False)  # if redirect is False, all stdout & stderr not direct to wxFrame [Test under MS-Windows]
    #app = App(redirect=True)  # if redirect is True, when App created, all stdout & stderr direct to wxFrame [Test under MS-Windows]
    app = App(redirect=True, filename='./redirect_stdout_stderr_5.log')

    print '>>> Before MainLoop'
    app.MainLoop()
    print '>>> After MainLoop'




