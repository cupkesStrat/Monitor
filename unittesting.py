__author__ = 'christopherupkes'

import nagiosplugin
from   nagiosplugintest import *
from   macload import *
import unittest

class TestNagiosPluginMethods(unittest.TestCase):

  def test_base_name_check(self):
      npt = NagiosPluginTest()
      check_metric = npt.probe()
      result_metric = check_metric[0]
      self.assertEqual(result_metric.name
          , 'Plugin Test')
      self.assertEqual(result_metric.value, True)


  def test_base_value_check(self):
      npt = NagiosPluginTest()
      check_metric = npt.probe()
      result_metric = check_metric[0]
      self.assertEqual(result_metric.value, True)

  def test_macload_name_check(self):
      mlt = MacLoad()
      result = mlt.probe()
      self.assertEqual(next(result).name,'load1')
      self.assertEqual(next(result).name, 'load5')
      self.assertEqual(next(result).name, 'load15')

  def test_macload_value_check(self):
      mlt = MacLoad()
      result = mlt.probe()
      self.assertGreater(next(result).value,0)
      self.assertGreater(next(result).value,0)
      self.assertGreater(next(result).value,0)


if __name__ == '__main__':
    unittest.main()