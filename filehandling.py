import unittest
class test1(unittest.TestCase):
    def test_func (self):
        ex=1
        self.assertEqual(ex, 2*5 )
    def test_funct (self):
        ex=2
        self.assertEqual(ex, 2 )


if __name__=='__main__':
    unittest.main()
        