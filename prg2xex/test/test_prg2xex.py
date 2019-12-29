import unittest
from prg2xex import process

class TestPrg2Xex(unittest.TestCase):

    def test_prepend_meta(self):
        original = bytearray(b'\x00\xa0\xa9\x00\x8d0\x02\xa9')
        actual = bytearray()

        actual = process(original)
        expected = bytearray(b'\xff\xff\x00\xa0\x06\xa0\xa9\x00\x8d0\x02\xa9')
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()