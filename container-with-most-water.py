import unittest
from typing import List

class Solution:
    @staticmethod
    def maxArea(height: List[int]) -> int:
        '''
        https://leetcode.com/problems/container-with-most-water/description/
        
        You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
        Find two lines that together with the x-axis form a container, such that the container contains the most water.
        Return the maximum amount of water a container can store.
        Notice that you may not slant the container.
        '''
        l,r=0,len(height)-1
        area=0
        while l<r:
            area=max(area,min(height[r],height[l])*(r-l)) #min(r,l) to get min value since they are not equal water will stone if we select max one, so instead we get min
            if height[r]<=height[l]:
                r-=1
            elif height[r]>height[l]:
                l+=1
        return area

class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        height = [1,8,6,2,5,4,8,3,7]
        self.assertEqual(49, Solution.maxArea(height))
    def test_case_2(self):
        height = [1,1]
        self.assertEqual(1, Solution.maxArea(height))
            