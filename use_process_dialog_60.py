#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use process dialog.
#-----------------------------------------------------------------------------

import wx
import random

class App(wx.App):

    def OnInit(self):

        progressMax = 100
        dlg = wx.ProgressDialog(title='Progress Box',
                                message='Progressing...',
                                maximum=progressMax,
                                parent=None,
                                style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
        keepGoing = True
        cnt = 0
        while keepGoing and cnt < progressMax:

            cnt += random.randint(1, 10)
            if cnt > 100:
                cnt = 100

            wx.Sleep(1)
            keepGoing = dlg.Update(cnt)[0]  # Update(self, int value, String newmsg) --> (continue, skip)
            # print 'keepGoing =', keepGoing
        dlg.Destroy()

        return True

if __name__ == '__main__':

    app = App()
    app.MainLoop()



