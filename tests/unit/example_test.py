import io
import sys
import unittest

from sample_package import example

class TestExample(unittest.TestCase):
  def setUp(self) -> None:
      super().setUp()
      self.stdout = io.StringIO()
      sys.stdout = self.stdout

  def tearDown(self) -> None:
      super().tearDown()
      sys.stdout = sys.__stdout__


  def test_hello(self):
    input = 'Cory'
    want = 'Hello, Cory!\n'

    example.hello(input)
    got = self.stdout.getvalue()

    self.assertEqual(want, got)

if __name__ == '__main__':
  unittest.main()
