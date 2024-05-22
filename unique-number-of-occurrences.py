import unittest
from typing import List

class Solution:
    @staticmethod
    def uniqueOccurrences(arr: List[int]) -> bool:
        dic={}
        keys=[]
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        for k in dic.values():
            if k in keys:
                return False
            keys.append(k)
        return True
    
class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        arr = [1,2]
        self.assertEqual(False, Solution.uniqueOccurrences(arr))

    def test_case_2(self):
        arr = [-3,0,1,-3,1,1,1,-3,10,0]
        self.assertEqual(True, Solution.uniqueOccurrences(arr))
    
    def test_case_3(self):
        arr=[1,2,2,1,1,3]
        self.assertEqual(True, Solution.uniqueOccurrences(arr))
