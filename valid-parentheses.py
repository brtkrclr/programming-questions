import unittest
from typing import List

class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        arr = []
        paranthesis = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            if i in paranthesis:
                arr.append(i)
            elif  len(arr)==0 or paranthesis[arr.pop()] != i:
                return False
        return len(arr)==0
    
class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        s = "()"
        self.assertEqual(True, Solution.isValid(s))

    def test_case_2(self):
        s = "()[]{}"
        self.assertEqual(True, Solution.isValid(s))
    
    def test_case_3(self):
        s = "(}"
        self.assertEqual(False, Solution.isValid(s))