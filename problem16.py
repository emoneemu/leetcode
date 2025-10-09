"""
problem set 16: 3 Sum closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104

"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        # Initialize with the sum of the first three (after sort)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            # Optional micro-optimization to skip same anchors
            if i > 0 and nums[i] == nums[i - 1]:
                pass  # not strictly necessary for correctness

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                # Update closest if this is better
                if abs(s - target) < abs(closest - target):
                    closest = s

                if s == target:
                    return target  # exact match can't be beaten
                elif s < target:
                    l += 1
                else:
                    r -= 1

        return closest