import unittest
from typing import List
class Solution:
    @staticmethod
    def mergeAlternately(word1: str, word2: str) -> str:
        res=[]
        i=0
        j=0
        while i<len(word1) and j<len(word2):
            res.append(word1[i])
            i+=1
            res.append(word2[j])
            j+=1
        res.append(word1[i:]) # if word1 is longer it will add the remaining part
        res.append(word2[j:]) # it will add starting from j to end (j is the last one since we already incremented the value)
        return ''.join(res)

class mergeAlterTest(unittest.TestCase):
    def test_case_1(self):
        word1 = "abc"
        word2 = "qrs" 
        self.assertEqual("aqbrcs", Solution.mergeAlternately(word1,word2))

    def test_case_2(self):
        word1 = "ab"
        word2 = "pqrs" 
        self.assertEqual("apbqrs", Solution.mergeAlternately(word1,word2))
    
    def test_case_3(self):
        word1 = "abcd"
        word2 = "pq" 
        self.assertEqual("apbqcd", Solution.mergeAlternately(word1,word2))