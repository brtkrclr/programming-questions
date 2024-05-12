class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        Given two strings s and t, return true if s is a subsequence of t, or false otherwise. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

        Example 1:

        Input: s = "abc", t = "ahbgdc"
        Output: true
        Example 2:

        Input: s = "axc", t = "ahbgdc"
        Output: false

        Constraints:
        0 <= s.length <= 100
        0 <= t.length <= 104
        s and t consist only of lowercase English letters.
        '''
        '''
        First Solution

        if len(s)==0: --> if s is empty it is a substring
            return True
        else:
            j=0
            for i in range(len(t)):
            if t[i]==s[j] and j<len(s): -> check if length of substring is less then incremented values and current t[i] and s[j]
                j+=1
            if j==len(s):  --> if incremented value become the length of s return true
                return True
            return False
        '''

        i=0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i==len(s):
            return True
        else:
            return False