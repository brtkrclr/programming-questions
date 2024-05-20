import unittest
from typing import List

class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        '''
        Given an input string s, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
        Return a string of the words in reverse order concatenated by a single space. Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

        Example 1:
        Input: s = "the sky is blue"
        Output: "blue is sky the"

        Example 2:
        Input: s = "  hello world  "
        Output: "world hello"
        Explanation: Your reversed string should not contain leading or trailing spaces.

        Example 3:
        Input: s = "a good   example"
        Output: "example good a"
        Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
        '''
        a=s.split()
        i,j=0,len(a)-1

        while i<j:
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
        return ' '.join(a)

class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        s = "  hello world  "
        self.assertEqual("world hello", Solution.reverseWords(s))

    def test_case_2(self):
        s="the sky is blue"
        self.assertEqual("blue is sky the", Solution.reverseWords(s))
    
    def test_case_3(self):
        s="a good   example"
        self.assertEqual("example good a", Solution.reverseWords(s))
