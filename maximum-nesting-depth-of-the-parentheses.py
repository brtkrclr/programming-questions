import unittest
from typing import List

class Solution:
    @staticmethod
    def maxDepth(s: str) -> int:
        '''
        Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.
        Example 1:
        Input: s = "(1+(2*3)+((8)/4))+1"
        Output: 3
        Explanation:
        Digit 8 is inside of 3 nested parentheses in the string.

        Example 2:
        Input: s = "(1)+((2))+(((3)))"
        Output: 3
        Explanation:
        Digit 3 is inside of 3 nested parentheses in the string.

        Example 3:
        Input: s = "()(())((()()))"
        Output: 3
        '''
        stack=[]
        count=0
        for i in s:
            if i=="(":
                stack.append(i)
                print(stack)
            elif i==")":
                count=max(count,len(stack)) #before popping the closing paranthes count the stack and get the max so far
                stack.pop()
                print(stack)
        return count
    
class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        s = "(1+(2*3)+((8)/4))+1"
        self.assertEqual(3, Solution.maxDepth(s))

    def test_case_2(self):
        s = "(1)+((2))+(((3)))"
        self.assertEqual(3, Solution.maxDepth(s))

    def test_case_3(self):
        s = "()(())((()()))"
        self.assertEqual(3, Solution.maxDepth(s))