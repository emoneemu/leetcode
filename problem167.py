from typing import List

class Solution(object):
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0 ,len(numbers)-1
        count = 0
        while count!=len(numbers)-1:
            if numbers[l]+numbers[r]== target:
                return [(l+1),(r+1)]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            count += 1