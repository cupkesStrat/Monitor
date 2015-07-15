__author__ = 'christopherupkes'

import nagiosplugin
from   nagiosplugintest import *
import unittest

class TestNagiosPluginMethods(unittest.TestCase):

  def test_name_check(self):
      npt = NagiosPluginTest()
      check_metric = npt.probe()
      result_metric = check_metric[0]
      self.assertEqual(result_metric.name
          , 'Plugin Test')
      self.assertEqual(result_metric.value, True)


  def test_value_check(self):
      npt = NagiosPluginTest()
      check_metric = npt.probe()
      result_metric = check_metric[0]
      self.assertEqual(result_metric.value, True)



if __name__ == '__main__':
    unittest.main()