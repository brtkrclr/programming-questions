import unittest
from typing import List

class Solution:
    @staticmethod
    def missingNumber(nums: List[int]) -> int:
        n=len(nums)
        for i in range(n+1):
            if i not in nums:
              return i
    
class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        nums = [3,0,1]
        self.assertEqual(2, Solution.missingNumber(nums))
    def test_case_2(self):
        nums = [0,1]
        self.assertEqual(2, Solution.missingNumber(nums))
    def test_case_3(self):
        nums = [9,6,4,2,3,5,7,0,1]
        self.assertEqual(8, Solution.missingNumber(nums))
