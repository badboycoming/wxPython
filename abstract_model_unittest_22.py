#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-----------------------------------------------------------------------------
# Purpose: Use the class AbstractModel, unittest
#-----------------------------------------------------------------------------

import wx
import unittest
import abstract_model_21 as abstract_model

class TestAbstractModel(unittest.TestCase):  # define a test case class

    def setUp(self):  # pre-condition, make necessary config
        self.app = abstract_model.App()
        self.frame = abstract_model.Frame()

    def tearDown(self):  # post-condition, make necessary clear
        self.frame.Destroy()

    #-------------------------------------------------------------------------

    def testApple(self):  # define a test case
        self.frame.OnApple(event=None)
        self.assertEqual(first='Apple', second=self.frame.model.first, msg='Apple first is wrong')
        self.assertEqual(first='U.S.', second=self.frame.model.last, msg='Apple last is wrong')

    def testSamsung(self):  # define another test case
        self.frame.OnSamsung(event=None)
        self.assertEqual(first='Samsung', second=self.frame.model.first, msg='Samsung first is wrong')
        self.assertEqual(first='Kroea', second=self.frame.model.last, msg='Samsung last is wrong')

    def testHuawei(self):
        self.frame.OnHuawei(event=None)
        self.assertEqual(first='Huawei', second=self.frame.model.first, msg='Huawei first is wrong')
        self.assertEqual(first='China', second=self.frame.model.last, msg='Huawei last is wrong')

    def testOppo(self):
        self.frame.OnOppo(event=None)
        self.assertEqual(first='Oppo', second=self.frame.model.first, msg='Oppo first is wrong')
        self.assertEqual(first='China', second=self.frame.model.last, msg='Oppo last is wrong')

    #-------------------------------------------------------------------------

    def testEvent(self):  # only take Huawei as an example
        panel = self.frame.GetChildren()[0]

        for each in panel.GetChildren():
            if each.GetLabel() == 'Huawei':
                hw = each
                break

        # generate click event
        event = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, hw.GetId())
        hw.GetEventHandler().ProcessEvent(event)

        self.assertEqual(first='Huawei', second=self.frame.model.first, msg='Event test failed for first item')
        self.assertEqual(first='China', second=self.frame.model.last, msg='Event test failed for last item')

# define a test suite
def AMsuite():
    sut = unittest.makeSuite(testCaseClass=TestAbstractModel, prefix='test')
    return sut

if __name__ == '__main__':
    unittest.main(defaultTest='AMsuite')





