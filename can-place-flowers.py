import unittest
from typing import List

class Solution:
    @staticmethod
    def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
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