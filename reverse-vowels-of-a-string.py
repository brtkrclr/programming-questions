import unittest
from typing import List

class Solution:
    @staticmethod
    def reverseVowels(s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        i,j=0,len(s)-1
        s=list(s)
        print(s)
        while i<j:
            if s[i] not in vowels:
                i+=1
            elif s[j] not in vowels:
                j-=1
            else:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(s)

class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        s = "leetcode" 
        self.assertEqual("leotcede", Solution.reverseVowels(s))

    def test_case_2(self):
        s="hello"
        self.assertEqual("holle", Solution.reverseVowels(s))
