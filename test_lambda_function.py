import unittest
from lambda_function import gather_anagrams

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Basic unit test to verify anagram of cinema including upper+lower case        
        """
        test_word = "iceman"
        get_result = gather_anagrams(test_word)
        expected = ['anemic', 'cinema', 'iceman']
        self.assertEqual(get_result, expected)

if __name__ == '__main__':
    unittest.main()
