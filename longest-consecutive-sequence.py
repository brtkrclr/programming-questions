import unittest
from typing import List

class Solution:
    @staticmethod
    def longestConsecutive(nums: List[int]) -> int:
        number_set=set(nums)
        count=0

        # |1,2,3,4|...|100|...|200| so assume that a sequence is a block, and a sequence start with if i-1 for i doesnt exist (left handside) end with if i+1 exists for i
        for i in number_set:
            if (i-1) not in number_set:
                length=1
                while (i+length) in number_set:
                    length+=1
                count=max(length,count)
        return count
        
                
    
class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        nums = [3,100,1,200,2,4]
        self.assertEqual(4, Solution.longestConsecutive(nums))
    def test_case_2(self):
        nums = [0]
        self.assertEqual(1, Solution.longestConsecutive(nums))