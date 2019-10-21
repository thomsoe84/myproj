import unittest
import hitung

class TestHitung(unittest.TestCase):
    def test_kali_dua(self):
        self.assertTrue(hitung.kali_dua(5) == 10)
        self.assertTrue(hitung.kali_dua(6) == 12)

if __name__ == '__main__':
    unittest.main()
