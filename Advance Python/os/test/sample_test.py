import unittest
import Explorer


class ScoreListTest(unittest.TestCase):

    def test_1(self):
        result = {'sample_test_media/A': 1, 'sample_test_media/A/dir': 1}
        self.assertEqual(result, Explorer.explore("txt", "sample_test_media"), "\nخروجی تابع برای پسوند txt و پوشه‌ی sample_test_media (این پوشه در فایل پروژه اولیه سوال قرار دارد) برابر\n{'sample_test_media/A': 1, 'sample_test_media/A/dir': 1}\nاست.")

    def test_2(self):
        result = {'sample_test_media/A/A/b': 1}
        self.assertEqual(result, Explorer.explore("mkv", "sample_test_media"), "\nخروجی تابع برای پسوند mkv و پوشه‌ی sample_test_media (این پوشه در فایل پروژه اولیه سوال قرار دارد) برابر\n{'sample_test_media/A/A/b': 1}\nاست.")