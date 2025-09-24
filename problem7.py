"""
Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1


"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Handle negative numbers
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_num = 0

        while x != 0:
            # Get the last digit
            digit = x % 10
            # Remove the last digit from x
            x = x // 10

            # Check for overflow before actually updating reversed_num
            if sign == 1 and reversed_num > ( 2**31 - 1 - digit) // 10:
                return 0
            if sign == -1 and reversed_num > ( 2**31 - digit) // 10:
                return 0

            # Update the reversed number
            reversed_num = reversed_num * 10 + digit

        return sign * reversed_num