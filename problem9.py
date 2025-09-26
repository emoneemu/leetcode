"""
Palindrome Number

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


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?

"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Numbers ending with 0 (except 0 itself) are not palindromes
        if x % 10 == 0 and x != 0:
            return False

        # Reverse half of the number and compare
        reversed_half = 0
        original = x

        while x > reversed_half:
            # Get the last digit and add it to reversed_half
            reversed_half = reversed_half * 10 + x % 10
            # Remove the last digit from x
            x //= 10

        # For even digits: x == reversed_half
        # For odd digits: x == reversed_half // 10 (middle digit doesn't matter)
            return x == reversed_half or x == reversed_half // 10  # Negative numbers are not palindromes
        if x < 0:
            return False

        # Numbers ending with 0 (except 0 itself) are not palindromes
        if x % 10 == 0 and x != 0:
            return False

        # Reverse half of the number and compare
        reversed_half = 0
        original = x

        while x > reversed_half:
            # Get the last digit and add it to reversed_half
            reversed_half = reversed_half * 10 + x % 10
            # Remove the last digit from x
            x //= 10

        # For even digits: x == reversed_half
        # For odd digits: x == reversed_half // 10 (middle digit doesn't matter)
        return x == reversed_half or x == reversed_half // 10