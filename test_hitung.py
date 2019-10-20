import unittest
import hitung

class TestHitung(unittest.TestCase):
    def test_kali_dua(self):
        self.assertTrue(hitung.kali_dua(5) == 10)

if __name__ == '__main__':
    unittest.main()