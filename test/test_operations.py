import unittest


class TestArimtOp(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
    def test_upper(self):
        self.assertEqual('tree'.upper(), 'TREE')
        
        
if __name__ == '__main__':
    unittest.main()