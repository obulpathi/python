#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mymodule

import mock
import unittest

class TestRm(unittest.TestCase):
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os):
        mymodule.rm("any path")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")
