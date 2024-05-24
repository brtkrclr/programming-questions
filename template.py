import unittest
from typing import List

class Solution:
    @staticmethod
    def problem(n: int) -> bool:
        return True
    
class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        n = [1,0,0,0,1]
        self.assertEqual(True, Solution.problem(n))
