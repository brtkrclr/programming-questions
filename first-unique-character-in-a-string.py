class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int

        Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

        Example 1:

        Input: s = "leetcode"
        Output: 0
        Example 2:

        Input: s = "loveleetcode"
        Output: 2
        Example 3:

        Input: s = "aabb"
        Output: -1
        """
        for i in s:
            a=s.count(i)
            if a==1:
                return (s.index(i))
                break
        return (-1)
