import unittest
from typing import List

class Solution:
    @staticmethod
    def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
        '''
        You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
        Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

        Example 1:
        Input: flowerbed = [1,0,0,0,1], n = 1
        Output: true

        Example 2:
        Input: flowerbed = [1,0,0,0,1], n = 2
        Output: false
        '''
        for i in range(len(flowerbed)):
            if n==0:
                return True
            #if first element or current's prev element ==0 AND current elemen ==0 AND last or current's+1 element ==0 
            if ((i==0 or flowerbed[i-1]==0)) and (flowerbed[i]==0) and ((i==len(flowerbed)-1 or flowerbed[i+1]==0)):
                flowerbed[i] = 1
                n-=1
                if n==0:
                    return True
        return False
    
class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        flowerbed = [1,0,0,0,1]
        n=1
        self.assertEqual(True, Solution.canPlaceFlowers(flowerbed,n))

    def test_case_2(self):
        flowerbed = [1,0,0,0,1]
        n=2
        self.assertEqual(False, Solution.canPlaceFlowers(flowerbed,n))
    
    def test_case_3(self):
        flowerbed = [1,0,0,0,1,0,0]
        n=2
        self.assertEqual(True, Solution.canPlaceFlowers(flowerbed,n))