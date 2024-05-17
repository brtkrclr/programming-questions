import unittest
from typing import List
class Solution:
    '''
    Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
    answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
    Note that the integers in the lists may be returned in any order.

    Example 1:

    Input: nums1 = [1,2,3], nums2 = [2,4,6]
    Output: [[1,3],[4,6]]
    Explanation:
    For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
    For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
    
    Example 2:
    Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
    Output: [[3],[]]
    Explanation:
    For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
    Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
    '''
    @staticmethod
    def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        s1=set(nums1)
        s2=set(nums2)
        l1=list(s1-s2)
        l2=list(s2-s1)
        return [l1,l2]

    @staticmethod
    def findDifferenceSecondWay(nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1=set(nums1)
        s2=set(nums2)
        l1 = []
        for num in s1:
            if num not in s2:
                l1.append(num)
        l2 = []
        for num in s2:
            if num not in s1:
                l2.append(num)

        return [l1,l2]

class findDiffTest(unittest.TestCase):
    def test_case_1(self):
        nums1 = [1,2,3]
        nums2 = [2,4,6]
        result = Solution.findDifference(nums1,nums2)
        self.assertListEqual([[1,3],[4,6]], result)

    def test_case_2(self):
        nums1 = [1,2,3]
        nums2 = [2,4,6]
        result = Solution.findDifferenceSecondWay(nums1,nums2)
        self.assertListEqual([[1,3],[4,6]], result)

    def test_case_3(self):
        nums1 = [1,2,3,3]
        nums2 = [1,1,2,2]
        result = Solution.findDifference(nums1,nums2)
        self.assertListEqual([[3],[]], result)

    def test_case_4(self):
        nums1 = [1,2,3,3]
        nums2 = [1,1,2,2]
        result = Solution.findDifferenceSecondWay(nums1,nums2)
        self.assertListEqual([[3],[]], result)