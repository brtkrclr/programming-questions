import unittest
from typing import List
class Solution:
    @staticmethod
    def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
        greatestNumber=max(candies)
        res=[]
        for i in candies:
            if i+extraCandies>=greatestNumber:
                res.append(True)
            else:
                res.append(False)
        return res

class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        candies = [4,2,1,1,2]
        extraCandies = 1 
        self.assertListEqual([True,False,False,False,False], Solution.kidsWithCandies(candies,extraCandies))

    def test_case_2(self):
        candies = [2,3,5,1,3]
        extraCandies = 3 
        self.assertListEqual([True,True,True,False,True], Solution.kidsWithCandies(candies,extraCandies))
    
    def test_case_3(self):
        candies = [12,1,12]
        extraCandies=10
        self.assertEqual([True,False,True] , Solution.kidsWithCandies(candies,extraCandies))