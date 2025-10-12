"""
Leetcode 18

problem statement:
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Prune: smallest possible sum > target -> break; largest < target -> continue
            min1 = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
            if min1 > target:
                break
            max1 = nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3]
            if max1 < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # More pruning on the inner loop
                min2 = nums[i] + nums[j] + nums[j + 1] + nums[j + 2]
                if min2 > target:
                    break
                max2 = nums[i] + nums[j] + nums[n - 1] + nums[n - 2]
                if max2 < target:
                    continue

                l, r = j + 1, n - 1
                need = target - nums[i] - nums[j]

                while l < r:
                    s = nums[l] + nums[r]
                    if s == need:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif s < need:
                        l += 1
                    else:
                        r -= 1

        return res