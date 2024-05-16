class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        '''
        Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

        Example 1:

        Input: nums = [3,2,3]
        Output: 3
        Example 2:

        Input: nums = [2,2,1,1,1,2,2]
        Output: 2
        

        Constraints:

        n == nums.length
        1 <= n <= 5 * 104
        -109 <= nums[i] <= 109
        

        Follow-up: Could you solve the problem in linear time and in O(1) space?
        '''
        #O(n) that's the basic solution        
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        return (max(dic,keys=dic.get()))
    
    def majorityConstantTime(self, nums: List[int]) -> int:
        #O(1) --> Please see Boyer-Moore Algorithm
        count=0
        res=0
        for i in nums:
            if count==0:
                res=i
            if i==res:
                count +=1
            else:
                -1
        return res