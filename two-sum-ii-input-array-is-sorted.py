import unittest
from typing import List

class Solution:
    @staticmethod
    def twoSum(numbers: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
                """
        l,r=0,len(numbers)-1

        while l<r:
            sum=numbers[l]+numbers[r]
            if sum<target:
                l+=1
            elif sum>target:
                r-=1
            else:
                return [l+1,r+1]

         
class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        nums = [2,7,11,15] 
        target = 9
        self.assertListEqual([1,2], Solution.twoSum(nums,target))
    def test_case_2(self):
        nums = [2,3,4] 
        target = 6
        self.assertListEqual([1,3], Solution.twoSum(nums,target))
            