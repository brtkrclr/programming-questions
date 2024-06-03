import unittest
from typing import List

class Solution:
    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        n=[]
        for i in range(len(nums)):
            if target-nums[i] in dic:
                print([dic[target - nums[i]],i])
                return ([dic[target - nums[i]],i])
            else:
                dic[nums[i]]=i
         
class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        nums = [2,7,11,15] 
        target = 9
        self.assertListEqual([0,1], Solution.twoSum(nums,target))
    def test_case_2(self):
        nums = [3,2,4] 
        target = 6
        self.assertListEqual([1,2], Solution.twoSum(nums,target))
            