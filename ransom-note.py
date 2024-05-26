import unittest
from typing import List

class Solution:
    @staticmethod
    def canConstruct( ransomNote: str, magazine: str) -> bool:
        '''
        Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise. Each letter in magazine can only be used once in ransomNote.

        Example 1:
        Input: ransomNote = "a", magazine = "b"
        Output: false

        Example 2:
        Input: ransomNote = "aa", magazine = "ab"
        Output: false

        Example 3:
        Input: ransomNote = "aa", magazine = "aab"
        Output: true
        '''
        dic={}

        for i in magazine:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in ransomNote:
            if i in dic and dic[i]>0:
                dic[i]-=1
            else:
                return False
        return True
    
class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        ransomNote = "a"
        magazine = "b"
        self.assertEqual(False, Solution.canConstruct(ransomNote,magazine))
    def test_case_2(self):
        ransomNote = "aa"
        magazine = "ab"
        self.assertEqual(False, Solution.canConstruct(ransomNote,magazine))
    def test_case_3(self):
        ransomNote = "aa"
        magazine = "aab"
        self.assertEqual(True, Solution.canConstruct(ransomNote,magazine))
