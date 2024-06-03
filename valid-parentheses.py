import unittest
from typing import List

class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        '''
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.

        Example 1:
        Input: s = "()"
        Output: true

        Example 2:
        Input: s = "()[]{}"
        Output: true

        Example 3:
        Input: s = "(]"
        Output: false

        '''
        arr = []
        paranthesis = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            if i in paranthesis:
                arr.append(i)
            elif  len(arr)==0 or paranthesis[arr.pop()] != i: #ex: paranthesis["("] == ")"  
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