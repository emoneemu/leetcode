'''
Problem statement::::

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Dummy node to simplify the code when returning the result
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Loop until both linked lists are empty and there's no carry left
        while l1 or l2 or carry:
            # Get the current digits or 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of the two digits and carry
            total = val1 + val2 + carry
            carry = total // 10  # Determine the carry for the next step
            current.next = ListNode(total % 10)  # Add the result as a new node

            # Move the current pointer to the new node
            current = current.next

            # Move to the next node in l1 and l2 if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the result list, skipping the dummy node
        return dummy.next

