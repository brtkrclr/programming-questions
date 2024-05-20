import unittest
from typing import List

class Solution:
    @staticmethod
    def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
        Note that you must do this in-place without making a copy of the array.

        Example 1:
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]

        Example 2:
        Input: nums = [0]
        Output: [0]
        """
        j=0
        for i in range(len(nums)):
            if nums[i]!=0 and nums[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
            if nums[j]!=0:
                j+=1
        return nums
    
class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        nums = [0,1,0,3,12]
        self.assertListEqual([1,3,12,0,0], Solution.moveZeroes(nums))

    def test_case_2(self):
        nums=[0]
        self.assertListEqual([0], Solution.moveZeroes(nums))
    
    def test_case_3(self):
        nums=[0,41,0,54,1,2,0]
        self.assertListEqual([41,54,1,2,0,0,0], Solution.moveZeroes(nums))
