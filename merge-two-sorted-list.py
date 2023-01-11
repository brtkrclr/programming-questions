# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):

        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        You are given the heads of two sorted linked lists list1 and list2.
		Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
		Return the head of the merged linked list.

		Example 1:

		Input: list1 = [1,2,4], list2 = [1,3,4]
		Output: [1,1,2,3,4,4]
		Example 2:

		Input: list1 = [], list2 = []
		Output: []
		Example 3:

		Input: list1 = [], list2 = [0]
		Output: [0]
		 

		Constraints:

		The number of nodes in both lists is in the range [0, 50].
		-100 <= Node.val <= 100
		Both list1 and list2 are sorted in non-decreasing order.
        """
        root=ListNode()
        tail=root     # output linked list since it will be empty initially we need to define it 

        while l1 and l2:
            if l1.val<l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail = tail.next # output=1,1,2,3, it goes to the next elements

        #lets assume size are not equal, we need to get the remaining portion. That's why we are gettin the remaining and adding at the end.
        if l1:
            tail.next=l1
        elif l2:
            tail.next=l2
        return root.next
