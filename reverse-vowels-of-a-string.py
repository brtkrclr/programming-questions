import unittest
from typing import List

class Solution:
    @staticmethod
    def reverseVowels(s: str) -> str:
        '''
        Given a string s, reverse only all the vowels in the string and return it. The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

        Example 1:
        Input: s = "hello"
        Output: "holle"

        Example 2:
        Input: s = "leetcode"
        Output: "leotcede"
        
        Constraints:

        1 <= s.length <= 3 * 105
        s consist of printable ASCII characters.
        '''
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
