class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        Given an integer x, return true if x is a palindrome, and false otherwise.

        Example 1:

        Input: x = 121
        Output: true
        Explanation: 121 reads as 121 from left to right and from right to left.
        Example 2:

        Input: x = -121
        Output: false
        Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
        Example 3:

        Input: x = 10
        Output: false
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

        '''
        #Solution 1
        str_x=list(str(x))  
        rev_str_x=list(reversed(str_x))
        if str_x==rev_str_x:
            return True
        else:
            return False

        #Solution 2
        old_x = str(x)
        new_x = old_x[::-1]
        return old_x == new_x
